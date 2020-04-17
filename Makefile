MAKELIB=.makelib
TARGET_ENV?=local
CONFIG_FILE:=env/$(TARGET_ENV)/config.ini
PYTHON:=FII_APP_CONFIG_FILE=$(CONFIG_FILE) PYTHONPATH=./src:./lib python

include $(MAKELIB)/ops.mk
include $(MAKELIB)/test.mk
include $(MAKELIB)/chore.mk

install:
	pip install -r requirements.txt

run:
	@$(PYTHON) -m notification_mqtt

run-connect:
	@$(PYTHON) src/notification_mqtt/connect.py
