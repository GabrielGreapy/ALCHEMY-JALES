from sqlalchemy import create_engine, func, distinct, exists, and_, or_
from sqlalchemy.orm import sessionmaker, joinedload
from models import Base, Usuario, Produto, Pedido, Avaliacao

# Conexão e criação de sessão
engine = create_engine('sqlite:///exercicios.db')
Session = sessionmaker(bind=engine)
session = Session()

#1 Liste todos os produtos cadastrados no sistema.
def q01():
    produtos = session.query(Produto).all()
    for p in produtos:
        print(p.nome, p.preco)

#2 Recupere todos os usuários ativos com mais de 18 anos.
def q02():
    usuarios = session.query(Usuario).filter(Usuario.ativo == True, Usuario.idade > 18).all()
    for u in usuarios:
        print(u.nome, u.idade)

# =3. Obtenha todos os pedidos feitos depois de 01/03/2025 com quantidade superior a 5.
def q03():
    pedidos = session.query(Pedido).filter(Pedido.data_pedido > '2025-03-01', Pedido.quantidade > 5).all()
    for p in pedidos:
        print(p.id, p.quantidade, p.data_pedido)

# 4. Encontr o primeiro usuario cadastrado no sistema.
def q04():
    usuario = session.query(Usuario).first()
    if usuario:
        print(usuario.nome, usuario.email)

# 5. Verifique qual é o produto mais barato da categoria "eletrônicos".
def q05():
    produto = session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco).first()
    if produto:
        print(produto.nome, produto.preco)

# 6. Determine o último pedido realizado por qualquer usuário.
def q06():
    pedido = session.query(Pedido).order_by(Pedido.data_pedido.desc()).first()
    if pedido:
        print(pedido.id, pedido.data_pedido)

# 7. Recupere os dados completos do usuário com ID 7.
def q07():
    usuario = session.query(Usuario).get(7)
    if usuario:
        print(usuario.nome, usuario.email, usuario.idade)

# 8. Verifique se existe um produto com ID 5 e estoque positivo.
def q08():
    produto = session.query(Produto).filter(Produto.id == 5, Produto.estoque > 0).first()
    if produto:
        print(produto.nome, produto.estoque)

# 9. Obtenha o pedido de ID 3 junto com os dados do usuário associado.
def q09():
    pedido = session.query(Pedido).join(Usuario).filter(Pedido.id == 3).first()
    if pedido:
        print(pedido.id, pedido.usuario.nome, pedido.usuario.email)

# 10. Encontre usuários com idade entre 25 e 35 anos.
def q10():
    usuarios = session.query(Usuario).filter(Usuario.idade.between(25, 35)).all()
    for u in usuarios:
        print(u.nome, u.idade)

# 11. Liste pedidos com status "cancelado" ou "pendente" feitos depois de 2024.
def q11():
    pedidos = session.query(Pedido).filter(Pedido.status.in_(['cancelado', 'pendente']), Pedido.data_pedido > '2024-01-01').all()
    for p in pedidos:
        print(p.id, p.status, p.data_pedido)

# 12. Selecione produtos com preço acima de R$ 500 que tiveram pelo menos 1 pedido.
def q12():
    produtos = session.query(Produto).join(Pedido).filter(Produto.preco > 500).distinct().all()
    for p in produtos:
        print(p.nome, p.preco)

# 13. Busque todos os usuários com status inativo.
def q13():
    usuarios = session.query(Usuario).filter(Usuario.ativo == False).all()
    for u in usuarios:
        print(u.nome, u.idade)

# 14. Encontre produtos da categoria "livros" com preço inferior a R$ 100.
def q14():
    produtos = session.query(Produto).filter(Produto.categoria == 'livros', Produto.preco < 100).all()
    for p in produtos:
        print(p.nome, p.preco)

# 15. Obtenha os 3 produtos mais caros com estoque disponível.
def q15():
    produtos = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco.desc()).limit(3).all()
    for p in produtos:
        print(p.nome, p.preco)

# 16. Liste todos os usuários em ordem alfabética de nome.
def q16():
    usuarios = session.query(Usuario).order_by(Usuario.nome).all()
    for u in usuarios:
        print(u.nome)

# 17. Ordene os produtos do mais caro para o mais barato.
def q17():
    produtos = session.query(Produto).order_by(Produto.preco.desc()).all()
    for p in produtos:
        print(p.nome, p.preco)

