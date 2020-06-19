# DadosAbertoFlask

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Generic badge](https://img.shields.io/badge/Github-Clodonil-<COLOR>.svg)](https://github.com/clodonil)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Using-Flask-<COLOR>.svg)](https://palletsprojects.com/p/flask/)

***
### Breve Descrição

Este é um pequeno projeto Web que utilizan o Microframework Flask para manipula a API dos Dados Aberto da Câmara dos Deputados, e traz os dados em uma página web.

### Agradecimento

Gostaria de agradecer o [Professor Clodonil Trigo](https://github.com/clodonil) por ter apresentado a linguagem Python e o Microframework Flask. 

Todo o conteudo visto e implementado dentro deste projeto, teve como base o repositório [Python-Fundamentals](https://github.com/clodonil/Python-Fundamentals) do [Professor Clodonil Trigo](https://github.com/clodonil)

***

![screenshot](static/screenshot.png)

***

### Observações

*Para executar este projeto, primeiramente deve-se ter o **Python** devidamente instalado na máquina, de preferencia a **Versão 3**.*

*Após feito a instalção, faça o clone deste projeto para a tua máquina.*

```Bash
git clone https://github.com/wspx/DadosAbertosFlask.git
```

*Depois de clonar abra o teu terminal padrão do seu sistema e siga os passos abaixo.*

***

## Instação e Execução

1. **Abra a pasta onde este projeto foi clonado**

```bash
cd DadosAbertosFlask
```

2. **Instalar e Criar um Ambiente Virtual do Python**

   Criar um ambiente virtual ajuda a não poluir o teu Python com um monte de biblioteca de vários projetos no projeto atual.

   Desse modo, o projeto terá apenas as bibliotecas necessárias para o projeto ser executado.   
    
* ***Instalar o Virtualenv no Python***

```bash
pip install virtualenv
```

* ***Criar o Ambiente Virtual para o Projeto***

  (Ao executar o comando abaixo, irá criar uma pasta oculta dentro do diretório atual chamada **/.venv/**).

  Eu recomendo criar a pasta com esse nome porque esta pasta já está sendo ignorada pelo arquivo .gitignore.

  *Caso deseje colocar outro nome para a pasta virtual, não se esqueça de mudar o arquivo .gitignore .*

```bash
virtualenv .venv
```

3. **Ativar e Desativar o Ambiente Virtual**

   Para ativar o ambiente virtual, basta digitar o comando abaxio de acordo com o teu Sistema Operacional.
   
###### Windows

```bat
.venv\Scripts\activate.bat
```
   
###### Linux e MacOS

```bash
source .venv/bin/activate
```
   
###### Para desativar o Ambiente Virutal em ambos os sistemas.
   
```bash
deactivate
```

4. **Instalar as Dependências do Projeto**

   Todas as dependências deste projeto estão listadas no arquivo [*requirements.txt*](https://github.com/wspx/DadosAbertoFlask/blob/master/requirements.txt).
   
   Para instalar todas elas de uma vez, basta seguir o comando abaixo:
   
   ###### *NÃO ESQUEÇA QUE O AMBIENTE VIRTUAL DEVE ESTAR ATIVO!*
   
```bash
pip install -r requirements.txt
```   
   
5. **Executar o Projeto**

   Após feitos todos os passos anteriores, basta digitar o comando abaixo iniciar o Servidor Web do Flask:
   
   ###### *NÃO ESQUEÇA QUE O AMBIENTE VIRTUALDEVE ESTAR ATIVO!*
   
```bash
python app.py
``` 

6. **Extras**
   
   Ao executar pela primeira vez a aplicação, ela está configurado para sempre ser acessível apenas no *localhost ou 127.0.0.1* da porta *8080*.
   
   Contudo, é possivel acessar essa aplicação Flask através de qualquer outro dispositipo na tua rede local.
   
   Para isso, basta fazer as seguintes alterrações no arquivo [app.py](https://github.com/wspx/DadosAbertoFlask/blob/master/app.py) na ultima linha do arquivo pelo trecho abaixo:
   
```python
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)
``` 



#### E com isso, está documentação se encerra!
