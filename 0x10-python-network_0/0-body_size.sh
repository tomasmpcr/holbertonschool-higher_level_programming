#!/bin/bash
# lenght
LEN=$(curl -so /dev/null "$1" -w '%{size_download}')
echo "$LEN"
