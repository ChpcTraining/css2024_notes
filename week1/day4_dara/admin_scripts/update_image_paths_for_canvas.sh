#!/bin/bash

path_to_file=$1

sed "s/.\\/images/https\\:\\/\\/raw.githubusercontent.com\\/ChpcTraining\\/css2024\\_notes\\/main\\/week1\\/day4\\_dara\\/images/g" $path_to_file
