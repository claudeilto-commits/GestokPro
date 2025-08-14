
# GestokPro - Sistema de Gestão de Estoque

GestokPro é um sistema completo de gestão de estoque desenvolvido em Flask, projetado para pequenas e médias empresas. O sistema oferece uma interface web moderna para gerenciar catálogos de produtos, controlar níveis de estoque e monitorar métricas de inventário.

## ÍNDICE

- Características
- Pré-requisitos
- Instalação Local
- Estrutura do Projeto
- Entidades do Sistema
- Funcionalidades
- Sistema de Testes de Performance
- Como Usar
- Deploy no GitHub
- API Endpoints
- Contribuição

## CARACTERÍSTICAS

- Interface Web Moderna: Interface responsiva com Tailwind CSS
- Autenticação de Usuários: Sistema seguro com Flask-Login
- CRUD de Produtos: Criação, leitura, atualização e exclusão de produtos
- Gestão de Estoque: Controle de quantidades e status de produtos
- Dashboard Analytics: Métricas em tempo real do inventário
- Sistema de Performance: Monitoramento completo de performance
- Testes de Estresse: Sistema avançado de testes automatizados
- Relatórios Automáticos: Geração de relatórios detalhados
- Localização: Sistema totalmente em português brasileiro

## PRÉ-REQUISITOS

Software Necessário:
- Python 3.8+ - Linguagem de programação principal
- PostgreSQL 13+ - Banco de dados de produção
- Git - Para controle de versão
- Navegador Web Moderno - Para interface do usuário

Dependências Python:
flask>=2.0.0          # Framework web principal
flask-sqlalchemy      # ORM para banco de dados
flask-login           # Sistema de autenticação
flask-wtf             # Formulários e CSRF protection
wtforms               # Validação de formulários
werkzeug              # Utilitários WSGI e segurança
psycopg2-binary       # Driver PostgreSQL
gunicorn              # Servidor WSGI para produção
aiohttp               # Cliente HTTP para testes

## INSTALAÇÃO LOCAL

1. Clone o Repositório:
git clone https://github.com/seu-usuario/gestokpro.git
cd gestokpro

2. Criar Ambiente Virtual:
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

3. Instalar Dependências:
pip install -r requirements.txt

4. Configurar Banco de Dados:
# Instalar PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Criar banco de dados
sudo -u postgres createdb gestokpro

5. Configurar Variáveis de Ambiente:
Crie um arquivo .env:
DATABASE_URL=postgresql://usuario:senha@localhost/gestokpro
SESSION_SECRET=sua-chave-secreta-super-segura

6. Inicializar Banco de Dados:
python init_db.py

7. Executar Aplicação:
# Desenvolvimento
python app.py

# Produção
gunicorn --bind 0.0.0.0:5000 main:app

Acesse: http://localhost:5000

Login padrão:
- Email: admin@gestokpro.com
- Senha: admin

## ESTRUTURA DO PROJETO

gestokpro/
├── Documentação
│   ├── README.md                   # Documentação principal
│   ├── PROJECT_STRUCTURE.md       # Estrutura do projeto
│   ├── LICENSE                     # Licença MIT
│   └── .gitignore                  # Arquivos ignorados pelo Git
├──
├── Aplicação Principal
│   ├── app.py                      # Aplicação Flask principal
│   ├── main.py                     # Ponto de entrada WSGI
│   ├── models.py                   # Modelos de dados SQLAlchemy
│   ├── forms.py                    # Formulários WTForms
│   ├── init_db.py                  # Script de inicialização do BD
│   └── replit.md                   # Arquitetura e preferências
├──
├── Templates e Interface
│   ├── templates/                  # Templates Jinja2
│   │   ├── base.html               # Template base
│   │   ├── login.html              # Página de login
│   │   ├── dashboard.html          # Dashboard principal
│   │   ├── produtos.html           # Listagem de produtos
│   │   ├── produto_form.html       # Formulário de produtos
│   │   └── teste_estresse.html     # Interface de testes
│   └── static/                     # Arquivos estáticos
│       └── css/                    # Estilos customizados
├──
├── Sistema de Testes
│   ├── stress_testing/             # Testes de performance
│   │   ├── test_stress.py          # Teste básico
│   │   ├── advanced_stress_test.py # Teste avançado
│   │   ├── run_stress_test.py      # Teste rápido
│   │   └── test_menu.py            # Menu interativo
│   └── tests/                      # Testes unitários (futuro)
├──
├── Documentação Técnica
│   └── docs/                       
│       ├── ARCHITECTURE.md         # Arquitetura do sistema
│       ├── CONTRIBUTING.md         # Guia de contribuição
│       └── INSTALL.md              # Guia de instalação
├──
├── Configuração
│   ├── pyproject.toml              # Configuração Python/UV
│   ├── uv.lock                     # Lock de dependências
│   └── .replit                     # Configuração Replit
└──
└── Dados da Aplicação
    ├── instance/                   # Dados Flask
    ├── stress_test_report_*.md     # Relatórios básicos (gerados)
    └── advanced_stress_report_*.md # Relatórios avançados (gerados)

