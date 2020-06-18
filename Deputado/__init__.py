from flask import Flask
from flask import Blueprint
from flask import render_template

#Importando a API do Dados Abertos
from api.scrapy_dadosAbertos import DadosAbertos

#Registrando a rota
DeputadoController = Blueprint('Deputado', __name__)




#Index da rota
@DeputadoController.route('/')
def index():
    
    #Instanciando a Classe de API
    api = DadosAbertos()

    #Retona todos os deputados
    deputados = api.deputados()

    return render_template('Deputado/index.html', deputados=deputados)


@DeputadoController.route('/<int:idDeputado>/')
def infoDeputado(idDeputado):

    #Instanciando a Classe de API
    api = DadosAbertos()

    #Retona todos os dados do deputado pelo seu ID
    deputado = api.deputado_id(idDeputado)

    return render_template('Deputado/infoDeputado.html', infoDeputado=deputado)




@DeputadoController.route('/<int:idDeputado>/Gastos')
def gastos(idDeputado):

    #Instanciando a Classe de API
    api = DadosAbertos()

     #Retona todos os dados do deputado pelo seu ID
    deputado = api.deputado_id(idDeputado)

    #Retorna todos os gastos do deputdo
    gastosDeputado = api.deputado_despesas(idDeputado)

    return render_template("Deputado/gastosDeputado.html", infoDeputado=deputado, GastosDeputado=gastosDeputado)