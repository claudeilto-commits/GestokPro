# 🏗️ Arquitetura do Sistema - GestokPro

## 📊 Visão Geral da Arquitetura

O GestokPro é construído com uma arquitetura monolítica moderna, otimizada para simplicidade e performance, seguindo os princípios de separação de responsabilidades e escalabilidade horizontal.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   Database      │
│                 │    │                 │    │                 │
│ • Tailwind CSS  │◄──►│ • Flask 2.3+    │◄──►│ • PostgreSQL    │
│ • Jinja2        │    │ • SQLAlchemy    │    │ • Connection    │
│ • Font Awesome  │    │ • Flask-Login   │    │   Pooling       │
│ • Responsive    │    │ • WTForms       │    │ • ACID          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🎯 Princípios Arquiteturais

### 1. **Simplicidade em Primeiro Lugar**
- Monólito bem estruturado vs microserviços desnecessários
- Stack única (Python) reduz complexidade
- Configuração mínima para deploy rápido

### 2. **Separação de Responsabilidades**
```
app.py      → Controle de rotas e lógica de aplicação
models.py   → Modelos de dados e regras de negócio  
forms.py    → Validação e processamento de formulários
templates/  → Apresentação e interface do usuário
```

### 3. **Performance por Design**
- Connection pooling no banco
- Middleware de monitoramento integrado
- Sistema de testes de stress automatizado
- Queries otimizadas com SQLAlchemy

### 4. **Segurança Integrada**
- Autenticação com Flask-Login
- Proteção CSRF em todos os formulários
- Hash seguro de senhas com Werkzeug
- Validação de entrada em todas as rotas

## 🔧 Componentes Principais

### **Camada de Apresentação (Frontend)**

**Tecnologias:**
- Jinja2 para templating server-side
- Tailwind CSS para styling responsivo
- Font Awesome para iconografia consistente

**Responsabilidades:**
- Renderização de templates dinâmicos
- Formulários interativos com validação
- Interface responsiva para mobile/desktop
- Feedback visual de operações

### **Camada de Aplicação (Backend)**

**Estrutura MVC Simplificada:**
```python
# Modelo (models.py)
class Produto(db.Model):
    # Entidades de negócio
    # Validações de domínio
    # Métodos de cálculo

# Visão (templates/)
# Templates Jinja2 com lógica de apresentação

# Controlador (app.py)
@app.route('/produtos')
def listar_produtos():
    # Lógica de controle
    # Orquestração de serviços
    # Renderização de resposta
```

**Módulos Especializados:**
- `forms.py`: Validação e processamento de entrada
- `init_db.py`: Migração e seed de dados
- Testes de performance: Sistema completo de monitoramento

### **Camada de Dados (Database)**

**Modelo Relacional:**
```sql
usuarios
├── id (PK)
├── email (UNIQUE)
├── senha_hash
├── admin (BOOLEAN)
└── data_criacao

produtos
├── id (PK)
├── sku (UNIQUE)
├── nome
├── descricao
├── quantidade
├── preco_custo
├── preco_venda
├── categoria
├── data_criacao
└── data_atualizacao
```

**Características:**
- PostgreSQL para ACID e escalabilidade
- Connection pooling para performance
- Índices otimizados para consultas frequentes
- Constraints de integridade referencial

## ⚡ Fluxo de Dados

### **Fluxo de Requisição Típico:**

```
1. Requisição HTTP → Flask Router
2. Middleware de Timing → Captura métricas
3. Autenticação → Flask-Login validation
4. Validação → WTForms processing
5. Modelo → SQLAlchemy ORM
6. Banco → PostgreSQL query
7. Resposta → Jinja2 template
8. Frontend → Tailwind CSS styling
```

### **Exemplo: Cadastro de Produto**

```python
# 1. Rota recebe requisição
@app.route('/produtos/novo', methods=['GET', 'POST'])
@login_required
def novo_produto():
    # 2. Instancia formulário
    form = ProdutoForm()
    
    # 3. Validação de dados
    if form.validate_on_submit():
        # 4. Criar modelo
        produto = Produto(
            sku=form.sku.data,
            nome=form.nome.data,
            # ... outros campos
        )
        
        # 5. Persistir no banco
        db.session.add(produto)
        db.session.commit()
        
        # 6. Resposta de sucesso
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('produtos'))
    
    # 7. Renderizar template
    return render_template('produto_form.html', form=form)
```

