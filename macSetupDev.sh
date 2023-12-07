# Run me as "source macSetupDev.sh venv_name"
# run with python3.9 because brownie doesn't support other versions of python!
python3.9 -m venv $1
source $1/bin/activate
#pip install --upgrade cx_Freeze
#pip install black-22.10.0-py3-none-any.whl
pip install docker
pip install Gitpython
pip install eth-brownie
pip install psutil
pip install pyyaml
