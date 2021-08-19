#!/bin/bash
# lenght sdf dsf 
curl -X OPTIONS -sI "$1" | grep "Allow:" | cut -c8-
