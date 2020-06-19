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
    
* **Instalar o Virtualenv no Python**

```bash
pip install virtualenv
```

* **Criar o Ambiente Virtual para o Projeto**

  (Ao executar o comando abaixo, irá criar uma pasta oculta dentro do diretório atual chamada **/.venv/**).

  Eu recomendo criar a pasta com esse nome porque esta pasta já está sendo ignorada pelo arquivo .gitignore.

  *Caso deseje colocar outro nome para a pasta virtual, não se esqueça de mudar o arquivo .gitignore .*

  ```bash
  virtualenv .venv
  ```


