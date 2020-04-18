from flask import Flask, render_template
from apps.alunos.api import bp as bp_alunos
from apps.professores.api import bp as bp_professores
from apps.disciplinas.api import bp as bp_disciplinas

app = Flask('app')

app.register_blueprint(bp_alunos, url_prefix='/alunos')

app.register_blueprint(bp_professores, url_prefix='/professores')

app.register_blueprint(bp_disciplinas, url_prefix='/disciplinas')

app.run(host='localhost', port=8080, debug=True)