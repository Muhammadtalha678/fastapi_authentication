#!/bin/bash

# 1. Update package lists and install necessary utilities
apt-get update
apt-get install -y unixodbc-dev apt-transport-https gnupg2

# 2. Add the Microsoft ODBC Driver Repository (using Debian 11/Bullseye)
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# 3. Install the ODBC Driver 17
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17

# DO NOT put the uvicorn command here. We will run it separately.