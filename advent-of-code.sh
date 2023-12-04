#!/bin/bash
date=$(date '+%d')
if [ ${date:0:1} = 0 ]
then
    date=${date:1}
fi
year=$(date '+%Y')
echo "Opening day $date of advent of code $year!"
xdg-open https://adventofcode.com/$year/day/"$date"
