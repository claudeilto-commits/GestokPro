from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, NumberRange, ValidationError
from models import Produto

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email é obrigatório'),
        Email(message='Email inválido')
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message='Senha é obrigatória')
    ])
    remember_me = BooleanField('Lembrar de mim')

class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[
        DataRequired(message='Nome é obrigatório'),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    sku = StringField('SKU', validators=[
        DataRequired(message='SKU é obrigatório'),
        Length(min=2, max=50, message='SKU deve ter entre 2 e 50 caracteres')
    ])
    descricao = TextAreaField('Descrição', validators=[
        Length(max=500, message='Descrição deve ter no máximo 500 caracteres')
    ])
    quantidade = IntegerField('Quantidade', validators=[
        DataRequired(message='Quantidade é obrigatória'),
        NumberRange(min=0, message='Quantidade deve ser maior ou igual a 0')
    ])
    preco_venda = DecimalField('Preço de Venda', validators=[
        DataRequired(message='Preço de venda é obrigatório'),
        NumberRange(min=0.01, message='Preço deve ser maior que 0')
    ], places=2)
    
    def __init__(self, produto_id=None, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.produto_id = produto_id
    
    def validate_sku(self, sku):
        produto = Produto.query.filter_by(sku=sku.data).first()
        if produto:
            if self.produto_id is None or produto.id != self.produto_id:
                raise ValidationError('SKU já existe. Use um SKU único.')
