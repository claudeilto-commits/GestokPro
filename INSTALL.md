# 🚀 Guia de Instalação Rápida - GestokPro

## 📋 Instalação em 5 Minutos

### Pré-requisitos
- Python 3.8+
- PostgreSQL 13+
- Git

### 1. Clone e Configure

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gestokpro.git
cd gestokpro

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install flask flask-sqlalchemy flask-login flask-wtf wtforms
pip install werkzeug psycopg2-binary gunicorn aiohttp email-validator
```

### 2. Configurar Banco de Dados

```bash
# PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql

# Criar banco
sudo -u postgres createdb gestokpro

# Configurar variáveis (criar arquivo .env)
echo "DATABASE_URL=postgresql://postgres:senha@localhost/gestokpro" > .env
echo "SESSION_SECRET=minha-chave-super-secreta-123" >> .env
```

### 3. Inicializar e Executar

```bash
# Inicializar banco de dados
python init_db.py

# Executar aplicação
python app.py
```

### 4. Acessar Sistema

- URL: `http://localhost:5000`
- Login: `admin@gestokpro.com`
- Senha: `admin`

## 🔧 Configuração Detalhada

### Variáveis de Ambiente

Crie arquivo `.env` na raiz do projeto:

```env
# Banco de Dados
DATABASE_URL=postgresql://usuario:senha@localhost:5432/gestokpro

# Segurança
SESSION_SECRET=sua-chave-secreta-super-complexa

# Opcional: Configurações de desenvolvimento
FLASK_ENV=development
FLASK_DEBUG=1
```

### PostgreSQL - Configuração Completa

```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Acessar console PostgreSQL
sudo -u postgres psql

# Criar usuário e banco
CREATE USER gestokpro_user WITH PASSWORD 'senha_forte';
CREATE DATABASE gestokpro OWNER gestokpro_user;
GRANT ALL PRIVILEGES ON DATABASE gestokpro TO gestokpro_user;
\q
```

### Estrutura de Pastas Necessárias

```
gestokpro/
├── instance/          # Criada automaticamente
├── static/           # Arquivos estáticos (opcional)
├── templates/        # Templates HTML
└── reports/          # Relatórios de teste (criada automaticamente)
```

## 🐳 Docker (Opcional)

### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://gestokpro:password@db:5432/gestokpro
      - SESSION_SECRET=your-secret-key
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=gestokpro
      - POSTGRES_USER=gestokpro
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

Executar com Docker:
```bash
docker-compose up -d
```

## ⚡ Deploy Rápido

### Replit
1. Importe repositório do GitHub
2. Configure variáveis de ambiente no Secrets
3. Execute `python init_db.py`
4. Clique em "Run"

### Heroku
```bash
heroku create gestokpro-app
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python init_db.py
```

### Railway
1. Conecte repositório GitHub
2. Adicione PostgreSQL
3. Configure variáveis de ambiente
4. Deploy automático

## 🧪 Validar Instalação

### 1. Executar Teste Básico
```bash
python run_stress_test.py
```

### 2. Verificar Endpoints
- Dashboard: `http://localhost:5000/dashboard`
- Produtos: `http://localhost:5000/produtos`
- Performance: `http://localhost:5000/teste-estresse`

### 3. Logs de Debug
Verificar logs no terminal para confirmar:
- ✅ Conexão com banco de dados
- ✅ Criação de tabelas
- ✅ Login de usuário
- ✅ Carregamento de produtos

## 🔍 Solução de Problemas

### Erro de Banco de Dados
```bash
# Verificar se PostgreSQL está rodando
sudo systemctl status postgresql

# Reiniciar se necessário
sudo systemctl restart postgresql

# Testar conexão
psql -U gestokpro_user -d gestokpro -h localhost
```

### Erro de Dependências
```bash
# Atualizar pip
pip install --upgrade pip

# Reinstalar dependências
pip uninstall flask flask-sqlalchemy flask-login
pip install flask flask-sqlalchemy flask-login
```

### Erro de Permissões
```bash
# Linux: dar permissão aos scripts
chmod +x *.py

# Windows: executar como administrador
```

### Porta Ocupada
```bash
# Verificar processos na porta 5000
lsof -i :5000

# Matar processo se necessário
kill -9 PID
```

## 📞 Ajuda

Se encontrar problemas:

1. ✅ Verifique se todos os pré-requisitos estão instalados
2. ✅ Confirme se o PostgreSQL está rodando
3. ✅ Valide as variáveis de ambiente
4. ✅ Execute `python init_db.py` novamente
5. ✅ Consulte os logs de erro no terminal

---

**🎉 Instalação concluída! O GestokPro está pronto para uso.**