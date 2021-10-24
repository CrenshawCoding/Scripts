@echo off
if "%1" == "" (
	echo usage: compress_video_ffmpeg.bat "<video_to_compress>"
	goto :EOF
) 
set original = %1
ffmpeg -i %1 -vcodec h264 -acodec mp2 %~n1_compressed.mp4
exit 0