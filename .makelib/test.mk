PYTEST:=PYTHONPATH=./src:./lib pytest
PYTEST_PARAM?= -q -W ignore::DeprecationWarning --html=tests/logs/report.html --self-contained-html


test-api:
	@$(PYTEST) $(PYTEST_PARAM) ./test/**/*.py
