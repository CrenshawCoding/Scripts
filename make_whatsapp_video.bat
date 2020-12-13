rem // converts a video into a format thats sendable by whatsapp
rem // usage: make_whatsapp_video.bat <video_to_convert>
ffmpeg -i %1 -c:v libx264 -profile:v baseline -level 3.0 -pix_fmt yuv420p %~n1_converted.mp4