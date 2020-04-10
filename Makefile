TARGET_ENV?=develop
REPOSITORY:=registry.fiisoft.net
IMAGE:=fiisoft/noti-server
IMAGE_NAME:=$(IMAGE):$(TARGET_ENV)

build:
	echo "$(REPOSITORY)/$(IMAGE_NAME)"
	mkdir -p .build/src
	rsync -a --copy-links ./src/ ./.build/src/
	docker build --build-arg TARGET_ENV=$(TARGET_ENV) -t $(IMAGE_NAME) -f docker/Dockerfile ./
	docker tag $(IMAGE_NAME) $(REPOSITORY)/$(IMAGE_NAME)

docker-push:
	docker push $(REPOSITORY)/$(IMAGE_NAME)

run:
	PYTHONPATH=./src:./lib python -m notification_server