## 🧪 Sistema de Performance

### **Arquitetura de Monitoramento**

```
┌─────────────────┐
│  Web Interface  │ ← Interface visual para testes
├─────────────────┤
│  Test Scripts   │ ← Múltiplos tipos de teste
├─────────────────┤
│  Async Engine   │ ← aiohttp para concorrência
├─────────────────┤
│  Metrics Collector │ ← Coleta de métricas
├─────────────────┤
│  Report Generator │ ← Análise e relatórios
└─────────────────┘
```

### **Tipos de Teste Implementados:**

1. **Teste Básico (30s)**: Validação rápida
2. **Teste Avançado (45s)**: Análise detalhada com percentis
3. **Teste Intensivo (60-90s)**: Stress test completo
4. **Teste Personalizado**: Via menu interativo

### **Métricas Coletadas:**

- **Performance**: Tempo médio, mediana, P90, P95, P99
- **Disponibilidade**: Taxa de sucesso, falhas
- **Capacidade**: Throughput, requests/minuto
- **Qualidade**: Detecção de anomalias, padrões

## 🔒 Segurança

### **Camadas de Segurança:**

1. **Autenticação**: Flask-Login com sessões seguras
2. **Autorização**: Decorators `@login_required`
3. **Validação**: WTForms com sanitização
4. **CSRF**: Proteção automática em formulários
5. **Senhas**: Hash com salt usando Werkzeug
6. **Headers**: ProxyFix para HTTPS correto

### **Práticas de Segurança:**

```python
# Hash seguro de senhas
senha_hash = generate_password_hash(senha)

# Validação de entrada
class ProdutoForm(FlaskForm):
    sku = StringField('SKU', validators=[
        DataRequired(),
        Length(min=3, max=20)
    ])

# Proteção de rota
@app.route('/admin')
@login_required
def admin_only():
    if not current_user.admin:
        abort(403)
```

## 📈 Escalabilidade

### **Estratégias Implementadas:**

1. **Database Connection Pooling**
```python
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
```

2. **Template Caching**: Jinja2 otimizado
3. **Static File Serving**: CDN-ready
4. **Lazy Loading**: Paginação em listas grandes

### **Pontos de Escala Horizontal:**

- **Web Layer**: Múltiplas instâncias Flask
- **Database**: Read replicas, sharding
- **Static Assets**: CDN distribution
- **Session Store**: Redis/Memcached

## 🚀 Deploy e DevOps

### **Ambientes Suportados:**

1. **Desenvolvimento**: SQLite + Flask dev server
2. **Staging**: PostgreSQL + Gunicorn
3. **Produção**: PostgreSQL + Gunicorn + Nginx

### **Pipeline de Deploy:**

```yaml
# GitHub Actions
Build → Test → Security Scan → Deploy
  ↓       ↓         ↓           ↓
Docker  Pytest   Bandit    Replit/Heroku
```

### **Monitoramento em Produção:**

- **Health Checks**: `/health` endpoint
- **Metrics**: Tempo de resposta em tempo real
- **Logs**: Structured logging com níveis
- **Alerts**: Performance degradation detection

## 📊 Métricas e KPIs

### **Performance KPIs:**

- **Tempo de Resposta**: < 500ms para 95% das requests
- **Disponibilidade**: > 99.5% uptime
- **Throughput**: > 100 requests/segundo
- **Error Rate**: < 0.1% de falhas

### **Métricas de Negócio:**

- Produtos cadastrados
- Operações de estoque
- Usuários ativos
- Taxa de utilização de funcionalidades

### **Dashboard de Monitoramento:**

O sistema inclui dashboard em tempo real com:
- Métricas de performance no rodapé
- Alertas de estoque baixo
- Estatísticas de uso do sistema
- Histórico de testes de performance

---

## 🔮 Roadmap Técnico

### **Versão 2.0 (Futuro):**
- API REST completa
- Sistema de relatórios avançados
- Integração com sistemas externos
- Mobile app com React Native
- Machine learning para previsão de estoque

### **Melhorias Contínuas:**
- Otimização de queries
- Cache distribuído
- Testes automatizados expandidos
- Documentação interativa
- Observabilidade avançada

---

**Esta arquitetura foi projetada para crescer com seu negócio, mantendo simplicidade e performance.**