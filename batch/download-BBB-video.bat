@echo off
if "%1" == "" (
	echo usage: download-BBB-video.bat "<presentation-url>" "<webcam-url>"
	goto :EOF
) 
if "%2" == "" (
	echo usage: download-BBB-video.bat "<presentation-url>" "<webcam-url>"
	goto :EOF
)
if "%3" == "" (
	echo usage: download-BBB-video.bat "<presentation-url>" "<webcam-url>" "<output-file-name>"
	goto :EOF
)
set curDir = %cd%
youtube-dl -i %1 -o "%curDir%\%3-presentation%~x1"
youtube-dl -i %2 -o "%curDir%\%3-webcam%~x2"
ffmpeg -i "%3-webcam%~x2" "%3-webcam-audio.mp3"
ffmpeg -i "%3-presentation%~x1" -i "%3-webcam-audio.mp3" -c copy "%3.mp4"
del "%3-webcam.webm" "%3-presentation.webm" "%3-webcam-audio.mp3"
pause
exit 0