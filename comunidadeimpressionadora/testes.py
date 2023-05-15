#from comunidadeimpressionadora import app, database
#with app.app_context():
#    database.drop_all()
#    database.create_all()
# criando um usuario
# with app.app_context():
    #usuario=Usuario(username='lira',email='lira@gmail.com', senha='123456')
#   database.session.add(usuario)
#   database.session.comit()

# Requisitando uma informação de usuario
# with app.app_context():
#   meus_usuarios= Usuario.query.all() [(query.filter.by(id=1)).first() para pegar um valor especifico]
#   print(meus_usuarios)
#   print(meus_usuarios.username)

# criando um post
#with app.app_context():
#   meu_post= Post(id=1,titulo='Primeiro post do Lira',corpo="lira voando")
#   database.session.add(meu_post)
#   database.session.comit()

#pesquisando um post
# with app.app_context():
#   post= Post.query.all()
#   print(post.titulo)
#   print(post.autor.email)