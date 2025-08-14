#!/usr/bin/env python3
"""
Sistema Avançado de Teste de Estresse para GestokPro
Inclui testes mais sofisticados e relatórios com gráficos
"""

import asyncio
import aiohttp
import time
import json
import random
import statistics
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import threading
import os
import sys

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from test_stress import GestokProStressTester

class AdvancedGestokProTester(GestokProStressTester):
    def __init__(self, base_url="http://localhost:5000"):
        super().__init__(base_url)
        self.memory_snapshots = []
        self.cpu_usage = []
        self.concurrent_users = []
        
    async def simulate_realistic_user(self, session_id, behavior_type="normal"):
        """Simula comportamento mais realista de usuário"""
        async with aiohttp.ClientSession() as session:
            # Login
            login_success = await self.login_user(session)
            if not login_success:
                return
                
            if behavior_type == "heavy":
                # Usuário pesado - faz muitas operações
                operations = [
                    ('/dashboard', 'GET', 'Dashboard'),
                    ('/produtos', 'GET', 'Lista Produtos'),
                    ('/produtos?search=notebook', 'GET', 'Busca Notebook'),
                    ('/produtos?search=mouse', 'GET', 'Busca Mouse'),
                    ('/produtos?page=1', 'GET', 'Página 1'),
                    ('/produtos?page=2', 'GET', 'Página 2'),
                    ('/produtos/novo', 'GET', 'Novo Produto'),
                    ('/produtos', 'GET', 'Lista Produtos 2'),
                    ('/dashboard', 'GET', 'Dashboard 2'),
                ]
                delay_between_ops = 0.1
                
            elif behavior_type == "fast":
                # Usuário rápido - navega rapidamente
                operations = [
                    ('/dashboard', 'GET', 'Dashboard'),
                    ('/produtos', 'GET', 'Lista Produtos'),
                    ('/produtos/novo', 'GET', 'Novo Produto'),
                ]
                delay_between_ops = 0.05
                
            else:  # normal
                # Usuário normal
                operations = [
                    ('/dashboard', 'GET', 'Dashboard'),
                    ('/produtos', 'GET', 'Lista Produtos'),
                    ('/produtos?search=' + random.choice(['notebook', 'mouse', 'monitor']), 'GET', 'Busca'),
                    ('/produtos?page=1', 'GET', 'Paginação'),
                    ('/produtos/novo', 'GET', 'Formulário'),
                ]
                delay_between_ops = 0.2
            
            # Executa operações
            for endpoint, method, description in operations:
                await self.test_endpoint(
                    session, method, endpoint, 
                    description=f"{description} - {behavior_type.title()} User {session_id}"
                )
                await asyncio.sleep(delay_between_ops)
    
    async def run_mixed_load_test(self, duration_seconds=60):
        """Executa teste com diferentes tipos de carga"""
        print(f"🚀 Iniciando teste de carga mista...")
        print(f"📊 Duração: {duration_seconds}s")
        print("-" * 60)
        
        start_time = time.time()
        wave = 1
        
        while time.time() - start_time < duration_seconds:
            # Mistura diferentes tipos de usuários
            user_types = ['normal'] * 2 + ['heavy'] * 1 + ['fast'] * 1
            random.shuffle(user_types)
            
            print(f"🌊 Onda {wave} - Usuários: {', '.join(user_types)}")
            
            # Cria tasks para diferentes tipos de usuários
            tasks = []
            for i, user_type in enumerate(user_types):
                session_id = f"{wave}-{i+1}"
                task = asyncio.create_task(
                    self.simulate_realistic_user(session_id, user_type)
                )
                tasks.append(task)
            
            # Executa usuários simultaneamente
            await asyncio.gather(*tasks, return_exceptions=True)
            
            wave += 1
            await asyncio.sleep(random.uniform(1, 3))  # Pausa variável entre ondas
            
        print(f"✅ Teste de carga mista concluído!")
        print(f"📈 Total de requests: {len(self.results)}")
    
    def generate_advanced_report(self):
        """Gera relatório avançado com mais análises"""
        if not self.results:
            print("❌ Nenhum resultado disponível")
            return
            
        # Análise temporal
        results_by_time = {}
        for result in self.results:
            timestamp = datetime.fromisoformat(result['timestamp'])
            time_bucket = timestamp.replace(second=0, microsecond=0)  # Agrupa por minuto
            
            if time_bucket not in results_by_time:
                results_by_time[time_bucket] = []
            results_by_time[time_bucket].append(result['response_time_ms'])
        
        # Calcula throughput por minuto
        throughput_data = []
        for time_bucket, response_times in sorted(results_by_time.items()):
            throughput_data.append({
                'time': time_bucket.strftime('%H:%M'),
                'requests_per_minute': len(response_times),
                'avg_response_time': statistics.mean(response_times),
                'max_response_time': max(response_times)
            })
        
        # Análise de percentis mais detalhada
        response_times = [r['response_time_ms'] for r in self.results]
        response_times.sort()
        
        percentiles = {}
        for p in [10, 25, 50, 75, 80, 85, 90, 95, 99, 99.9]:
            if len(response_times) > 0:
                index = int(len(response_times) * (p / 100.0))
                if index >= len(response_times):
                    index = len(response_times) - 1
                percentiles[f'P{p}'] = response_times[index]
        
        # Detecção de anomalias
        mean_time = statistics.mean(response_times)
        std_dev = statistics.stdev(response_times) if len(response_times) > 1 else 0
        threshold = mean_time + (2 * std_dev)  # 2 desvios padrão
        
        anomalies = [r for r in self.results if r['response_time_ms'] > threshold]
        
        # Gera relatório
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"advanced_stress_report_{timestamp}.md"
        
        report_content = f"""# Relatório Avançado de Teste de Estresse - GestokPro

**Data/Hora:** {datetime.now().strftime("%d/%m/%Y às %H:%M:%S")}  
**URL Testada:** {self.base_url}  
**Tipo de Teste:** Carga Mista (Usuários Normal, Pesado e Rápido)

## 📊 Resumo Executivo

### Indicadores Chave de Performance (KPIs)
- **Total de Requests:** {len(self.results)}
- **Taxa de Sucesso:** {len([r for r in self.results if r['success']])/len(self.results)*100:.1f}%
- **Tempo de Resposta Médio:** {statistics.mean(response_times):.2f} ms
- **Throughput Médio:** {len(self.results) / ((max([datetime.fromisoformat(r['timestamp']) for r in self.results]) - min([datetime.fromisoformat(r['timestamp']) for r in self.results])).total_seconds() / 60):.1f} req/min

### Classificação de Performance
"""
        
        avg_time = statistics.mean(response_times)
        if avg_time < 200:
            performance_grade = "🟢 EXCELENTE"
            performance_desc = "Sistema operando com performance ótima"
        elif avg_time < 500:
            performance_grade = "🟡 BOM"
            performance_desc = "Performance aceitável, monitoramento recomendado"
        elif avg_time < 1000:
            performance_grade = "🟠 ATENÇÃO"
            performance_desc = "Performance degradada, otimização necessária"
        else:
            performance_grade = "🔴 CRÍTICO"
            performance_desc = "Performance inaceitável, ação imediata necessária"
            
        report_content += f"**Status:** {performance_grade}  \n**Avaliação:** {performance_desc}\n\n"
        
        # Percentis detalhados
        report_content += f"""## 📈 Análise de Percentis de Latência

| Percentil | Tempo de Resposta |
|-----------|-------------------|
"""
        for percentil, valor in percentiles.items():
            report_content += f"| {percentil} | {valor:.2f} ms |\n"
        
        # Throughput por tempo
        report_content += f"""
## ⚡ Análise de Throughput

| Horário | Req/min | Tempo Médio | Tempo Máximo |
|---------|---------|-------------|--------------|
"""
        for data in throughput_data:
            report_content += f"| {data['time']} | {data['requests_per_minute']} | {data['avg_response_time']:.1f} ms | {data['max_response_time']:.1f} ms |\n"
        
        # Anomalias
        if anomalies:
            report_content += f"""
## 🚨 Detecção de Anomalias

Foram detectados **{len(anomalies)}** requests com tempo de resposta anômalo (>{threshold:.1f} ms):

"""
            for anomaly in anomalies[-5:]:  # Últimas 5 anomalias
                report_content += f"- {anomaly['endpoint']} - {anomaly['response_time_ms']:.1f} ms ({anomaly['timestamp']})\n"
        
        # Análise de padrões
        report_content += f"""
## 🔍 Análise de Padrões de Uso

### Endpoints Mais Acessados
"""
        endpoint_counts = {}
        for result in self.results:
            endpoint = result['endpoint']
            endpoint_counts[endpoint] = endpoint_counts.get(endpoint, 0) + 1
        
        for endpoint, count in sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            percentage = (count / len(self.results)) * 100
            report_content += f"- **{endpoint}**: {count} requests ({percentage:.1f}%)\n"
        
        # Recomendações baseadas nos dados
        report_content += f"""
## 💡 Recomendações de Otimização

"""
        
        if avg_time > 1000:
            report_content += "### 🔴 Ações Críticas\n"
            report_content += "- Implementar cache de consultas ao banco de dados\n"
            report_content += "- Otimizar queries SQL mais lentas\n"
            report_content += "- Considerar implementar paginação mais eficiente\n"
            report_content += "- Revisar índices do banco de dados\n\n"
        
        if len(anomalies) > len(self.results) * 0.05:  # Mais de 5% de anomalias
            report_content += "### 🟠 Estabilidade\n"
            report_content += "- Investigar picos de latência\n"
            report_content += "- Implementar circuit breakers\n"
            report_content += "- Configurar alertas de performance\n\n"
        
        # Endpoints que precisam de otimização
        slow_endpoints = []
        endpoint_stats = {}
        for result in self.results:
            endpoint = result['endpoint']
            if endpoint not in endpoint_stats:
                endpoint_stats[endpoint] = []
            endpoint_stats[endpoint].append(result['response_time_ms'])
        
        for endpoint, times in endpoint_stats.items():
            avg_endpoint_time = statistics.mean(times)
            if avg_endpoint_time > 500:  # Endpoints com mais de 500ms
                slow_endpoints.append((endpoint, avg_endpoint_time))
        
        if slow_endpoints:
            report_content += "### 🔧 Endpoints para Otimização\n"
            for endpoint, avg_time in sorted(slow_endpoints, key=lambda x: x[1], reverse=True):
                report_content += f"- **{endpoint}**: {avg_time:.1f} ms médio\n"
        
        report_content += f"""
## 📊 Dados Técnicos Detalhados

### Distribuição de Status Codes
"""
        status_codes = {}
        for result in self.results:
            code = result['status_code']
            status_codes[code] = status_codes.get(code, 0) + 1
        
        for code, count in sorted(status_codes.items()):
            percentage = (count / len(self.results)) * 100
            report_content += f"- **{code}**: {count} requests ({percentage:.1f}%)\n"
        
        report_content += f"""
### Métricas de Confiabilidade
- **MTTR (Mean Time To Respond)**: {statistics.mean(response_times):.2f} ms
- **Desvio Padrão**: {std_dev:.2f} ms
- **Coeficiente de Variação**: {(std_dev/statistics.mean(response_times))*100:.1f}%
- **Requests com Erro**: {len([r for r in self.results if not r['success']])}
- **Uptime**: {len([r for r in self.results if r['success']])/len(self.results)*100:.2f}%

---
*Relatório gerado automaticamente pelo Sistema Avançado de Teste de Estresse*  
*Versão: 2.0 | Data: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}*
"""
        
        # Salva o relatório
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        print(f"📄 Relatório avançado salvo: {report_filename}")
        
        # Exibe resumo no console
        print("\n" + "="*70)
        print("🎯 RELATÓRIO AVANÇADO DE TESTE DE ESTRESSE")
        print("="*70)
        print(f"Status de Performance: {performance_grade}")
        print(f"Total de Requests: {len(self.results)}")
        print(f"Taxa de Sucesso: {len([r for r in self.results if r['success']])/len(self.results)*100:.1f}%")
        print(f"Tempo Médio: {avg_time:.2f} ms")
        print(f"P95: {percentiles.get('P95', 0):.2f} ms")
        print(f"P99: {percentiles.get('P99', 0):.2f} ms")
        print(f"Anomalias Detectadas: {len(anomalies)}")
        print(f"Endpoints Lentos: {len(slow_endpoints)}")
        print("="*70)
        
        return report_filename

async def main():
    """Executa teste avançado"""
    print("🧪 GestokPro - Sistema Avançado de Teste de Estresse")
    print("=" * 60)
    
    # Configurações do teste
    BASE_URL = "http://localhost:5000"
    DURATION = 45  # segundos
    
    # Cria testador avançado
    tester = AdvancedGestokProTester(base_url=BASE_URL)
    
    # Executa teste de carga mista
    await tester.run_mixed_load_test(duration_seconds=DURATION)
    
    # Gera relatório avançado
    report_file = tester.generate_advanced_report()
    
    print(f"\n🎉 Teste avançado concluído!")
    print(f"📊 Relatório detalhado: {report_file}")

if __name__ == "__main__":
    asyncio.run(main())