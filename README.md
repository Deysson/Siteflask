# Site de comunidade em flask e bootstrap na qual se emprega conceitos de login, formularios e banco de dados.
Ele contém os seguintes routes
#home para vizualizar os posts
#contato para as informações de contato
#usuarios para que se possa ver todos os usuários
#login para criar conta e fazer login
#sair para fazer o logout da conta
#perfil para a visualição do perfil do usuário logado
#criar_post para que o usuário possa postar textos
#editar_perfil para que o usuário atualize as informações de perfil, mude a foto do perfil do usuário e atualiza os cursos
#exibir_post para o usário veja o post de forma especifica e caso ele seja o autor ele possa editar o post
#excluir_post para o dono do post possa excluir o post
Na pagina de forms temos
#FormCriarConta para criar conta que contém um def validate_email(self, email) para não haver mais de uma conta para um e-mail
#FormLogin para fazer login
#FormEditarPerfil editar o perfil, adicionar foto e adicionar cursos que contém def validate_email(self, email): para o usuário não possa mudar para um e-mail existente
#FormCriarPost para que o usuário possa criar post
Na pagina models temos
#A class Usuario e a class Post para que se possa trabalhar o banco de dados
