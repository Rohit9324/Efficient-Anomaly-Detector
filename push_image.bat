@echo off

REM Ask for version name (for branch)
set /p VERSION=Enter Version Name (for branch): 

REM Ask for image tag (for commit)
set /p TAG=Enter Image Tag (for commit message): 

C:\Users\rohit\Downloads\Efficient-Anomaly-Detector

REM Create new branch
"C:\Program Files\Git\cmd\git.exe" checkout -b %VERSION%

REM Add files
"C:\Program Files\Git\cmd\git.exe" add .

REM Commit with image tag
"C:\Program Files\Git\cmd\git.exe" commit -m "%TAG% file added"

REM Push branch
"C:\Program Files\Git\cmd\git.exe" push -u origin %VERSION%

pause
