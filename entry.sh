#! /bin/sh

export TZ=JST-9

/usr/local/apache2/bin/apachectl start

while test true
do
    date
    sleep 60
done


