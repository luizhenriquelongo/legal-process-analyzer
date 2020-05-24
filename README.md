# Analisador de Processos Jurídicos
API que analisa via scrapping arquivos html especificos com processos jurídicos

## Tecnologias Utilizadas:
- Python 3.6.9
- Flask 1.1.1

## Instalação:

### Ambiente Linux: 
Para podermos rodar o projeto, precisamos primeiro criar um ambiente virtual para instalar todas as dependências e para isso utiliaremos o virtualenv.

Utilize o seguinte comando para instalar o virtualenv caso não o tenha instalado:

```sudo apt install virtualenv -y```

Com o virtualenv instalado, podemos criar o ambiente virtual e instalar os pacotes. No diretório do projeto utilize o seguinte comando:

```virtualenv -p python3 --clear venv```

Utilize os seguintes comandos para entrar e sair do ambiente virtual:

```
source venv/bin/activate # ativar o ambiente virtual
deactivate 				 # desativar o ambiente virtual

```

Com o ambiente virtual ativo, utilize o comando abaixo para installar as dependencias:

``` pip install -r requirements.txt```

Para o acesso ao banco de dados, o sistema utiliza de duas variáveis de ambiente, para crialas nativamente utilize os comandos:

```bash
    export 'FLASK_APP'='run.py' 
    export 'SECRET'='teste-optimum' 
```

P.S.: Também é possível simular essas variaveis de ambiente em alguns editores de texto ou IDEs.

## Uso:

Para iniciar o servidor, da pasta raiz do projeto, podemos acessar a pasta 'src' e usar o seguinte comando:

```flask run```

Caso este comando não funcione, podemos inicia-lo através do próprio python:

```python run.py```

Desta forma o servidor estará funcionando e disponível para acesso no link: http://127.0.0.1:5000/

## Endpoints

Basta enviar o arquivo via POST para o endpoit utilizando a key 'file': 

- http://127.0.0.1:5000/api/v1/processos/


## To-do:

- Refatorar alguns arquivos;
- Organizar melhor a estrutura de pastas e arquivos;
- Realizar testes unitários;
- Realizar testes dos endpoints;

## Autores:

- [Luiz Henrique Longo](https://www.linkedin.com/in/luizhenriquelongo/)
