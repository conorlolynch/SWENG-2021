#!/bin/bash
if [[ -f "$1" ]]
then
	echo "Deleting file $1"
	rm "$1"
else
	echo "No such file exists"
fi