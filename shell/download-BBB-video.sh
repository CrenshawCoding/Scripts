#!/bin/bash

youtube-dl -i $1 -o "presentation.webm"
youtube-dl -i $2 -o "webcam.webm"
ffmpeg -i "webcam.webm" "webcam-audio.mp3"
ffmpeg -i "presentation.webm" -i "webcam-audio.mp3" -c:v copy -c:a aac "output.mp4"
rm webcam.webm presentation.webm webcam-audio.mp3