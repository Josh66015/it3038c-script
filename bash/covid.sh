#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
HOSPITALIZED=$(echo $DATA | jq ' .[0].hospitalized')
echo "On $TODAY, there were $POSITIVE positive COVID cases, there were $NEGATIVE negative COVID tests taken, There are still $HOSPITALIZED people still hospitalized, please be sure to get vaccinated and continue to practice CDC guidelines""
