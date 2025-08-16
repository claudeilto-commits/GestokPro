#!/usr/bin/env python3
"""
Sistema de Teste de Estresse para GestokPro
Simula múltiplos usuários e operações para testar performance da aplicação.
"""

import asyncio
import aiohttp
import time
import json
import random
import statistics
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import threading

class GestokProStressTester:
    def __init__(self, base_url="http://localhost:5000", max_concurrent=10):
        self.base_url = base_url
        self.max_concurrent = max_concurrent
        self.results = []
        self.login_cookies = None
        self.test_products = []
        self.lock = threading.Lock()
        
    async def get_csrf_token(self, session):
        """Obtém token CSRF da página de login"""
        try:
            async with session.get(f"{self.base_url}/login") as response:
                html = await response.text()
                # Busca pelo token CSRF no HTML
                import re
                match = re.search(r'name="csrf_token"[^>]*value="([^"]*)"', html)
                return match.group(1) if match else None
        except:
            return None

    async def login_user(self, session):
        """Realiza login na aplicação"""
        try:
            csrf_token = await self.get_csrf_token(session)
            if not csrf_token:
                return False
                
            login_data = {
                'email': 'admin@gestokpro.com',
                'password': 'admin',
                'csrf_token': csrf_token,
                'remember_me': False
            }
            
            async with session.post(f"{self.base_url}/login", data=login_data) as response:
                return response.status in [200, 302]  # 302 = redirect após login
        except:
            return False

    async def test_endpoint(self, session, method, endpoint, data=None, description=""):
        """Testa um endpoint específico e mede o tempo de resposta"""
        start_time = time.time()
        success = False
        status_code = 0
        
        try:
            if method.upper() == 'GET':
                async with session.get(f"{self.base_url}{endpoint}") as response:
                    status_code = response.status
                    success = 200 <= status_code < 400
            elif method.upper() == 'POST':
                async with session.post(f"{self.base_url}{endpoint}", data=data) as response:
                    status_code = response.status
                    success = 200 <= status_code < 400
                    
        except Exception as e:
            success = False
            status_code = 0
            
        response_time = (time.time() - start_time) * 1000  # em ms
        
        result = {
            'timestamp': datetime.now().isoformat(),
            'method': method,
            'endpoint': endpoint,
            'description': description,
            'response_time_ms': round(response_time, 2),
            'status_code': status_code,
            'success': success
        }
        
        with self.lock:
            self.results.append(result)
            
        return result

    async def simulate_user_session(self, session_id):
        """Simula uma sessão completa de usuário"""
        async with aiohttp.ClientSession() as session:
            # 1. Login
            login_success = await self.login_user(session)
            if not login_success:
                print(f"❌ Sessão {session_id}: Falha no login")
                return
                
            print(f"✅ Sessão {session_id}: Login realizado")
            
            # 2. Acessa dashboard
            await self.test_endpoint(session, 'GET', '/dashboard', 
                                   description=f"Dashboard - Sessão {session_id}")
            
            # 3. Lista produtos (múltiplas vezes)
            for i in range(3):
                await self.test_endpoint(session, 'GET', '/produtos', 
                                       description=f"Lista Produtos {i+1} - Sessão {session_id}")
                await asyncio.sleep(0.1)  # Pequena pausa entre requests
            
            # 4. Busca produtos
            search_terms = ['notebook', 'mouse', 'teclado', 'monitor']
            search_term = random.choice(search_terms)
            await self.test_endpoint(session, 'GET', f'/produtos?search={search_term}', 
                                   description=f"Busca '{search_term}' - Sessão {session_id}")
            
            # 5. Simula navegação entre páginas
            for page in range(1, 3):
                await self.test_endpoint(session, 'GET', f'/produtos?page={page}', 
                                       description=f"Página {page} - Sessão {session_id}")
            
            # 6. Acessa formulário de novo produto
            await self.test_endpoint(session, 'GET', '/produtos/novo', 
                                   description=f"Formulário Novo Produto - Sessão {session_id}")
            
            print(f"✅ Sessão {session_id}: Completada")

    async def run_stress_test(self, duration_seconds=60, users_per_wave=5):
        """Executa teste de estresse principal"""
        print(f"🚀 Iniciando teste de estresse...")
        print(f"📊 Duração: {duration_seconds}s | Usuários por onda: {users_per_wave}")
        print(f"🔗 URL: {self.base_url}")
        print("-" * 60)
        
        start_time = time.time()
        wave = 1
        
        while time.time() - start_time < duration_seconds:
            print(f"🌊 Onda {wave} - {users_per_wave} usuários simultâneos")
            
            # Cria tasks para usuários simultâneos
            tasks = []
            for user_id in range(users_per_wave):
                session_id = f"{wave}-{user_id + 1}"
                task = asyncio.create_task(self.simulate_user_session(session_id))
                tasks.append(task)
            
            # Executa todos os usuários da onda simultaneamente
            await asyncio.gather(*tasks, return_exceptions=True)
            
            wave += 1
            await asyncio.sleep(2)  # Pausa entre ondas
            
        print(f"✅ Teste de estresse concluído!")
        print(f"📈 Total de requests executados: {len(self.results)}")

    def generate_performance_report(self):
        """Gera relatório detalhado de performance"""
        if not self.results:
            print("❌ Nenhum resultado disponível para gerar relatório")
            return
            
        # Estatísticas gerais
        response_times = [r['response_time_ms'] for r in self.results]
        successful_requests = [r for r in self.results if r['success']]
        failed_requests = [r for r in self.results if not r['success']]
        
        # Estatísticas por endpoint
        endpoints_stats = {}
        for result in self.results:
            endpoint = result['endpoint']
            if endpoint not in endpoints_stats:
                endpoints_stats[endpoint] = {
                    'count': 0,
                    'success_count': 0,
                    'response_times': [],
                    'status_codes': []
                }
            
            stats = endpoints_stats[endpoint]
            stats['count'] += 1
            if result['success']:
                stats['success_count'] += 1
            stats['response_times'].append(result['response_time_ms'])
            stats['status_codes'].append(result['status_code'])
        
        # Gera relatório
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"stress_test_report_{timestamp}.md"
        
        report_content = f"""# Relatório de Teste de Estresse - GestokPro

**Data/Hora:** {datetime.now().strftime("%d/%m/%Y às %H:%M:%S")}  
**URL Testada:** {self.base_url}  
**Duração do Teste:** {max([datetime.fromisoformat(r['timestamp']) for r in self.results]) - min([datetime.fromisoformat(r['timestamp']) for r in self.results])}

## 📊 Resumo Geral

- **Total de Requests:** {len(self.results)}
- **Requests Bem-sucedidos:** {len(successful_requests)} ({len(successful_requests)/len(self.results)*100:.1f}%)
- **Requests com Falha:** {len(failed_requests)} ({len(failed_requests)/len(self.results)*100:.1f}%)
- **Taxa de Sucesso:** {len(successful_requests)/len(self.results)*100:.1f}%

## ⚡ Métricas de Performance

### Tempo de Resposta (ms)
- **Média:** {statistics.mean(response_times):.2f} ms
- **Mediana:** {statistics.median(response_times):.2f} ms
- **Mínimo:** {min(response_times):.2f} ms
- **Máximo:** {max(response_times):.2f} ms
- **Desvio Padrão:** {statistics.stdev(response_times) if len(response_times) > 1 else 0:.2f} ms

### Percentis
- **P50 (Mediana):** {statistics.median(response_times):.2f} ms
- **P90:** {sorted(response_times)[int(len(response_times) * 0.9)]:.2f} ms
- **P95:** {sorted(response_times)[int(len(response_times) * 0.95)]:.2f} ms
- **P99:** {sorted(response_times)[int(len(response_times) * 0.99)]:.2f} ms

## 🎯 Performance por Endpoint

"""
        
        for endpoint, stats in sorted(endpoints_stats.items()):
            avg_response = statistics.mean(stats['response_times'])
            success_rate = (stats['success_count'] / stats['count']) * 100
            
            report_content += f"""### {endpoint}
- **Total de Requests:** {stats['count']}
- **Taxa de Sucesso:** {success_rate:.1f}%
- **Tempo Médio de Resposta:** {avg_response:.2f} ms
- **Tempo Mínimo:** {min(stats['response_times']):.2f} ms
- **Tempo Máximo:** {max(stats['response_times']):.2f} ms

"""
        
        # Análise e recomendações
        avg_response_time = statistics.mean(response_times)
        success_rate = len(successful_requests) / len(self.results) * 100
        
        report_content += f"""## 🔍 Análise e Recomendações

### Performance Geral
"""
        
        if avg_response_time < 100:
            report_content += "✅ **Excelente**: Tempo de resposta médio abaixo de 100ms\n"
        elif avg_response_time < 200:
            report_content += "🟡 **Bom**: Tempo de resposta médio entre 100-200ms\n"
        elif avg_response_time < 500:
            report_content += "🟠 **Aceitável**: Tempo de resposta médio entre 200-500ms\n"
        else:
            report_content += "🔴 **Crítico**: Tempo de resposta médio acima de 500ms - otimização necessária\n"
            
        if success_rate >= 99:
            report_content += "✅ **Excelente**: Taxa de sucesso acima de 99%\n"
        elif success_rate >= 95:
            report_content += "🟡 **Bom**: Taxa de sucesso entre 95-99%\n"
        else:
            report_content += "🔴 **Crítico**: Taxa de sucesso abaixo de 95% - investigação necessária\n"
            
        # Endpoints mais lentos
        slow_endpoints = []
        for endpoint, stats in endpoints_stats.items():
            avg_time = statistics.mean(stats['response_times'])
            if avg_time > 200:  # endpoints com mais de 200ms em média
                slow_endpoints.append((endpoint, avg_time))
        
        if slow_endpoints:
            report_content += f"\n### Endpoints que Precisam de Otimização\n"
            for endpoint, avg_time in sorted(slow_endpoints, key=lambda x: x[1], reverse=True):
                report_content += f"- **{endpoint}**: {avg_time:.2f} ms médio\n"
        
        report_content += f"""
## 📋 Dados Detalhados

### Últimos 10 Requests
"""
        
        # Últimos requests
        recent_requests = sorted(self.results, key=lambda x: x['timestamp'])[-10:]
        for req in recent_requests:
            status_icon = "✅" if req['success'] else "❌"
            report_content += f"- {status_icon} {req['method']} {req['endpoint']} - {req['response_time_ms']}ms ({req['status_code']})\n"
        
        report_content += f"""
---
*Relatório gerado automaticamente pelo Sistema de Teste de Estresse do GestokPro*
"""
        
        # Salva o relatório
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        print(f"📄 Relatório salvo em: {report_filename}")
        
        # Exibe resumo no console
        print("\n" + "="*60)
        print("📊 RESUMO DO TESTE DE ESTRESSE")
        print("="*60)
        print(f"Total de Requests: {len(self.results)}")
        print(f"Taxa de Sucesso: {success_rate:.1f}%")
        print(f"Tempo Médio: {avg_response_time:.2f} ms")
        print(f"Tempo Máximo: {max(response_times):.2f} ms")
        print(f"Relatório completo: {report_filename}")
        print("="*60)
        
        return report_filename

async def main():
    """Função principal"""
    print("🧪 GestokPro - Sistema de Teste de Estresse")
    print("=" * 50)
    
    # Configurações do teste
    BASE_URL = "http://localhost:5000"
    DURATION = 30  # segundos
    USERS_PER_WAVE = 3  # usuários simultâneos por onda
    
    # Cria instância do testador
    tester = GestokProStressTester(base_url=BASE_URL)
    
    # Executa teste de estresse
    await tester.run_stress_test(duration_seconds=DURATION, users_per_wave=USERS_PER_WAVE)
    
    # Gera relatório
    report_file = tester.generate_performance_report()
    
    print(f"\n🎉 Teste concluído! Verifique o arquivo: {report_file}")

if __name__ == "__main__":
    asyncio.run(main())