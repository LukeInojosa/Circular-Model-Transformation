# Circular-Model-Transformation

# Pyenv Use:

	1. pyenv install 3 (instala versão 3 do python)
	2. pyenv virtualenv 3 env (cria ambiente virtual com versão python 3 e nome venv)
	3. pyenv local env (estabelece versão local do python = env)
	4. pyevn activate (ativa ambiente)
	5. pip freeze > requirements.txt (guarda versões das bibliotecas instaladas em arquivo .txt)
	6. source deactivate (desativa ambiente virtual)

# Como rodar o projeto:

	1. Instale pyenv e pyenv-virtualenv

# Execute uma única vez: 

	1. pyenv install 3.13.3 (instala versão python)
	2. pyenv virtualenv 3.13.3 env (cria ambiente virtual com versão instalada)
	3. pyenv activate ou pyenv activate [nome do ambiente] (ativa ambiente virtual)
	4. pip install -r requirements.txt (instala dependências)

	alternativa rode o Makefile : make set_env
#  Execute
	1.python -m src
