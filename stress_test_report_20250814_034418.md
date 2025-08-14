# Relatório de Teste de Estresse - GestokPro

**Data/Hora:** 14/08/2025 às 03:44:18  
**URL Testada:** http://localhost:5000  
**Duração do Teste:** 0:00:38.086240

## 📊 Resumo Geral

- **Total de Requests:** 48
- **Requests Bem-sucedidos:** 48 (100.0%)
- **Requests com Falha:** 0 (0.0%)
- **Taxa de Sucesso:** 100.0%

## ⚡ Métricas de Performance

### Tempo de Resposta (ms)
- **Média:** 1221.17 ms
- **Mediana:** 1196.59 ms
- **Mínimo:** 817.51 ms
- **Máximo:** 1685.03 ms
- **Desvio Padrão:** 207.36 ms

### Percentis
- **P50 (Mediana):** 1196.59 ms
- **P90:** 1638.68 ms
- **P95:** 1656.62 ms
- **P99:** 1685.03 ms

## 🎯 Performance por Endpoint

### /dashboard
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1652.16 ms
- **Tempo Mínimo:** 1637.01 ms
- **Tempo Máximo:** 1685.03 ms

### /produtos
- **Total de Requests:** 18
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1204.65 ms
- **Tempo Mínimo:** 1123.26 ms
- **Tempo Máximo:** 1485.58 ms

### /produtos/novo
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 920.38 ms
- **Tempo Mínimo:** 817.51 ms
- **Tempo Máximo:** 1022.99 ms

### /produtos?page=1
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1228.47 ms
- **Tempo Mínimo:** 1226.77 ms
- **Tempo Máximo:** 1230.18 ms

### /produtos?page=2
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1226.34 ms
- **Tempo Mínimo:** 1224.56 ms
- **Tempo Máximo:** 1228.71 ms

### /produtos?search=monitor
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1124.38 ms
- **Tempo Mínimo:** 1124.38 ms
- **Tempo Máximo:** 1124.38 ms

### /produtos?search=mouse
- **Total de Requests:** 3
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1127.26 ms
- **Tempo Mínimo:** 1124.93 ms
- **Tempo Máximo:** 1129.68 ms

### /produtos?search=notebook
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1132.02 ms
- **Tempo Mínimo:** 1132.02 ms
- **Tempo Máximo:** 1132.02 ms

### /produtos?search=teclado
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1130.23 ms
- **Tempo Mínimo:** 1130.23 ms
- **Tempo Máximo:** 1130.23 ms

## 🔍 Análise e Recomendações

### Performance Geral
🔴 **Crítico**: Tempo de resposta médio acima de 500ms - otimização necessária
✅ **Excelente**: Taxa de sucesso acima de 99%

### Endpoints que Precisam de Otimização
- **/dashboard**: 1652.16 ms médio
- **/produtos?page=1**: 1228.47 ms médio
- **/produtos?page=2**: 1226.34 ms médio
- **/produtos**: 1204.65 ms médio
- **/produtos?search=notebook**: 1132.02 ms médio
- **/produtos?search=teclado**: 1130.23 ms médio
- **/produtos?search=mouse**: 1127.26 ms médio
- **/produtos?search=monitor**: 1124.38 ms médio
- **/produtos/novo**: 920.38 ms médio

## 📋 Dados Detalhados

### Últimos 10 Requests
- ✅ GET /produtos - 1137.61ms (200)
- ✅ GET /produtos - 1128.36ms (200)
- ✅ GET /produtos?search=mouse - 1129.68ms (200)
- ✅ GET /produtos?search=mouse - 1127.18ms (200)
- ✅ GET /produtos?page=1 - 1230.18ms (200)
- ✅ GET /produtos?page=1 - 1229.24ms (200)
- ✅ GET /produtos?page=2 - 1225.45ms (200)
- ✅ GET /produtos?page=2 - 1225.76ms (200)
- ✅ GET /produtos/novo - 1021.7ms (200)
- ✅ GET /produtos/novo - 818.15ms (200)

---
*Relatório gerado automaticamente pelo Sistema de Teste de Estresse do GestokPro*
