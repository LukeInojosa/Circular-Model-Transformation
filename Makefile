set_env: requirements.txt
	echo "instalando python 3.13.3 ..."
	pyenv install 3.13.3
	echo "criando ambiente virtual..."
	pyenv virtualenv 3.13.3 env
	echo "instalando dependencias..."
	pip install -r requirements.txt
