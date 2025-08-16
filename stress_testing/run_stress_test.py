#!/usr/bin/env python3
"""
Script simplificado para executar teste de estresse no GestokPro
"""

import asyncio
import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from test_stress import GestokProStressTester

async def run_quick_test():
    """Executa um teste rápido de estresse"""
    print("🧪 Iniciando teste de estresse do GestokPro...")
    
    # Configurações
    BASE_URL = "http://localhost:5000"
    DURATION = 30  # 30 segundos
    USERS_PER_WAVE = 2  # 2 usuários simultâneos por onda
    
    # Cria testador
    tester = GestokProStressTester(base_url=BASE_URL)
    
    # Executa teste
    await tester.run_stress_test(duration_seconds=DURATION, users_per_wave=USERS_PER_WAVE)
    
    # Gera relatório
    report_file = tester.generate_performance_report()
    
    print(f"\n✅ Teste concluído!")
    print(f"📄 Relatório salvo em: {report_file}")

if __name__ == "__main__":
    asyncio.run(run_quick_test())