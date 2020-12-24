%ECHO OFF
rem // moves files given as param and srt files into seperate directories. One file of type parameter and one of srt is put together.
rem // used to prepare for merging with merge script.
rem // Usage: mergeFiles.bat <file_to_move_ending> 
rem // e.g. mergeFiles.bat mkv moves all srt and mkv files 

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