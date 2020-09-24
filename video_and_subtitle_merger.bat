@echo off
if not [%1]==[/y] echo Usage: add /y parameter to execute
set param=%1
set baseDir=%CD%
REM setup the folder for source files
set toDeleteFolderName=toDelete
if not exist %toDeleteFolderName% mkdir %toDeleteFolderName%
call :treeProcess
goto :eof

:treeProcess
for /D %%d in (*) do (
	cd %%d
	if not %%d==%toDeleteFolderName% CALL :treeProcess
	cd ..
)

:MergeIfCorrectNumOfFiles
set /A mkvCounter=0
set /A srtCounter=0
REM Count .mkv files in directory
for %%f in (*.mkv) do (
	set /A mkvCounter=mkvCounter+1)
REM Count .srt files in directory
for %%f in (*.srt) do (
	set /A srtCounter=srtCounter+1)

REM Merge if there is one mkv and one srt
IF %mkvCounter%==1 (
	IF %srtCounter%==1 (
		setlocal EnableDelayedExpansion
		for %%f in (*.mkv) do set mkvFileName=%%~nf
		for %%f in (*.srt) do set srtFileName=%%~nf
		if [%param%]==[/y] (
			"C:\Portable Installations\mkvtoolnix\mkvmerge.exe" -o "%baseDir%\!mkvFileName!" "!mkvFileName!.mkv" "!srtFileName!.srt"
			move ^"!mkvFilename!.mkv^" ^"%baseDir%\%toDeleteFolderName%\!mkvFilename!.mkv^"
			move ^"!srtFilename!.srt^" ^"%baseDir%\%toDeleteFolderName%\!mkvFilename!.srt^"
		) else (
			echo "C:\Portable Installations\mkvtoolnix\mkvmerge.exe" -o "%baseDir%\!mkvFileName!-with-subs.mkv" "!mkvFileName!.mkv" "!srtFileName!.srt"
		)
		endlocal
	)
)
EXIT /B 0

IF NOT %mkvCounter% LEQ 1 (
	echo There is more than 1 .mkv file in this directory
	set counter=1
	for %%f in (*.mkv) do (
		set a[!counter!]=%%f
		echo !counter!: %%f
		set /a counter=counter+1
	)
	echo select the number of the .mkv file that you want to merge
	set /p num="Number: "
	REM Check if the number is valid 
	if not !num! GEQ 0 (
		echo Error invalid input, select number between 0 and !mkvCounter!
		EXIT /B
	)
	if not !num! LEQ !mkvCounter! (
		set /A max=!mkvCounter
		echo Error invalid input, select number between 0 and !mkvCounter!
		EXIT /B
	)
	echo Selected Mkv File: !a[%num%]!
)
EXIT /B