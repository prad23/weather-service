#!/bin/sh
echo "Executing Flask run..."
read -p 'Enter environment: ' Env
export FLASK_ENV=$Env
read -p 'Enter application name: ' App
export FLASK_APP=$App
read -p 'Enter port number for application: ' port
echo "Running application on $port"
flask run --port=$port
exit 0