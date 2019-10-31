pip install -r requirements.txt --user --upgrade
set -o allexport
. ./.env.default
. ./.env
set +o allexport
python setup.py develop
app