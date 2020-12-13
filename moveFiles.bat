%ECHO OFF
SETLOCAL EnableDelayedExpansion
set /a counter=1
for %%f in (*.%1) do (
mkdir !counter! 
set /a counter=counter+1
)

set /a counter=1
for %%f in (*.%1) do (
move "%%f" "!counter!\%%f"
set /a counter=counter+1
)

set /a counter=1
for %%f in (*.srt) do (
move "%%f" "!counter!\%%f"
set /a counter=counter+1
)
endlocal