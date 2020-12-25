@echo off
rem // check for parameter to arm the script
set fileType=%1
if "%1"=="" echo enter file type as first param (e.g. mkv)
set param=%2
if not [%param%]==[/y] echo Usage: add /y as 2nd parameter to execute
set baseDir=%CD%

rem // setup the folder for source files
set toDeleteFolderName=toDelete
if not exist %toDeleteFolderName% (
	if not [%param%]==[/y] (echo mkdir "%toDeleteFolderName%") else mkdir "%toDeleteFolderName%"
)

call :treeProcess
goto :eof

:treeProcess
call :MergeIfCorrectNumOfFiles
for /D %%d in (*) do (
	set /A counter=counter+1
	cd %%d
	if not %%d==%toDeleteFolderName% CALL :treeProcess
	cd ..
)
exit /b 0

:MergeIfCorrectNumOfFiles
set /A mkvCounter=0
set /A srtCounter=0
rem // Count .mkv files in directory
for %%f in (*.%fileType%) do (
	set /A mkvCounter=mkvCounter+1)
REM Count .srt files in directory
for %%f in (*.%fileType%) do (
	set /A srtCounter=srtCounter+1)

REM // Merge if there is one mkv and one srt
IF %mkvCounter%==1 (
	IF %srtCounter%==1 (
		setlocal EnableDelayedExpansion
		for %%f in (*.%fileType%) do set mkvFileName=%%f
		for %%f in (*.srt) do set srtFileName=%%f
		call :MergeFiles "!mkvFileName!", "!srtFileName!"
		rem // files would get moved if merge fails call 
		rem // :MoveFiles "!mkvFileName!", "!srtFileName!"
		endlocal
	) else if %mkvCounter% GTR 1 echo there is more than 1 .srt file in %CD% please fix this
) else if %srtCounter% GTR 1 echo there is more than 1 .mkv file in %CD% please fix this
EXIT /B 0

rem // usage: param1: the return value
:SelectMkvFile 
echo There is more than 1 .mkv file in this directory
setlocal EnableDelayedExpansion
set counter=1
for %%f in (*.%fileType%) do (
	set a[!counter!]=%%f
	echo !counter!: %%f
	set /a counter=counter+1
)

echo select the number of the .mkv file that you want to merge
set /p num="Number: "
REM // Check if the number is valid 
if not %num% GEQ 0 (
	echo Error invalid input, select number between 0 and %mkvCounter%
	EXIT /B
)
if not %num% LEQ %mkvCounter% (
	echo Error invalid input, select number between 0 and !mkvCounter!
	EXIT /B
)
echo Selected Mkv File: %a[%num%]%
endlocal
exit /b 0

rem // usage: param1: source mkv file, param2: source srt file
:MergeFiles 
if [%param%]==[/y] (
	"C:\Portable Installations\mkvtoolnix\mkvmerge.exe" -o "%baseDir%\%~1" "%~1" "%~2" --language 0:eng --track-name 0:English
) else echo "C:\Portable Installations\mkvtoolnix\mkvmerge.exe" -o "%baseDir%\%~1" "%~1" "%~2" --language 0:eng --track-name 0:English
exit /b 0

rem // usage: param1: mkv, param2: srt
:MoveFiles 
if [%param%]==[/y] (
	move "%~1" "%baseDir%\%toDeleteFolderName%\%~1"
	move "%~2" "%baseDir%\%toDeleteFolderName%\%~2"
) else (
	echo move "%~1" "%baseDir%\%toDeleteFolderName%\%~1"
	echo move "%~2" "%baseDir%\%toDeleteFolderName%\%~2"
)
exit /b 0