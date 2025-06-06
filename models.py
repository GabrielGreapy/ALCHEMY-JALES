from sqlalchemy import (
    Column, Integer, String, ForeignKey, Float,
    DateTime, Boolean, func, UniqueConstraint
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property, _HybridSetterType


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)
    pedidos = relationship('Pedido', back_populates='usuario')
    @hybrid_property
    def dominio(self):
        return self.email

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    categoria = Column(String(50))
    estoque = Column(Integer, default=0)
    criado_em = Column(DateTime, default=datetime.now)
    @hybrid_property
    def valor_estoque(self):
        return self.preco * self.estoque
    



class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    status = Column(String(20), default='pendente')
    data_pedido = Column(DateTime, default=datetime.now)

    usuario = relationship('Usuario', back_populates='pedidos')
    produto = relationship('Produto')

    __table_args__ = (
        UniqueConstraint('usuario_id', 'produto_id', name='uq_usuario_produto'),
    )

class Avaliacao(Base):
    __tablename__ = 'avaliacoes'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(String(300))

    usuario = relationship('Usuario')

