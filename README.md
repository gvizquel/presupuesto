# Presupuesto

Generador de Presupuesto

## Caracteristicas

* Carga de articulos y precios.
* Editor de articulos y precios.
* Configuración de emisión de presupuestos.
* Gestor de catálogos.

## Instalación

01. git clone <https://github.com/gvizquel/presupuesto.git>
02. cd /presupuesto
03. sudo apt update
04. sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
05. curl <https://pyenv.run> | bash
06. echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
07. echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
08. pyenv update
09. pyenv install 3.8.5
10. pyenv local 3.8.5
11. curl <https://bootstrap.pypa.io/get-pip.py> -o get-pip.py
12. python get-pip.py
13. pip install --upgrade pip
14. pip install pipenv
15. export PIPENV_VENV_IN_PROJECT=".venv"
16. export PIPENV_INSTALL_TIMEOUT=9000
17. pipenv shell
18. pipenv install
19. celery -A ebisuu.celery worker -l info -E
20. ./manage runserver
