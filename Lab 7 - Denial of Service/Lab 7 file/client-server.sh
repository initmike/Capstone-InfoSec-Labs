#!/bin/bash

#traffic between client and server
for ((x=1; x<1000000; x++)); do
    curl -o index.html http://5.6.7.8
    sleep 1
done
~          
