# Presupuesto

Generador de Presupuesto

## Caracteristicas

* Carga de articulos y precios.
* Editor de articulos y precios.
* Configuración de emisión de presupuestos.
* Gestor de catálogos.

## Instalación

1. git clone <https://github.com/gvizquel/presupuesto.git>
2. cd /presupuesto
3. sudo apt update
4. sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
5. curl <https://pyenv.run> | bash
6. echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
7. echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
8. pyenv update
9. pyenv install 3.8.5
10. pyenv local 3.8.5
11. curl <https://bootstrap.pypa.io/get-pip.py> -o get-pip.py
12. python get-pip.py
13. pip install --upgrade pip
14. pip install pipenv
15. export PIPENV_VENV_IN_PROJECT=".venv"
16. export PIPENV_INSTALL_TIMEOUT=9000
17. ~/.pyenv/versions/3.8.5/bin/pipenv shell
18. ~/.pyenv/versions/3.8.5/bin/pipenv install
19. celery -A ebisuu.celery worker -l info -E
20. ./manage runserver
