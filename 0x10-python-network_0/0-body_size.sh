#!/bin/bash
# lenght asd a sdf
curl -Is "$1" | grep -i "Content-Length" | cut -d" " -f2
