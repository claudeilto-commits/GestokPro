from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    senha_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    
    def set_password(self, password):
        """Hash and set password"""
        self.senha_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if provided password matches hash"""
        return check_password_hash(self.senha_hash, password)
    
    def __repr__(self):
        return f'<Usuario {self.email}>'

class Produto(db.Model):
    __tablename__ = 'produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False, index=True)
    descricao = db.Column(db.Text)
    quantidade = db.Column(db.Integer, nullable=False, default=0)
    preco_venda = db.Column(db.Numeric(10, 2), nullable=False)
    
    def __repr__(self):
        return f'<Produto {self.nome}>'
    
    @property
    def valor_total_estoque(self):
        """Calculate total stock value for this product"""
        return float(self.quantidade * self.preco_venda)
    
    @property
    def status_estoque(self):
        """Return stock status"""
        if self.quantidade == 0:
            return 'Sem estoque'
        elif self.quantidade <= 5:
            return 'Estoque baixo'
        else:
            return 'Em estoque'
