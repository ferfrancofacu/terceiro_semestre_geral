# importando dependencias
from flask import Flask
from apps import vehicle_blueprint

# criando aplicativo flask, usando seu construtor padrao
app = Flask('vehicles')

# definindo rota padrão para o app (única rota fora de blueprints)
@app.route('/')
def index():
    return "Vehicle MS at your service..."

# registrando blueprint (vehicles)
app.register_blueprint(vehicle_blueprint, url_prefix='/vehicles')


app.url_map.strict_slashes = False
print(app.url_map)
# se o executavel for main, entao roda o flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