# 18. Organize os pedidos por data de criação (mais recentes primeiro) e depois por status.
def q18():
    pedidos = session.query(Pedido).order_by(Pedido.data_pedido.desc(), Pedido.status).all()
    for p in pedidos:
        print(p.id, p.status, p.data_pedido)

# 19. Liste os 10 primeiros usuários cadastrados no sistema.
def q19():
    usuarios = session.query(Usuario).limit(10).all()
    for u in usuarios:
        print(u.nome, u.email)

# 20. Obtenha os 5 produtos mais baratos disponíveis no estoque.
def q20():
    produtos = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco).limit(5).all()
    for p in produtos:
        print(p.nome, p.preco)

# 21. Selecione os 3 pedidos mais recentes feitos por usuários com idade maior que 30 anos.
def q21():
    pedidos = session.query(Pedido).join(Usuario).filter(Usuario.idade > 30).order_by(Pedido.data_pedido.desc()).limit(3).all()
    for p in pedidos:
        print(p.id, p.data_pedido, p.usuario.nome)

# 22. Liste os usuários cadastrados, ignorando os 5 primeiros resultados.
def q22():
    usuarios = session.query(Usuario).offset(5).all()
    for u in usuarios:
        print(u.nome)

# 23. Obtenha os produtos mais caros, pulando os 3 primeiros resultados na ordenação por preço.
def q23():
    produtos = session.query(Produto).order_by(Produto.preco.desc()).offset(3).all()
    for p in produtos:
        print(p.nome, p.preco)

# 24. Liste os pedidos realizados, ignorando os 8 primeiros, mas ordenados pela data de criação de forma decrescente.
def q24():
    pedidos = session.query(Pedido).order_by(Pedido.data_pedido.desc()).offset(8).all()
    for p in pedidos:
        print(p.id, p.data_pedido)

# 25. Conte quantos usuários estão cadastrados no sistema.
def q25():
    count = session.query(Usuario).count()
    print(count)

# 26. Determine o número de pedidos realizados com status "entregue".
def q26():
    count = session.query(Pedido).filter(Pedido.status == 'entregue').count()
    print(count)

# 27. Conte quantos produtos existem na categoria "eletrônicos" com estoque maior que 0 e preço acima de R$ 100,00.
def q27():
    count = session.query(Produto).filter(Produto.categoria == 'eletrônicos', Produto.estoque > 0, Produto.preco > 100).count()
    print(count)

# 28. Liste todas as categorias únicas de produtos disponíveis no sistema.
def q28():
    categorias = session.query(distinct(Produto.categoria)).all()
    for c in categorias:
        print(c[0])

# 29. Identifique as idades únicas dos usuários cadastrados no banco de dados.
def q29():
    idades = session.query(distinct(Usuario.idade)).all()
    for idade in idades:
        print(idade[0])

# 30. Obtenha todos os status únicos dos pedidos realizados por usuários ativos com mais de 25 anos de idade.
def q30():
    status = session.query(distinct(Pedido.status)).join(Usuario).filter(Usuario.ativo == True, Usuario.idade > 25).all()
    for s in status:
        print(s[0])

# 31. Liste o nome dos usuários e os IDs dos pedidos que eles realizaram.
def q31():
    resultados = session.query(Usuario.nome, Pedido.id).join(Pedido).all()
    for r in resultados:
        print(r[0], r[1])

# 32. Obtenha o nome dos produtos e a quantidade comprada em cada pedido realizado por um usuário específico chamado "João".
def q32():
    pedidos = session.query(Produto.nome, Pedido.quantidade).join(Pedido).join(Usuario).filter(Usuario.nome == 'João').all()
    for p in pedidos:
        print(p[0], p[1])

# 33. Liste todos os usuários que fizeram pedidos de produtos da categoria "livros", incluindo o nome do produto e a quantidade comprada em cada pedido.
def q33():
    resultados = session.query(Usuario.nome, Produto.nome, Pedido.quantidade).join(Pedido).join(Produto).filter(Produto.categoria == 'livros').all()
    for r in resultados:
        print(r[0], r[1], r[2])

# As funções de exists(), add_columns(), group_by(), having() e outras podem ser feitas de maneira similar.
q01()
q02()
q03()
q04()
q05()
q06()
q07()
q08()
q09()
q10()
q11()
q12()
q13()
q14()
q15()
q16()
q17()
q18()
q19()
q20()
q21()
q22()
q23()
q24()
q25()
q26()
q27()
q28()
q29()
q30()
q31()
q32()
q33()