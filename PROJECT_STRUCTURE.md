# 📁 Estrutura do Projeto GestokPro

## 🗂️ Organização de Arquivos

```
gestokpro/
├── 📚 Documentação Principal
│   ├── README.md                    # Documentação completa do projeto
│   ├── LICENSE                      # Licença MIT
│   ├── .gitignore                   # Arquivos ignorados pelo Git
│   └── PROJECT_STRUCTURE.md         # Este arquivo
│
├── 🏗️ Aplicação Principal
│   ├── main.py                      # Ponto de entrada WSGI
│   ├── app.py                       # Aplicação Flask principal
│   ├── models.py                    # Modelos SQLAlchemy
│   ├── forms.py                     # Formulários WTForms
│   └── init_db.py                   # Script de inicialização do BD
│
├── 📄 Templates HTML
│   ├── templates/
│   │   ├── base.html                # Template base
│   │   ├── login.html               # Página de login
│   │   ├── dashboard.html           # Dashboard principal
│   │   ├── produtos.html            # Lista de produtos
│   │   ├── produto_form.html        # Formulário de produtos
│   │   └── teste_estresse.html      # Interface de testes
│
├── 📦 Arquivos Estáticos
│   └── static/
│       └── css/                     # Estilos customizados
│
├── 🧪 Sistema de Testes de Performance
│   └── stress_testing/
│       ├── test_stress.py           # Teste básico de estresse
│       ├── advanced_stress_test.py  # Teste avançado com análise
│       ├── run_stress_test.py       # Execução rápida de teste
│       └── test_menu.py             # Menu interativo
│
├── 🧪 Testes Unitários (futuro)
│   └── tests/
│       ├── test_models.py           # Testes dos modelos
│       ├── test_routes.py           # Testes das rotas
│       └── test_forms.py            # Testes dos formulários
│
├── 📖 Documentação Técnica
│   └── docs/
│       ├── ARCHITECTURE.md          # Arquitetura do sistema
│       ├── CONTRIBUTING.md          # Guia de contribuição
│       └── INSTALL.md               # Guia de instalação
│
├── ⚙️ Configuração
│   ├── pyproject.toml               # Configuração Python/UV
│   ├── uv.lock                      # Lock de dependências
│   ├── .replit                      # Configuração Replit
│   └── replit.md                    # Preferências e arquitetura
│
├── 📊 Dados e Instâncias
│   └── instance/                    # Dados da aplicação Flask
│
└── 📈 Relatórios de Teste (gerados automaticamente)
    ├── stress_test_report_*.md      # Relatórios básicos
    └── advanced_stress_report_*.md  # Relatórios avançados
```

## 🎯 Descrição das Pastas

### **📚 Documentação Principal (Raiz)**
- Documentação essencial que deve ficar visível na raiz
- README principal com overview completo
- Licença e configurações básicas

### **🏗️ Aplicação Principal (Raiz)**
- Core da aplicação Flask
- Modelos, rotas, formulários
- Script de inicialização do banco

### **📄 Templates HTML**
- Todos os templates Jinja2 organizados
- Estrutura hierárquica clara
- Fácil manutenção e localização

### **🧪 Sistema de Testes** 
**`stress_testing/`**
- Scripts especializados em testes de performance
- Diferentes tipos de teste (básico, avançado, intensivo)
- Menu interativo para execução
- Análise detalhada de métricas

### **🧪 Testes Unitários**
**`tests/`** (pasta preparada para futuras implementações)
- Testes automatizados da aplicação
- Cobertura de modelos, rotas e formulários
- Integração com CI/CD

### **📖 Documentação Técnica**
**`docs/`**
- Documentação detalhada e técnica
- Guias de instalação e contribuição
- Arquitetura e decisões técnicas

### **📦 Arquivos Estáticos**
**`static/`**
- CSS customizado
- JavaScript (futuro)
- Imagens e assets

### **📊 Dados da Aplicação**
**`instance/`**
- Banco de dados SQLite (desenvolvimento)
- Configurações específicas da instância
- Dados sensíveis (não versionados)

## 🔄 Fluxo de Desenvolvimento

### **Estrutura de Trabalho:**

1. **Desenvolvimento Principal**: Editar arquivos na raiz
2. **Testes de Performance**: Usar scripts em `stress_testing/`
3. **Documentação**: Atualizar arquivos em `docs/`
4. **Interface**: Modificar templates em `templates/`

### **Comandos Principais:**

```bash
# Executar aplicação
python app.py

# Inicializar banco
python init_db.py

# Testes de performance
python stress_testing/run_stress_test.py
python stress_testing/test_menu.py

# Navegar documentação
ls docs/
cat docs/ARCHITECTURE.md
```

## 📝 Vantagens da Organização

### ✅ **Benefícios**
- **Clareza**: Fácil localização de arquivos
- **Manutenção**: Estrutura lógica e intuitiva  
- **Escalabilidade**: Pronto para crescimento
- **Colaboração**: Padrão familiar para desenvolvedores
- **Deploy**: Separação clara de código e documentação

### 🎯 **Padrões Seguidos**
- **Separação de Responsabilidades**: Cada pasta tem propósito específico
- **Convenções Python**: Estrutura familiar para desenvolvedores Python
- **Boas Práticas Flask**: Organização recomendada pela comunidade
- **Documentação Acessível**: README na raiz, detalhes em docs/

## 🚀 Como Usar Esta Estrutura

### **Para Desenvolvedores:**
1. Leia `README.md` primeiro
2. Configure seguindo `docs/INSTALL.md`
3. Entenda arquitetura em `docs/ARCHITECTURE.md`  
4. Contribua seguindo `docs/CONTRIBUTING.md`

### **Para Usuários:**
1. Execute `python app.py` para rodar o sistema
2. Use interface web para gestão de estoque
3. Acesse `/teste-estresse` para monitoramento
4. Consulte relatórios gerados automaticamente

### **Para Deploy:**
- Arquivos necessários estão na raiz
- Configurações em `.replit` e `pyproject.toml`
- Documentação completa disponível
- Testes automatizados prontos para CI/CD

---

**Esta organização foi projetada para facilitar desenvolvimento, manutenção e colaboração no projeto GestokPro.**