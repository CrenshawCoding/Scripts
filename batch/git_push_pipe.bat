@echo off
set /p files_to_add=Welche Dateien willst du hinzufuegen?:
set /p commit_message=Was ist die commit message?:
git add %files_to_add%
git commit -m "%commit_message%"
git push