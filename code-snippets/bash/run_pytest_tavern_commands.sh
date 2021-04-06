# start local server using flask
export FLASK_APP=server.py
flask run



# run tests and get status of checks
tavern-ci test_server.tavern.yaml
echo $?

# or just common pytest call
pytest

# when using custom functions need to have folder with tests in python path, '-vv' each test separte line, '--tb=short' short traceback
PYTHONPATH=$(pwd):$(PWD)/test  pytest -vv --tb=short



