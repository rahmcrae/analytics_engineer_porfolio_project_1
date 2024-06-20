local-run:
	docker build --platform linux/amd64 -t python-app .
	docker run --rm -it \
		-v ~/.aws:/root/.aws:ro \
		-e AWS_PROFILE=default \
		-p 9000:8080 \
		python-app