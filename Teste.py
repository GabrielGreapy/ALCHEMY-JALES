from sqlalchemy import create_engine, func, distinct, exists, and_, or_
from sqlalchemy.orm import sessionmaker, joinedload
from models import Base, Usuario, Produto, Pedido, Avaliacao

engine = create_engine('sqlite:///exercicios.db')
Session = sessionmaker(bind=engine)
session = Session()

def t01():
    produtos = session.query(Produto).all()
    for p in produtos:
        print(p.valor_estoque)

t01()


def t02():
    for p in session.query(Produto).filter(Produto.valor_estoque > 1000).all():
        print(p.nome)

t02()

def t03():
    