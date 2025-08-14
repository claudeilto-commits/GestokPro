# 🤝 Guia de Contribuição - GestokPro

Obrigado por seu interesse em contribuir com o GestokPro! Este guia vai te ajudar a começar.

## 📋 Como Contribuir

### 1. Preparação
```bash
# Fork o repositório no GitHub
# Clone seu fork
git clone https://github.com/seu-usuario/gestokpro.git
cd gestokpro

# Adicione o repositório original como upstream
git remote add upstream https://github.com/autor-original/gestokpro.git
```

### 2. Configuração do Ambiente
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Instalar dependências de desenvolvimento
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 pre-commit

# Instalar hooks pre-commit
pre-commit install
```

### 3. Criação de Feature
```bash
# Criar nova branch
git checkout -b feature/nova-funcionalidade

# Fazer suas modificações
# ... código ...

# Testar suas mudanças
python -m pytest tests/
python run_stress_test.py

# Commit com mensagem descritiva
git add .
git commit -m "feat: adiciona funcionalidade X"

# Push para seu fork
git push origin feature/nova-funcionalidade
```

### 4. Pull Request
1. Abra um Pull Request no GitHub
2. Descreva as mudanças claramente
3. Referencie issues relacionadas
4. Aguarde review e feedback

## 🎯 Tipos de Contribuição

### 🐛 Correção de Bugs
- Reporte bugs via GitHub Issues
- Inclua passos para reproduzir
- Descreva comportamento esperado vs atual
- Adicione capturas de tela se relevante

### ✨ Novas Funcionalidades
- Discuta a ideia primeiro em uma Issue
- Implemente seguindo os padrões existentes
- Adicione testes para nova funcionalidade
- Atualize documentação se necessário

### 📚 Documentação
- Melhore README.md
- Adicione comentários no código
- Crie tutoriais e guias
- Traduza documentação

### 🧪 Testes
- Adicione testes unitários
- Melhore cobertura de testes
- Crie testes de integração
- Otimize testes de performance

## 📝 Padrões de Código

### Python (PEP 8)
```python
# Bom ✅
def calcular_estoque_total(produtos):
    """Calcula o valor total do estoque."""
    total = 0
    for produto in produtos:
        total += produto.quantidade * produto.preco_custo
    return total

# Evitar ❌
def calc_estoque(prods):
    t=0
    for p in prods:t+=p.qtd*p.preco
    return t
```

### HTML/Jinja2
```html
<!-- Bom ✅ -->
<div class="product-card">
  <h3 class="product-title">{{ produto.nome }}</h3>
  <p class="product-price">R$ {{ produto.preco_venda }}</p>
</div>

<!-- Evitar ❌ -->
<div class="pc"><h3>{{produto.nome}}</h3><p>R${{produto.preco_venda}}</p></div>
```

### Mensagens de Commit
Use Conventional Commits:
```bash
feat: adiciona filtro de produtos por categoria
fix: corrige cálculo de margem de lucro
docs: atualiza README com instruções de deploy
test: adiciona testes para modelo Usuario
refactor: reorganiza estrutura de templates
style: aplica formatação PEP 8
```

## 🧪 Executando Testes

### Testes Básicos
```bash
# Todos os testes
python -m pytest

# Com cobertura
python -m pytest --cov=. --cov-report=html

# Testes específicos
python -m pytest tests/test_models.py
python -m pytest tests/test_routes.py -v
```

### Testes de Performance
```bash
# Teste rápido
python run_stress_test.py

# Teste completo
python advanced_stress_test.py

# Menu interativo
python test_menu.py
```

### Linting e Formatação
```bash
# Verificar estilo
flake8 .

# Formatar código
black .

# Verificar imports
isort . --check-only
```

## 🏗️ Estrutura de Desenvolvimento

### Adicionando Nova Rota
1. **Definir rota em `app.py`**:
```python
@app.route('/nova-rota')
@login_required
def nova_funcionalidade():
    return render_template('nova_template.html')
```

2. **Criar template em `templates/`**:
```html
{% extends "base.html" %}
{% block title %}Nova Funcionalidade{% endblock %}
{% block content %}
<!-- Conteúdo aqui -->
{% endblock %}
```

3. **Adicionar ao menu** em `base.html`
4. **Criar testes** em `tests/`
5. **Atualizar documentação**

### Adicionando Nova Entidade
1. **Definir modelo em `models.py`**:
```python
class NovaEntidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    # ... outros campos
```

2. **Criar formulário em `forms.py`**:
```python
class NovaEntidadeForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    # ... outros campos
    submit = SubmitField('Salvar')
```

3. **Implementar CRUD completo**
4. **Criar testes de modelo**
5. **Atualizar init_db.py se necessário**

## 📊 Monitoramento e Debugging

### Logs de Desenvolvimento
```python
import logging

# Configurar logging detalhado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Usar em suas funções
logger = logging.getLogger(__name__)
logger.debug(f"Processando produto: {produto.nome}")
```

### Profile de Performance
```python
from werkzeug.middleware.profiler import ProfilerMiddleware

# Adicionar ao app em desenvolvimento
if app.debug:
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app)
```

## 🚀 Deploy e Testes

### Testando Deploy Local
```bash
# Produção local com Gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 main:app

# Testar todos os endpoints
curl http://localhost:5000/
curl http://localhost:5000/dashboard
curl http://localhost:5000/produtos
```

### Preparando para Deploy
1. ✅ Todos os testes passando
2. ✅ Cobertura de testes > 80%
3. ✅ Linting sem erros
4. ✅ Performance satisfatória
5. ✅ Documentação atualizada

## 🔍 Checklist de Pull Request

Antes de enviar PR, verifique:

- [ ] Código segue padrões do projeto
- [ ] Testes adicionados e passando
- [ ] Documentação atualizada
- [ ] Commits seguem Conventional Commits
- [ ] Branch atualizada com main
- [ ] PR tem descrição clara
- [ ] Issues relacionadas linkadas

## 📞 Ajuda e Suporte

### Canais de Comunicação
- **Issues**: Para bugs e feature requests
- **Discussions**: Para dúvidas e ideias
- **Email**: contato@gestokpro.com

### Mentoria para Novos Contribuidores
- Marque issues como `good first issue`
- Peça ajuda em issues complexas
- Participe das discussions
- Contribua com documentação primeiro

### Recursos Úteis
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Python PEP 8](https://pep8.org/)

---

**🙏 Obrigado por contribuir com o GestokPro!**

Sua contribuição ajuda a tornar o sistema melhor para todos os usuários.