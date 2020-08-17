# Presupuesto

Generador de Presupuesto

## Caracteristicas

* Carga de articulos y precios.
* Editor de articulos y precios.
* Configuración de emisión de presupuestos.
* Gestor de catálogos.

## Instalación

1. git clone https://github.com/gvizquel/presupuesto.git
2. cd /presupuesto
3. sudo apt update
4. sudo apt install -y build-essential libssl-devzlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wgetcurl llvm libncurses5-dev libncursesw5-dev xz-utilstk-dev libffi-dev liblzma-dev python-openssl git
5. curl https://pyenv.run | bash
6. pyenv update
7. pyenv install 3.8.5
8. pyenv local 3.8.5
9. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
10. python get-pip.py
11. pip install --upgrade pip
12. pip install pipenv
13. export PIPENV_VENV_IN_PROJECT=".venv"
14. export PIPENV_INSTALL_TIMEOUT=9000
15. ~/.pyenv/versions/3.8.5/bin/pipenv shell
16. ~/.pyenv/versions/3.8.5/bin/pipenv install
17. useradd -d /var/www/new_user  new_user
18. pipenv shell
19. ./manage runserver
