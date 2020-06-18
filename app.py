from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import jsonify


#Importando modulos de Controller
from Deputado    import DeputadoController
from Partidos    import PartidosController
from Comparativo import ComparativoController

app = Flask(__name__)

#Registrando as rotas
app.register_blueprint(DeputadoController, url_prefix='/Deputados')
app.register_blueprint(PartidosController, url_prefix='/Partidos')
app.register_blueprint(ComparativoController, url_prefix='/Comparativo')



#Rota Inical
@app.route("/")
@app.route("/index.html")
def hello():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=8080)