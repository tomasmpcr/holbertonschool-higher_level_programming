#!/bin/bash
# lenght
LEN=$(curl -X OPTIONS -sI "$1" | grep "Allow:" | cut -d':' -f2)
echo "${LEN##*( )}"
