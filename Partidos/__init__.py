from flask import Flask
from flask import Blueprint
from flask import render_template

#Importanto a Classe de API
from api.scrapy_dadosAbertos import DadosAbertos


#Registrando a rota
PartidosController = Blueprint('Partidos', __name__)


#Index da Rota
@PartidosController.route('/')
def index():

    #Instanciando a Classe de API
    api = DadosAbertos()

    #Retornado todos os partidos
    partidos = api.partidos()

    return render_template("Partidos/index.html", partidos=partidos)





@PartidosController.route('/<int:idPartido>/Membros')
def MembrosPartido(idPartido):

    #Instanciando a Classe de API
    api = DadosAbertos()

    #Retornado as informacoes do partidos
    partido = api.partido_id(idPartido)

    #Retornado todos as informacaoes do partido
    membros = api.partido_id_membros(idPartido)

    return render_template("Partidos/membros.html", membros=membros, partido=partido)