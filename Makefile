
VERSION := 0.0.2

requirements.txt:
	uv export --format requirements-txt > requirements.txt

build: requirements.txt
	docker build -t mocchi/sample-prometheus-app:$(VERSION) .

push: build
	docker push mocchi/sample-prometheus-app:$(VERSION)

run:
	docker run -it -p 5000:5000 mocchi/sample-prometheus-app:0.0.1

