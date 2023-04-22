# Run me as source init.sh venv_name
python3 -m venv $1
source $1/bin/activate
pip install --upgrade cx_Freeze
pip install black-22.10.0-py3-none-any.whl
pip install docker
pip install Gitpython
pip install eth-brownie
