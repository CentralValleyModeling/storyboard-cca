ECHO off
REM conda activate dev_storyboard_cca
cd src/storyboard_cca
flask run --reload --port 8000
REM conda deactivate
cd ../..
PAUSE