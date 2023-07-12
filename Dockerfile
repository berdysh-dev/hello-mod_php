FROM berdyshdev2/docker_alpine_apache_php

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

COPY php.ini /usr/local/lib

COPY entry.sh /usr/local/bin/entry.sh


CMD ["sh","/usr/local/bin/entry.sh"]




