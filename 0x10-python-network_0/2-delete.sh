#!/bin/bash
# lenght
LEN=$(curl -s -X "DELETE" "$1")
echo "$LEN"
