#!/bin/bash
# lenght
LEN=$(curl -s -X GET "$1")
echo "$LEN"
