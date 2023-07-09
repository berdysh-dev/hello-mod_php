TAG = mod_php

build:
	docker build -f Dockerfile --tag=${TAG} --rm=true .

run:
	docker run -it --rm -p 80:80 -p 443:443 -v /usr/local/GIT/hello-mod_php/htdocs:/usr/local/apache2/htdocs ${TAG}


