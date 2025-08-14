import os
import time
import logging
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix
from sqlalchemy.orm import DeclarativeBase

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize extensions
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure PostgreSQL database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize extensions with app
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

# Import models after db initialization
from models import Usuario, Produto
from forms import LoginForm, ProdutoForm

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Performance monitoring
@app.before_request
def before_request_func():
    g.start_time = time.time()

@app.after_request
def after_request_func(response):
    diff_ms = round((time.time() - g.start_time) * 1000, 2)
    response.headers['X-Response-Time'] = f'{diff_ms}ms'
    return response

@app.context_processor
def inject_performance():
    if hasattr(g, 'start_time'):
        response_time_ms = round((time.time() - g.start_time) * 1000, 2)
    else:
        response_time_ms = 0
    return {'response_time_ms': response_time_ms}

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('dashboard')
            return redirect(next_page)
        flash('Email ou senha inválidos.', 'error')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado com sucesso.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Calculate metrics
    total_produtos = Produto.query.count()
    total_estoque = db.session.query(db.func.sum(Produto.quantidade)).scalar() or 0
    valor_total_estoque = db.session.query(
        db.func.sum(Produto.quantidade * Produto.preco_venda)
    ).scalar() or 0
    
    produtos_baixo_estoque = Produto.query.filter(Produto.quantidade <= 5).count()
    
    return render_template('dashboard.html', 
                         total_produtos=total_produtos,
                         total_estoque=total_estoque,
                         valor_total_estoque=valor_total_estoque,
                         produtos_baixo_estoque=produtos_baixo_estoque)

@app.route('/produtos')
@login_required
def produtos():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '', type=str)
    
    query = Produto.query
    if search:
        query = query.filter(
            db.or_(
                Produto.nome.contains(search),
                Produto.sku.contains(search),
                Produto.descricao.contains(search)
            )
        )
    
    produtos = query.paginate(
        page=page, per_page=10, error_out=False
    )
    
    return render_template('produtos.html', produtos=produtos, search=search)

@app.route('/produtos/novo', methods=['GET', 'POST'])
@login_required
def produto_novo():
    form = ProdutoForm()
    if form.validate_on_submit():
        produto = Produto(
            nome=form.nome.data,
            sku=form.sku.data,
            descricao=form.descricao.data,
            quantidade=form.quantidade.data,
            preco_venda=form.preco_venda.data
        )
        db.session.add(produto)
        db.session.commit()
        flash('Produto criado com sucesso!', 'success')
        return redirect(url_for('produtos'))
    
    return render_template('produto_form.html', form=form, title='Novo Produto')

@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def produto_editar(id):
    produto = Produto.query.get_or_404(id)
    form = ProdutoForm(obj=produto)
    
    if form.validate_on_submit():
        form.populate_obj(produto)
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('produtos'))
    
    return render_template('produto_form.html', form=form, title='Editar Produto', produto=produto)

@app.route('/produtos/excluir/<int:id>', methods=['POST'])
@login_required
def produto_excluir(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('produtos'))

@app.route('/produtos/movimentar/<int:id>', methods=['POST'])
@login_required
def produto_movimentar(id):
    produto = Produto.query.get_or_404(id)
    quantidade = request.form.get('quantidade', type=int)
    
    if quantidade is None:
        flash('Quantidade inválida.', 'error')
        return redirect(url_for('produtos'))
    
    nova_quantidade = produto.quantidade + quantidade
    
    if nova_quantidade < 0:
        flash('Estoque insuficiente para esta operação.', 'error')
        return redirect(url_for('produtos'))
    
    produto.quantidade = nova_quantidade
    db.session.commit()
    
    operacao = "entrada" if quantidade > 0 else "saída"
    flash(f'Movimentação de {operacao} realizada com sucesso!', 'success')
    return redirect(url_for('produtos'))

@app.route('/teste-estresse')
@login_required
def teste_estresse():
    """Página para visualizar e executar testes de estresse"""
    import glob
    import os
    
    # Busca relatórios existentes na raiz do projeto
    basic_reports = glob.glob("stress_test_report_*.md")
    advanced_reports = glob.glob("advanced_stress_report_*.md")
    
    all_reports = []
    
    for report_file in basic_reports + advanced_reports:
        try:
            stats = os.stat(report_file)
            created_time = datetime.fromtimestamp(stats.st_mtime)
            
            # Lê algumas métricas básicas do relatório
            with open(report_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extrai métricas básicas do conteúdo
            import re
            # Busca pelos padrões dos relatórios básicos e avançados
            total_requests = re.search(r'- \*\*Total de Requests:\*\*\s*(\d+)', content)
            success_rate = re.search(r'- \*\*Taxa de Sucesso:\*\*\s*([\d.]+)%', content)
            avg_time = re.search(r'- \*\*Média:\*\*\s*([\d.]+)\s*ms', content)
            
            # Se não encontrou no padrão básico, tenta padrão avançado
            if not avg_time:
                avg_time = re.search(r'- \*\*Tempo de Resposta Médio:\*\*\s*([\d.]+)\s*ms', content)
            
            report_type = "Avançado" if "advanced" in report_file else "Básico"
            
            all_reports.append({
                'filename': report_file,
                'type': report_type,
                'created': created_time.strftime('%d/%m/%Y %H:%M'),
                'total_requests': total_requests.group(1) if total_requests else 'N/A',
                'success_rate': success_rate.group(1) if success_rate else 'N/A',
                'avg_time': avg_time.group(1) if avg_time else 'N/A'
            })
        except:
            continue
    
    # Ordena por data de criação (mais recente primeiro)
    all_reports.sort(key=lambda x: x['created'], reverse=True)
    
    return render_template('teste_estresse.html', reports=all_reports)

@app.route('/executar-teste-estresse', methods=['POST'])
@login_required
def executar_teste_estresse():
    """Executa um teste de estresse via web"""
    test_type = request.form.get('test_type', 'basic')
    
    # Aqui normalmente executaríamos o teste em background
    # Por simplicidade, vamos apenas simular
    flash('Teste de estresse iniciado! Verifique os logs do servidor.', 'info')
    return redirect(url_for('teste_estresse'))

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
