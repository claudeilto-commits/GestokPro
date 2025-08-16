
# 📥 Como Baixar o Projeto e Subir no GitHub

Este guia explica como baixar todos os arquivos do projeto GestokPro do Replit e fazer upload para o GitHub.

## 📋 Índice

- [Método 1: Download Direto do Replit](#método-1-download-direto-do-replit)
- [Método 2: Usando Git Clone](#método-2-usando-git-clone)
- [Preparar Arquivos](#preparar-arquivos)
- [Criar Repositório no GitHub](#criar-repositório-no-github)
- [Upload para GitHub](#upload-para-github)
- [Configurar GitHub Pages](#configurar-github-pages)
- [Dicas Importantes](#dicas-importantes)

## 📦 Método 1: Download Direto do Replit

### Passo 1: Baixar ZIP do Replit

1. **No seu Replit, clique nos 3 pontinhos (⋯)** no painel lateral esquerdo
2. **Selecione "Download as ZIP"**
3. **Aguarde o download** do arquivo `repl-download.zip`
4. **Extraia o arquivo ZIP** em uma pasta no seu computador

### Passo 2: Verificar Conteúdo

Após extrair, você deve ter esta estrutura:

```
gestokpro/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   └── INSTALL.md
├── static/
│   └── css/
│       └── styles.css
├── stress_testing/
│   ├── advanced_stress_test.py
│   ├── run_stress_test.py
│   ├── test_menu.py
│   └── test_stress.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── produto_form.html
│   ├── produtos.html
│   └── teste_estresse.html
├── tests/
├── .gitignore
├── .replit
├── LICENSE
├── PROJECT_STRUCTURE.md
├── README.md
├── README.txt
├── GIT.md (este arquivo)
├── app.py
├── forms.py
├── init_db.py
├── main.py
├── models.py
├── pyproject.toml
├── replit.md
└── uv.lock
```

## 🔧 Método 2: Usando Git Clone

### Passo 1: No Terminal do Replit

```bash
# Verificar se o projeto tem Git inicializado
git status

# Se não tiver, inicializar
git init

# Adicionar todos os arquivos
git add .

# Fazer commit inicial
git commit -m "Initial commit: GestokPro v1.0"
```

### Passo 2: Clonar Localmente

```bash
# No seu computador (terminal/prompt)
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

## 🧹 Preparar Arquivos

### Arquivos que Devem Ser Removidos/Ignorados

Antes de fazer upload, verifique se estes arquivos estão no `.gitignore`:

```gitignore
# Arquivos específicos do Replit
.replit
replit.nix

# Banco de dados local
instance/
*.db
*.sqlite
*.sqlite3

# Ambiente Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Logs e relatórios
*.log
stress_test_report_*.md
advanced_stress_report_*.md

# Arquivos de configuração local
.env
.env.local
config.local.py

# Dependências
node_modules/
.npm

# Arquivos temporários
*.tmp
*.temp
.DS_Store
Thumbs.db
```

### Arquivos Importantes para Manter

✅ **Manter estes arquivos:**
- `README.md` - Documentação principal
- `README.txt` - Versão em texto da documentação
- `GIT.md` - Este guia
- `LICENSE` - Licença do projeto
- `app.py` - Aplicação principal
- `models.py` - Modelos de dados
- `forms.py` - Formulários
- `init_db.py` - Inicialização do banco
- `main.py` - Ponto de entrada WSGI
- `pyproject.toml` - Configuração do projeto
- `templates/` - Todos os templates HTML
- `static/` - Arquivos CSS e recursos
- `stress_testing/` - Scripts de teste
- `docs/` - Documentação técnica

## 🚀 Criar Repositório no GitHub

### Passo 1: No GitHub.com

1. **Acesse** [GitHub.com](https://github.com)
2. **Clique** em "New Repository" (botão verde)
3. **Preencha:**
   - Repository name: `gestokpro`
   - Description: `Sistema de Gestão de Estoque desenvolvido em Flask`
   - ✅ Public (recomendado)
   - ✅ Add a README file (desmarque, já temos)
   - ✅ Add .gitignore: Python
   - ✅ Choose a license: MIT
4. **Clique** em "Create repository"

### Passo 2: Copiar URL do Repositório

Após criar, copie a URL que aparece:
```
https://github.com/seu-usuario/gestokpro.git
```

## 📤 Upload para GitHub

### Método A: Interface Web do GitHub

1. **No repositório criado**, clique em "uploading an existing file"
2. **Arraste todos os arquivos** da pasta extraída
3. **Escreva commit message:** "Initial commit: GestokPro v1.0"
4. **Clique** em "Commit changes"

### Método B: Linha de Comando

```bash
# Navegar para a pasta do projeto
cd caminho/para/gestokpro

# Inicializar Git (se necessário)
git init

# Adicionar origin remoto
git remote add origin https://github.com/seu-usuario/gestokpro.git

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit: GestokPro v1.0"

# Fazer push para main
git branch -M main
git push -u origin main
```

### Método C: GitHub Desktop

1. **Abra o GitHub Desktop**
2. **File > Add Local Repository**
3. **Selecione** a pasta do projeto
4. **Publish Repository** no GitHub
5. **Sync** para enviar arquivos

## 🌐 Configurar GitHub Pages (Opcional)

Para hospedar a documentação:

1. **No repositório**, vá em "Settings"
2. **Role até "Pages"**
3. **Source:** Deploy from a branch
4. **Branch:** main
5. **Folder:** / (root)
6. **Save**

A documentação ficará disponível em:
`https://seu-usuario.github.io/gestokpro`

## 📝 Dicas Importantes

### ✅ Boas Práticas

1. **Sempre revisar** arquivos antes do upload
2. **Não incluir** dados sensíveis (senhas, tokens)
3. **Usar .gitignore** adequadamente
4. **Commit messages** descritivas
5. **README.md** sempre atualizado

### 🔒 Segurança

```bash
# Verificar se não há dados sensíveis
grep -r "password\|token\|secret\|key" .
grep -r "@" . | grep -v "README\|\.md"
```

### 📋 Checklist Final

Antes de fazer push, verifique:

- [ ] `.gitignore` configurado
- [ ] Sem arquivos de banco de dados
- [ ] Sem credenciais no código
- [ ] README.md atualizado
- [ ] LICENSE incluído
- [ ] Dependências documentadas
- [ ] Instruções de instalação claras

### 🔄 Atualizações Futuras

Para sincronizar mudanças do Replit:

```bash
# No diretório local
git pull origin main

# Baixar novo ZIP do Replit
# Substituir arquivos alterados
# Adicionar mudanças

git add .
git commit -m "Update: descrição das mudanças"
git push origin main
```

### 📞 Suporte

Se encontrar problemas:

1. **Verifique** se o Git está instalado
2. **Confirme** credenciais do GitHub
3. **Revise** mensagens de erro
4. **Consulte** documentação do GitHub

### 📚 Links Úteis

- [GitHub Docs](https://docs.github.com)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [GitHub Desktop](https://desktop.github.com)
- [Configurar SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

**Seguindo este guia, você terá todo o projeto GestokPro disponível no GitHub de forma organizada e profissional! 🚀**
