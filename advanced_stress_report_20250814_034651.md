# Relatório Avançado de Teste de Estresse - GestokPro

**Data/Hora:** 14/08/2025 às 03:46:51  
**URL Testada:** http://localhost:5000  
**Tipo de Teste:** Carga Mista (Usuários Normal, Pesado e Rápido)

## 📊 Resumo Executivo

### Indicadores Chave de Performance (KPIs)
- **Total de Requests:** 66
- **Taxa de Sucesso:** 100.0%
- **Tempo de Resposta Médio:** 1990.03 ms
- **Throughput Médio:** 72.2 req/min

### Classificação de Performance
**Status:** 🔴 CRÍTICO  
**Avaliação:** Performance inaceitável, ação imediata necessária

## 📈 Análise de Percentis de Latência

| Percentil | Tempo de Resposta |
|-----------|-------------------|
| P10 | 609.19 ms |
| P25 | 1319.14 ms |
| P50 | 2125.87 ms |
| P75 | 2629.38 ms |
| P80 | 2978.25 ms |
| P85 | 3230.99 ms |
| P90 | 3233.18 ms |
| P95 | 3234.77 ms |
| P99 | 3306.32 ms |
| P99.9 | 3306.32 ms |

## ⚡ Análise de Throughput

| Horário | Req/min | Tempo Médio | Tempo Máximo |
|---------|---------|-------------|--------------|
| 03:45 | 10 | 2748.2 ms | 3233.3 ms |
| 03:46 | 56 | 1854.6 ms | 3306.3 ms |

## 🔍 Análise de Padrões de Uso

### Endpoints Mais Acessados
- **/dashboard**: 15 requests (22.7%)
- **/produtos**: 15 requests (22.7%)
- **/produtos/novo**: 12 requests (18.2%)
- **/produtos?page=1**: 9 requests (13.6%)
- **/produtos?search=notebook**: 6 requests (9.1%)

## 💡 Recomendações de Otimização

### 🔴 Ações Críticas
- Implementar cache de consultas ao banco de dados
- Otimizar queries SQL mais lentas
- Considerar implementar paginação mais eficiente
- Revisar índices do banco de dados

### 🔧 Endpoints para Otimização
- **/dashboard**: 2753.6 ms médio
- **/produtos?search=monitor**: 2224.2 ms médio
- **/produtos**: 2196.4 ms médio
- **/produtos?search=notebook**: 2127.2 ms médio
- **/produtos?search=mouse**: 1904.6 ms médio
- **/produtos?page=1**: 1635.6 ms médio
- **/produtos/novo**: 1309.7 ms médio
- **/produtos?page=2**: 608.4 ms médio

## 📊 Dados Técnicos Detalhados

### Distribuição de Status Codes
- **200**: 66 requests (100.0%)

### Métricas de Confiabilidade
- **MTTR (Mean Time To Respond)**: 1990.03 ms
- **Desvio Padrão**: 891.54 ms
- **Coeficiente de Variação**: 44.8%
- **Requests com Erro**: 0
- **Uptime**: 100.00%

---
*Relatório gerado automaticamente pelo Sistema Avançado de Teste de Estresse*  
*Versão: 2.0 | Data: 14/08/2025 03:46:51*
