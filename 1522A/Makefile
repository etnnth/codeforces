DOCKER_RUN = docker run --rm --user $$(id -u)\:$$(id -g)
VOLUMES = -v $(CURDIR):/raifml

build:
	docker build --rm -t raifml .

fish: 
	$(DOCKER_RUN) $(VOLUMES) -it --entrypoint fish raifml