## ENTIDADES DO SISTEMA

USUARIO (Usuário):
Entidade responsável pelo gerenciamento de contas de usuários.

Campos:
- id: Identificador único (Primary Key)
- email: Email do usuário (único, obrigatório)
- senha_hash: Senha criptografada com Werkzeug
- admin: Flag para permissões administrativas
- data_criacao: Timestamp de criação da conta

Métodos:
- verificar_senha(senha): Valida senha fornecida
- is_admin(): Verifica se usuário é administrador

PRODUTO (Produto):
Entidade central para gestão do catálogo de produtos.

Campos:
- id: Identificador único (Primary Key)
- sku: Código único do produto (obrigatório)
- nome: Nome do produto (obrigatório)
- descricao: Descrição detalhada
- quantidade: Estoque atual
- preco_custo: Custo de aquisição
- preco_venda: Preço de venda
- categoria: Categoria do produto
- data_criacao: Data de cadastro
- data_atualizacao: Última modificação

Métodos de Negócio:
- get_status_estoque(): Retorna status baseado na quantidade
  - "Crítico" (< 10 unidades)
  - "Baixo" (10-50 unidades)  
  - "Normal" (> 50 unidades)
- calcular_margem(): Calcula margem de lucro
- valor_total_estoque(): Valor total em estoque

## FUNCIONALIDADES

Sistema de Autenticação:
- Login/Logout: Sessões seguras com Flask-Login
- Proteção de Rotas: Decorators para páginas protegidas
- Gerenciamento de Sessão: Controle automático de expiração
- Segurança: Hashing de senhas com Werkzeug

Dashboard Principal:
- Métricas em Tempo Real:
  - Total de produtos cadastrados
  - Valor total do estoque
  - Produtos com estoque baixo
  - Produtos críticos (< 10 unidades)
- Gráficos e Estatísticas: Visualização interativa dos dados
- Alertas: Notificações de produtos com estoque baixo

Gestão de Produtos:
- CRUD Completo:
  - Create: Cadastro de novos produtos
  - Read: Listagem e visualização detalhada
  - Update: Edição de informações
  - Delete: Remoção de produtos
- Validações: Campos obrigatórios e formatos
- Busca e Filtros: Localização rápida de produtos
- Paginação: Navegação eficiente em grandes listas

## SISTEMA DE TESTES DE PERFORMANCE

O GestokPro inclui um sistema completo de testes de estresse e monitoramento de performance.

Scripts de Teste:

test_stress.py - Teste Básico:
- Duração: 30 segundos
- Usuários: 2 por onda
- Endpoints Testados: Login, Dashboard, Produtos
- Métricas: Tempo de resposta, taxa de sucesso

advanced_stress_test.py - Teste Avançado:
- Duração: 45-60 segundos
- Usuários: Padrões variados (normal, pesado, rápido)
- Análise Detalhada: Percentis, detecção de anomalias
- Relatórios: Markdown com gráficos e recomendações

run_stress_test.py - Teste Rápido:
- Propósito: Execução rápida para validação
- Saída: Resumo direto no terminal

test_menu.py - Menu Interativo:
- Interface: Menu de linha de comando
- Opções: Diferentes tipos de teste
- Personalização: Configuração de parâmetros

