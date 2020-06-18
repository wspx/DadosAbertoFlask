from flask import Flask
from flask import Blueprint
from flask import render_template

#Importanto a Classe de API
from api.scrapy_dadosAbertos import DadosAbertos

#Registrando a rota
ComparativoController = Blueprint('Comparativo', __name__)



@ComparativoController.route('/')
def index():

    return render_template('Infografico/index.html')




@ComparativoController.route('/Mostrar')
def MostrarGrafico():

    #Dicionario para guardar o total
    totalDeputados = 0
    totalDeputadas = 0

    #Instanciando a classe de API
    api = DadosAbertos()

    #Retornando todos os deputados
    listaDeputados = api.deputados()

    #Percorrendo a lista e pegando as informacoes individuais
    for deputado in listaDeputados:
       
        #Pegando o ID da lista
        idDeputado   = deputado['id']
        nomeDeputado = deputado['nome']

        print("ID: ", str(idDeputado) + " Nome: " + str(nomeDeputado) )
        
        #Retorna todas as informacoes do deputado pelo ID
        infoDeputado = api.deputado_id(idDeputado)

        #Verifica o sexo e acrescenta no contador
        if infoDeputado['sexo'] == 'F':
            totalDeputadas += 1
        else:
            totalDeputados += 1


    return render_template('Infografico/indexGrafico.html', totalDeputadas=totalDeputadas, totalDeputados=totalDeputados)







