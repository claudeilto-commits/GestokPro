# Relatório de Teste de Estresse - GestokPro

**Data/Hora:** 14/08/2025 às 03:54:11  
**URL Testada:** http://localhost:5000  
**Duração do Teste:** 0:00:37.788698

## 📊 Resumo Geral

- **Total de Requests:** 48
- **Requests Bem-sucedidos:** 48 (100.0%)
- **Requests com Falha:** 0 (0.0%)
- **Taxa de Sucesso:** 100.0%

## ⚡ Métricas de Performance

### Tempo de Resposta (ms)
- **Média:** 1209.28 ms
- **Mediana:** 1208.24 ms
- **Mínimo:** 807.52 ms
- **Máximo:** 1656.61 ms
- **Desvio Padrão:** 202.17 ms

### Percentis
- **P50 (Mediana):** 1208.24 ms
- **P90:** 1613.60 ms
- **P95:** 1622.41 ms
- **P99:** 1656.61 ms

## 🎯 Performance por Endpoint

### /dashboard
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1625.52 ms
- **Tempo Mínimo:** 1613.19 ms
- **Tempo Máximo:** 1656.61 ms

### /produtos
- **Total de Requests:** 18
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1196.84 ms
- **Tempo Mínimo:** 1111.80 ms
- **Tempo Máximo:** 1469.07 ms

### /produtos/novo
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 915.63 ms
- **Tempo Mínimo:** 807.52 ms
- **Tempo Máximo:** 1025.80 ms

### /produtos?page=1
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1214.87 ms
- **Tempo Mínimo:** 1213.33 ms
- **Tempo Máximo:** 1217.20 ms

### /produtos?page=2
- **Total de Requests:** 6
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1212.29 ms
- **Tempo Mínimo:** 1210.63 ms
- **Tempo Máximo:** 1214.37 ms

### /produtos?search=monitor
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1121.74 ms
- **Tempo Mínimo:** 1121.74 ms
- **Tempo Máximo:** 1121.74 ms

### /produtos?search=notebook
- **Total de Requests:** 1
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1111.81 ms
- **Tempo Mínimo:** 1111.81 ms
- **Tempo Máximo:** 1111.81 ms

### /produtos?search=teclado
- **Total de Requests:** 4
- **Taxa de Sucesso:** 100.0%
- **Tempo Médio de Resposta:** 1114.66 ms
- **Tempo Mínimo:** 1108.94 ms
- **Tempo Máximo:** 1123.02 ms

## 🔍 Análise e Recomendações

### Performance Geral
🔴 **Crítico**: Tempo de resposta médio acima de 500ms - otimização necessária
✅ **Excelente**: Taxa de sucesso acima de 99%

### Endpoints que Precisam de Otimização
- **/dashboard**: 1625.52 ms médio
- **/produtos?page=1**: 1214.87 ms médio
- **/produtos?page=2**: 1212.29 ms médio
- **/produtos**: 1196.84 ms médio
- **/produtos?search=monitor**: 1121.74 ms médio
- **/produtos?search=teclado**: 1114.66 ms médio
- **/produtos?search=notebook**: 1111.81 ms médio
- **/produtos/novo**: 915.63 ms médio

## 📋 Dados Detalhados

### Últimos 10 Requests
- ✅ GET /produtos - 1115.4ms (200)
- ✅ GET /produtos - 1116.86ms (200)
- ✅ GET /produtos?search=teclado - 1113.57ms (200)
- ✅ GET /produtos?search=notebook - 1111.81ms (200)
- ✅ GET /produtos?page=1 - 1214.69ms (200)
- ✅ GET /produtos?page=1 - 1216.68ms (200)
- ✅ GET /produtos?page=2 - 1214.37ms (200)
- ✅ GET /produtos?page=2 - 1210.63ms (200)
- ✅ GET /produtos/novo - 1008.43ms (200)
- ✅ GET /produtos/novo - 807.52ms (200)

---
*Relatório gerado automaticamente pelo Sistema de Teste de Estresse do GestokPro*
