REGION=us-east-1
ACCOUNT_ID=094506541504
REPO_NAME=api-app-test

create-repo:
	aws ecr describe-repositories --repository-names $(REPO_NAME) --region $(REGION) || \
	aws ecr create-repository --repository-name $(REPO_NAME) --region $(REGION)

build:
	docker build --platform linux/amd64 -t $(REPO_NAME) .

login:
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com

tag:
	docker tag $(REPO_NAME):latest $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(REPO_NAME):latest

push:
	docker push $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(REPO_NAME):latest

deploy: create-repo build login tag push

local-test:
	docker build --platform linux/amd64 -t python-app .
	docker run --rm -it \
		-v ~/.aws:/root/.aws:ro \
		-e AWS_PROFILE=default \
		-p 9000:8080 \
		python-app