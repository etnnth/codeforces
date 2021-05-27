DOCKER_RUN = docker run --rm --user $$(id -u)\:$$(id -g)
VOLUMES = -v $(CURDIR):/raifml



main.zip: main.py team.py model.py model.hdf5
	$(DOCKER_RUN) $(VOLUMES) raifml ./test.sh
	$(RM) main.zip
	zip -r main.zip main.py team.py model.py model.hdf5

model.hdf5: train.csv train.py model.py team.py
	$(DOCKER_RUN) $(VOLUMES) raifml python3 train.py

build:
	docker build --rm -t raifml .

sh: 
	$(DOCKER_RUN) $(VOLUMES) -it --entrypoint sh raifml

clean:
	$(RM) model.hdf5
	$(RM) __pycache__ -r

