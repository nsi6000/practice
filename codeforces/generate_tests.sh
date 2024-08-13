#!/bin/bash

echo "1"
echo "200000"

for i in {1..200000..1}
do
    echo -n $i
    echo -n " "
done

for i in {1..100000..1}
do
    echo -n "LR"
done
