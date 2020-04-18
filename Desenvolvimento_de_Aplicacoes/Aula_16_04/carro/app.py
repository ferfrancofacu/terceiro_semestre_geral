from flask import Flask
from apps.apis import bp

app = Flask('vehicles')

@app.route('/')
def index():
    return "Vehicle MS at your service..."

app.register_blueprint(bp, url_prefix='/vehicles')    

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)