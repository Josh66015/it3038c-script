#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
HOSPITALIZED=$(echo $DATA | jq ' .[0].hospitalized')
DEATHS=$(echo $DATA | jq ' .[0].death')
echo "On $TODAY, there were $POSITIVE positive COVID cases, there were $NEGATIVE negative COVID tests taken, There are still $HOSPITALIZED people still hospitalized, there have also been $DEATHS people die. Please be sure to get vaccinated and continue to practice CDC guidelines""
