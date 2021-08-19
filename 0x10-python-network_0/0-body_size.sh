#!/bin/bash
# lenght
RETURN=$(curl -s -I http://www.google.com | grep Content-Length | cut -d" " -f2)
echo -n "$RETURN"
