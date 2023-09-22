# Fetching the latest node image on alpine linux
FROM node:16-alpine


# Setting up the work directory
WORKDIR /frontend

# Installing dependencies
COPY ./package.json ./

# Install project dependencies
RUN npm install

# Copying all the files in our project
COPY . .
