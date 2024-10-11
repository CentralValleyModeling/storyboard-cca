#!/bin/bash
# Activate environment
source /env/bin/activate
# clone github repo
git clone -b production --depth 1 "$1" "code"
# Copy over any databases included in docker image
mkdir code/src/storyboard_cca/storyboard/database
cp -R database/. code/src/storyboard_cca/storyboard/database
# Change directory to the cloned repository
cd "code/src/storyboard_cca" || exit
# Run app
echo "Running the application..."
flask run --host 0.0.0.0 --port 80