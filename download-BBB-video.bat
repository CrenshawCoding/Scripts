@echo off
if "%~1" == "" (
	echo usage: download-BBB-video.bat "<presentation-url>" "<webcam-url>"
	goto :EOF
) 
if "%~2" == "" (
	echo usage: download-BBB-video.bat "<presentation-url>" "<webcam-url>"
	goto :EOF
)
set curDir = %cd%
youtube-dl -i %1 -o "%curDir%\presentation%~x1"
youtube-dl -i %2 -o "%curDir%\webcam%~x2"
ffmpeg -i "webcam%~x2" "webcam-audio.mp3"
ffmpeg -i "presentation%~x1" -i "webcam-audio.mp3" "output.mp4"
pause
exit 0