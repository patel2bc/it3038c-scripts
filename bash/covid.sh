#!/bin/bash
#This script downloads covid data and displays it

#Variables for script 
POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive') 
TODAY=$(date)
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
DEATH=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')
HOSPITALIZED=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalized')
INCHOS=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalizedIncrease')

#Output 
echo "On $TODAY, there were $POSITIVE postive COVID cases, $NEGATIVE negative COVID cases, $DEATH COVID deaths, and $HOSPITALIZED COVID recovered. $INCHOS COVID hospitalization increased."
