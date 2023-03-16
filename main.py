from flask import Flask, render_template,url_for
from forms import FormCriarConta,FormLogin

app = Flask(__name__)
app.config['SECRET_KEY']='70a9057405ab5f5967323c7686bbc6ab'

lista_de_usuarios=['alcoolemmim', 'cego', 'loko']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_de_usuarios=lista_de_usuarios)


@app.route('/login')
def login():
    form_login =FormLogin()
    form_criarconta =FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)



if __name__=='__main__':
    app.run(debug=True)