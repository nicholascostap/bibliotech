# bibliotech

Este projeto foi desenvolvido utilizando a linguagem de programação Python
e integrado com o banco de dados SQL Server.
O software foi projetado para atender as necessidades de uma biblioteca,
onde é possível cadastrar, editar, excluir e pesquisar livros, autores e editoras.

## Tecnologias utilizadas
- Python 3.1X
- PostgreSQL

## Guia de instalação do projeto

1. Clone o repositório
```bash
git clone https://github.com/nicholascostap/bibliotech.git
```

2. Acesse a pasta do projeto no terminal/cmd
```bash
cd bibliotech
```

3. Instale o pacote virtualenv
```bash
pip install virtualenv
```

3.1. Crie um ambiente virtual
```bash
virtualenv venv
```

4. Ative o ambiente virtual
```bash
venv\Scripts\activate
```

4.1. Caso apresente erro ao ativar o ambiente virtual, execute o comando abaixo
```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```

5. Instale as dependências
```bash
pip install -r requirements.txt
```

6. Execute o comando para criar o projeto
```bash
django-admin startproject setup .
```

7. Execute o comando para executar o servidor
```bash
python manage.py runserver
```

8. O servidor será iniciado no endereço //127.0.0.1:8000/

9. Altere os parâmetros no arquivo settings.py para configurar o timezone e o fuso horário
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True
```

10. 