Interface Web de Testes:
Acesse /teste-estresse para:
- Executar Testes: Botão direto para iniciar
- Ver Histórico: Lista de todos os testes realizados
- Métricas: Dashboard com estatísticas
- Relatórios: Visualização detalhada dos resultados

Métricas Coletadas:
- Tempo de Resposta: Médio, mediana, percentis (P90, P95, P99)
- Taxa de Sucesso: Porcentagem de requests bem-sucedidos
- Throughput: Requests por minuto
- Performance por Endpoint: Análise individual de cada rota
- Detecção de Anomalias: Identificação automática de problemas

## COMO USAR

1. Primeiro Acesso:
1. Acesse http://localhost:5000
2. Faça login com as credenciais padrão
3. Altere a senha do administrador
4. Explore o dashboard principal

2. Cadastrar Produtos:
1. Navegue para "Produtos" no menu
2. Clique em "Novo Produto"
3. Preencha os campos obrigatórios:
   - SKU (código único)
   - Nome do produto
   - Quantidade inicial
   - Preços de custo e venda
4. Salve o produto

3. Gerenciar Estoque:
1. Na lista de produtos, visualize o status atual
2. Use os filtros para encontrar produtos específicos
3. Edite produtos para atualizar quantidades
4. Monitor alertas de estoque baixo no dashboard

4. Executar Testes de Performance:
1. Acesse a aba "Performance"
2. Visualize o histórico de testes anteriores
3. Clique em "Executar Teste" para novo teste
4. Aguarde a conclusão e analise os resultados

5. Monitorar Performance:
- Observe o tempo de resposta no rodapé das páginas
- Use os relatórios para identificar gargalos
- Configure alertas para performance crítica

## DEPLOY NO GITHUB

1. Preparar Repositório:
# Inicializar Git (se não existir)
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "Initial commit: GestokPro v1.0"

# Conectar ao GitHub
git remote add origin https://github.com/seu-usuario/gestokpro.git
git branch -M main
git push -u origin main

2. Configurar GitHub Actions (CI/CD):
Crie .github/workflows/deploy.yml

3. Configurar Secrets:
No GitHub, vá em Settings > Secrets e adicione:
- DATABASE_URL: URL do banco de produção
- SESSION_SECRET: Chave secreta da sessão

## API ENDPOINTS

Autenticação:
- GET / - Página inicial (redireciona para dashboard se logado)
- GET /login - Página de login
- POST /login - Processar login
- GET /logout - Fazer logout

Dashboard:
- GET /dashboard - Dashboard principal com métricas

Produtos:
- GET /produtos - Lista todos os produtos
- GET /produtos/novo - Formulário de novo produto
- POST /produtos/novo - Criar novo produto
- GET /produtos/<id>/editar - Formulário de edição
- POST /produtos/<id>/editar - Atualizar produto
- POST /produtos/<id>/deletar - Deletar produto

Testes de Performance:
- GET /teste-estresse - Interface web de testes
- POST /executar-teste - Executar novo teste de estresse

Monitoramento:
- Todas as rotas incluem monitoramento automático de tempo de resposta
- Métricas exibidas no rodapé das páginas

## CONTRIBUIÇÃO

Como Contribuir:
1. Fork o repositório
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature)
3. Commit suas mudanças (git commit -am 'Add nova feature')
4. Push para a branch (git push origin feature/nova-feature)
5. Abra um Pull Request

Padrões de Código:
- Python: Siga PEP 8
- HTML/CSS: Indentação de 2 espaços
- JavaScript: Use ES6+
- Commits: Use Conventional Commits

Testes:
Execute os testes antes de abrir PR:
# Testes unitários
python -m pytest tests/

# Testes de integração
python -m pytest tests/integration/

# Testes de stress
python run_stress_test.py

## LICENÇA

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## SUPORTE

- Documentação: Este README.md
- Issues: Use o GitHub Issues para reportar bugs
- Discussões: GitHub Discussions para dúvidas
- Email: contato@gestokpro.com

GestokPro - Sistema de Gestão de Estoque Inteligente
