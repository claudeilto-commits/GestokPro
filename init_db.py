#!/usr/bin/env python3
"""
Script para inicializar o banco de dados com dados de exemplo.
Execute este script para recriar o banco de dados com dados iniciais.
"""

import os
import sys
from decimal import Decimal

# Add current directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import Usuario, Produto

def init_database():
    """Initialize database with sample data"""
    print("Inicializando banco de dados...")
    
    with app.app_context():
        # Drop all tables and recreate
        print("Removendo tabelas existentes...")
        db.drop_all()
        
        print("Criando novas tabelas...")
        db.create_all()
        
        # Create admin user
        print("Criando usuário administrador...")
        admin = Usuario(
            email='admin@gestokpro.com',
            is_admin=True
        )
        admin.set_password('admin')
        db.session.add(admin)
        
        # Create sample products
        print("Criando produtos de exemplo...")
        produtos_exemplo = [
            {
                'nome': 'Notebook Dell Inspiron 15',
                'sku': 'DELL-INS-15-001',
                'descricao': 'Notebook Dell Inspiron 15 com processador Intel Core i5, 8GB RAM, SSD 256GB',
                'quantidade': 25,
                'preco_venda': Decimal('2499.99')
            },
            {
                'nome': 'Mouse Logitech MX Master 3',
                'sku': 'LOG-MX3-001',
                'descricao': 'Mouse sem fio ergonômico com sensor de alta precisão e bateria recarregável',
                'quantidade': 50,
                'preco_venda': Decimal('349.90')
            },
            {
                'nome': 'Teclado Mecânico Corsair K95',
                'sku': 'COR-K95-RGB',
                'descricao': 'Teclado mecânico gamer com switches Cherry MX e iluminação RGB personalizada',
                'quantidade': 15,
                'preco_venda': Decimal('899.99')
            },
            {
                'nome': 'Monitor LG UltraWide 29"',
                'sku': 'LG-UW29-001',
                'descricao': 'Monitor ultrawide 29 polegadas, resolução 2560x1080, ideal para produtividade',
                'quantidade': 8,
                'preco_venda': Decimal('1299.00')
            },
            {
                'nome': 'SSD Samsung 970 EVO 1TB',
                'sku': 'SAM-970EVO-1TB',
                'descricao': 'SSD NVMe M.2 de 1TB com velocidades de leitura até 3.500 MB/s',
                'quantidade': 30,
                'preco_venda': Decimal('599.99')
            },
            {
                'nome': 'Webcam Logitech C920',
                'sku': 'LOG-C920-HD',
                'descricao': 'Webcam Full HD 1080p com microfone integrado e correção automática de luz',
                'quantidade': 12,
                'preco_venda': Decimal('289.90')
            },
            {
                'nome': 'Headset HyperX Cloud II',
                'sku': 'HYX-CLD2-001',
                'descricao': 'Headset gamer com som surround 7.1 virtual e microfone com cancelamento de ruído',
                'quantidade': 20,
                'preco_venda': Decimal('399.99')
            },
            {
                'nome': 'Cabo HDMI 2.1 - 2m',
                'sku': 'HDMI-21-2M',
                'descricao': 'Cabo HDMI 2.1 de alta velocidade, suporta 4K@120Hz e 8K@60Hz',
                'quantidade': 100,
                'preco_venda': Decimal('49.90')
            },
            {
                'nome': 'Hub USB-C 7 em 1',
                'sku': 'HUB-USBC-7IN1',
                'descricao': 'Hub USB-C com 7 portas: HDMI, USB 3.0, USB-C, leitor de cartão SD/microSD',
                'quantidade': 35,
                'preco_venda': Decimal('199.99')
            },
            {
                'nome': 'Suporte para Notebook',
                'sku': 'SUP-BOOK-ADJ',
                'descricao': 'Suporte ergonômico ajustável para notebook, melhora postura e ventilação',
                'quantidade': 18,
                'preco_venda': Decimal('129.90')
            }
        ]
        
        for produto_data in produtos_exemplo:
            produto = Produto(**produto_data)
            db.session.add(produto)
        
        # Commit all changes
        db.session.commit()
        
        print("✅ Banco de dados inicializado com sucesso!")
        print("\n📊 Dados criados:")
        print("👤 Usuário administrador:")
        print("   Email: admin@gestokpro.com")
        print("   Senha: admin")
        print(f"\n📦 {len(produtos_exemplo)} produtos de exemplo criados")
        print("\n🚀 Você pode agora executar a aplicação com: python app.py")

if __name__ == '__main__':
    init_database()
