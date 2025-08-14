# Sistema de Teste de Estresse - GestokPro

Este sistema permite testar e monitorar a performance da aplicação GestokPro através de testes de carga simulados.

## 🚀 Como Usar

### 1. Interface Web
Acesse `/teste-estresse` na aplicação para:
- Visualizar histórico de testes
- Executar novos testes via interface
- Ver métricas em tempo real
- Baixar relatórios

### 2. Linha de Comando

#### Teste Rápido (30 segundos)
```bash
python run_stress_test.py
```

#### Teste Avançado (45 segundos)
```bash
python advanced_stress_test.py
```

#### Menu Interativo
```bash
python test_menu.py
```

## 📊 Tipos de Teste

### Teste Básico
- **Duração:** Configurável (padrão: 30s)
- **Usuários:** 2-3 por onda
- **Comportamento:** Navegação padrão
- **Relatório:** Básico com métricas principais

### Teste Avançado
- **Duração:** 45 segundos
- **Usuários:** Mistos (normal, pesado, rápido)
- **Comportamento:** Simulação realística
- **Relatório:** Detalhado com análises avançadas

### Teste Intensivo
- **Duração:** 60-90 segundos
- **Usuários:** 5+ por onda
- **Comportamento:** Alta concorrência
- **Relatório:** Foco em limites do sistema

## 📈 Métricas Coletadas

### Performance
- Tempo de resposta médio, mínimo, máximo
- Percentis (P50, P90, P95, P99)
- Desvio padrão e coeficiente de variação
- Throughput (requests por minuto)

### Confiabilidade
- Taxa de sucesso
- Detecção de anomalias
- Status codes
- Uptime calculado

### Análise por Endpoint
- Performance individual
- Padrões de uso
- Endpoints mais lentos
- Recomendações de otimização

## 🎯 Interpretação dos Resultados

### Status de Performance
- **🟢 Excelente:** < 200ms médio
- **🟡 Bom:** 200-500ms médio
- **🟠 Atenção:** 500-1000ms médio
- **🔴 Crítico:** > 1000ms médio

### Recomendações Automáticas
O sistema gera automaticamente:
- Ações críticas necessárias
- Endpoints para otimização
- Melhorias de estabilidade
- Configurações recomendadas

## 📋 Estrutura dos Arquivos

### Scripts Principais
- `test_stress.py` - Sistema base de teste
- `advanced_stress_test.py` - Teste avançado com análises detalhadas
- `run_stress_test.py` - Script rápido para execução
- `test_menu.py` - Menu interativo
- `templates/teste_estresse.html` - Interface web

### Relatórios Gerados
- `stress_test_report_YYYYMMDD_HHMMSS.md` - Relatório básico
- `advanced_stress_report_YYYYMMDD_HHMMSS.md` - Relatório avançado

## 🛠️ Configurações

### Parâmetros Principais
```python
BASE_URL = "http://localhost:5000"  # URL da aplicação
DURATION = 30  # Duração em segundos
USERS_PER_WAVE = 2  # Usuários simultâneos
```

### Tipos de Usuário Simulado
- **Normal:** Navegação típica com pausas
- **Pesado:** Múltiplas operações, busca intensiva
- **Rápido:** Navegação rápida, poucas operações

## 📊 Exemplo de Resultados

### Último Teste Executado
- **Total de Requests:** 66
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio:** 1990.03 ms
- **Status:** 🔴 CRÍTICO (necessita otimização)

### Endpoints Mais Lentos
1. `/dashboard` - 2753.6 ms médio
2. `/produtos` - 2196.4 ms médio
3. `/produtos/novo` - 1309.7 ms médio

## 🔧 Otimizações Recomendadas

### Baseado nos Resultados Atuais
1. **Cache de Consultas:** Implementar cache Redis/Memcached
2. **Otimização SQL:** Revisar queries do dashboard
3. **Índices:** Adicionar índices nas consultas mais frequentes
4. **Paginação:** Melhorar eficiência da paginação de produtos
5. **Connection Pooling:** Otimizar pool de conexões do PostgreSQL

## 💡 Dicas de Uso

### Para Desenvolvimento
- Execute testes regulares durante desenvolvimento
- Compare performance antes/depois de mudanças
- Use teste rápido para iterações
- Use teste avançado para validação completa

### Para Produção
- Execute testes em ambiente similar à produção
- Monitore tendências de performance
- Configure alertas baseados nos limites
- Use relatórios para planejamento de capacidade

## 🚨 Considerações Importantes

### Limitações
- Testes são executados localmente
- Não simula carga de rede real
- Cache do navegador não é simulado
- Conexão com banco é local

### Boas Práticas
- Não execute em produção
- Execute em horários de baixo uso
- Monitore recursos do sistema durante testes
- Mantenha histórico de testes para comparação

---

*Sistema desenvolvido para monitoramento e otimização contínua da performance do GestokPro*