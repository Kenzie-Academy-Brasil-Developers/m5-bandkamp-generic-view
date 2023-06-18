# M5 - BandKamp Generic View

## Introdução

- Na empresa em que você trabalha, o líder de tecnologia solicitou que você acesse um projeto antigo, no qual os usuários poderiam se cadastrar, cadastrar álbuns e músicas. Esse projeto foi desenvolvido com Django, utilizando APIView, Serializer e SQLite3. Ele deseja que você faça uma refatoração, aplicando os conceitos de Generic View, Model Serializer e alterando o banco de dados para o PostgreSQL.

## Requisitos

### Entregáveis

Link deste repositório no GitHub;

- [Github Repo](https://github.com/toledomg/m5-bandkamp-generic-view-toledomg)

- [Link Deploy](https://google.com)

Link do repositório do GitHub, forkado deste template.

- [Github Template](https://github.com/Kenzie-Academy-Brasil-Developers/m5-bandkamp-generic-view)

##

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:

```shell
pip install pytest-testdox pytest-django
```

4. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:

```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:

```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de albums:

```python
pytest --testdox -vvs tests/albums/
```

- Rodando testes de songs:

```python
pytest --testdox -vvs tests/songs/
```

## Comandos Úteis

Abrir Shell nativo Django

```shell
python manage.py shell
```

Instalar Django

```shell
pip install django
```

Instalar Django Rest Framework

```shell
pip install djangorestframework
```

Inicializar Projeto Django

```shell
django-admin startproject nome_do_projeto
```

Inicializar App Django

```shell
python manage.py startapp nome_do_app
```

Salvar requirements

```shell
pip freeze > requirements.txt
```

Instalar requirements

```shell
pip install -r requirements.txt
```

Criar Migrations

```shell
python manage.py makemigrations
```

Rodar Migrations

```shell
python manage.py migrate
```

Server Start

```shell
python manage.py runserver
```
