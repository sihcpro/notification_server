IMAGE_TAG?=latest


run:
	PYTHONPATH=./src python -m src


test:
	PYTHONPATH=./src python -m src.test

# Docker compose

dc-up:
	cd docker && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose up $(TARGET)

dc-down:
	cd docker && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose down

dc-update:
	cd docker && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose up --detach --build $(TARGET)

dc-build:
	cd docker && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose build $(TARGET)

dc-pull:
	cd docker && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose pull $(TARGET)

dc-push:
	cd docker && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose push $(TARGET)

dc-restart:
	cd docker && \
		make dc-pull dc-down dc-up IMAGE_TAG=${IMAGE_TAG} TARGET=$(TARGET)
