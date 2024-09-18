#!/bin/bash

# Activate environment
source /env/bin/activate

git_repo_url="https://github.com/$1.git"

# Clone the repo into a subfolder
echo "cloning repo $1"
git clone -b production "$git_repo_url" "code"

# Copy over any databases included in docker image
cp -R database/. code/src/storyboard_cca/storyboard/database

# Change directory to the cloned repository
cd "code/src/storyboard_cca" || exit

# Run app
echo "Running the application..."

flask run --host 0.0.0.0 --port 80