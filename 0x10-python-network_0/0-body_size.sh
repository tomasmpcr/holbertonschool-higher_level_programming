#!/bin/bash
# lenght
RETURN=$(curl -s -I $1 | grep Content-Length | cut -d" " -f2)
echo -n "$RETURN"
