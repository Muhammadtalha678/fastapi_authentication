#!/bin/bash

# 1. Update package lists and install necessary utilities
apt-get update
apt-get install -y unixodbc-dev apt-transport-https gnupg2

# 2. Add the Microsoft ODBC Driver Repository (using Debian 11/Bullseye as a known compatible base)
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# 3. Install the ODBC Driver 17
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17

# 4. Start your application (replace the line below with your actual startup command)
# Your Fastapi/Uvicorn startup command, as used in your previous Dockerfile:
uvicorn main:app --host 0.0.0.0 --port 8000