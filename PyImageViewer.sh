#!/bin/bash
VAR=$0

DIR=$(dirname "${VAR}")

echo "$DIR"
echo "PWD: $PWD"
echo "0:  $0"
echo $(dirname 0)
echo "1: $1"
python3 $DIR/main.pyw $1
