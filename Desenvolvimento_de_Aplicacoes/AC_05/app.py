from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def index():
    return "Inicio do sistema"

#app.register_blueprint(, url_prefix='/')

app.url_map.strict_slashes = False
print(app.url_map)

app.run(host='localhost', port=8080, debug=True)
