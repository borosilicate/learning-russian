#!/bin/sh

for i in $(ls pictures/)
do
  ls pictures/$i/ | nl | sed 's/[0-9]//g' | tr _ ' ' | sed 's/.jpeg//g' | sed 's/.jpg//g' > CSVs/$i.csv
done