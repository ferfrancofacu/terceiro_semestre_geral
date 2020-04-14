from flask import Flask, render_template, request
app = Flask('app')

@app.route('/')
def index():
    return render_template('index.html')

usuarios = [
    {'login': 'Luna', 'senha': 'azul'},
    {'login': 'Malu', 'senha': 'castanho'}
]

@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html', mensagem=sendParamrnetro())    

@app.route("/form_teste", methods=["PUT", "POST"])

def form_teste():
    login = request.form["login"]
    senha = request.form["password"]

    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("login_ok.html", login = login)
    return render_template("login.html", mensagem = "Login inválido.")


def sendParamrnetro():
    return 'Olá, entre com os seus dados.'

app.run(host='localhost', port=5002, debug=True)