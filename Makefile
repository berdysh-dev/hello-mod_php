TAG = mod_php

all: build run

build:
	docker build -f Dockerfile --tag=${TAG} --rm=true .

run:
	docker run -it --rm -p 80:80 -p 443:443 -v /etc:/usr/local/etc -v /usr/local/GIT/hello-mod_php/htdocs:/usr/local/apache2/htdocs ${TAG}


