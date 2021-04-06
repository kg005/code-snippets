 PYTHONPATH=$(pwd):$(pwd)/python_tests  pytest python_tests/test_server.tavern.yaml

 PYTHONPATH=$(pwd):$(pwd)/python_tests  pytest --tb=short --tavern-beta-new-traceback -vv python_tests/test_server.tavern.yaml