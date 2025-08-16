# Relatório de Teste de Estresse - GestokPro

**Data/Hora:** 14/08/2025 às 04:05:31  
**URL Testada:** http://localhost:5000  
**Duração do Teste:** 0:00:23.144262

## 📊 Resumo Geral

- **Total de Requests:** 32
- **Requests Bem-sucedidos:** 32 (100.0%)
- **Requests com Falha:** 0 (0.0%)
- **Taxa de Sucesso:** 100.0%

## ⚡ Métricas de Performance

### Tempo de Resposta (ms)
- **Média:** 1196.21 ms
- **Mediana:** 1189.79 ms
- **Mínimo:** 800.22 ms
- **Máximo:** 1604.93 ms
- **Desvio Padrão:** 197.28 ms

### Percentis
- **P50 (Mediana):** 1189.79 ms
- **P90:** 1595.97 ms
- **P95:** 1599.65 ms
- **P99:** 1604.93 ms

## 🎯 Performance por Endpoint

### /dashboard
- **Total de Requests:** 4
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1599.36 ms
- **Tempo Mínimo:** 1595.97 ms
- **Tempo Máximo:** 1604.93 ms

### /produtos
- **Total de Requests:** 12
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1184.44 ms
- **Tempo Mínimo:** 1097.76 ms
- **Tempo Máximo:** 1419.39 ms

### /produtos/novo
- **Total de Requests:** 4
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 909.58 ms
- **Tempo Mínimo:** 800.22 ms
- **Tempo Máximo:** 1028.30 ms

### /produtos?page=1
- **Total de Requests:** 4
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1201.49 ms
- **Tempo Mínimo:** 1199.87 ms
- **Tempo Máximo:** 1204.77 ms

### /produtos?page=2
- **Total de Requests:** 4
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1203.51 ms
- **Tempo Mínimo:** 1197.50 ms
- **Tempo Máximo:** 1217.42 ms

### /produtos?search=monitor
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1108.42 ms
- **Tempo Mínimo:** 1108.42 ms
- **Tempo Máximo:** 1108.42 ms

### /produtos?search=mouse
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1104.87 ms
- **Tempo Mínimo:** 1104.87 ms
- **Tempo Máximo:** 1104.87 ms

### /produtos?search=teclado
- **Total de Requests:** 2
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1098.21 ms
- **Tempo Mínimo:** 1096.91 ms
- **Tempo Máximo:** 1099.51 ms

## 🔍 Análise e Recomendações

### Performance Geral
🔴 **Crítico**: Tempo de resposta médio acima de 500ms - otimização necessária
✅ **Excelente**: Taxa de sucesso acima de 99%

### Endpoints que Precisam de Otimização
- **/dashboard**: 1599.36 ms médio
- **/produtos?page=2**: 1203.51 ms médio
- **/produtos?page=1**: 1201.49 ms médio
- **/produtos**: 1184.44 ms médio
- **/produtos?search=monitor**: 1108.42 ms médio
- **/produtos?search=mouse**: 1104.87 ms médio
- **/produtos?search=teclado**: 1098.21 ms médio
- **/produtos/novo**: 909.58 ms médio

## 📋 Dados Detalhados

### Últimos 10 Requests
- ✅ GET /produtos - 1178.78ms (200)
- ✅ GET /produtos - 1097.76ms (200)
- ✅ GET /produtos?search=teclado - 1096.91ms (200)
- ✅ GET /produtos?search=teclado - 1099.51ms (200)
- ✅ GET /produtos?page=1 - 1200.03ms (200)
- ✅ GET /produtos?page=1 - 1199.87ms (200)
- ✅ GET /produtos?page=2 - 1199.19ms (200)
- ✅ GET /produtos?page=2 - 1197.5ms (200)
- ✅ GET /produtos/novo - 999.46ms (200)
- ✅ GET /produtos/novo - 800.22ms (200)

---
*Relatório gerado automaticamente pelo Sistema de Teste de Estresse do GestokPro*
