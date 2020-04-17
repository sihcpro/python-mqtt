COMPOSE=docker-compose -f env/$(TARGET_ENV)/docker-compose.yml
IMAGE:=gotecq/notification_mqtt:$(TARGET_ENV)
REPOSITORY:=registry.fiisoft.net
DB_SCHEMA?=
DB_ENV?=local
CURRENT_TIME?=$(shell date '+%Y%m%d_%H%M%S')

build: clean-py-binary
	mkdir -p .build/src
	rsync -a --copy-links ./src/ ./.build/src/
	docker build --build-arg BUILD_ENV=$(TARGET_ENV) -t ${IMAGE} -f img/Dockerfile ./
	docker tag $(IMAGE) $(REPOSITORY)/$(IMAGE)

docker-push:
	docker push $(REPOSITORY)/$(IMAGE)

docker-pull:
	docker pull $(REPOSITORY)/$(IMAGE)

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f

