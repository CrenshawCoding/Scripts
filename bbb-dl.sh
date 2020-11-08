#!/bin/bash

# This script downloads BBB stream (only works with screen share by the teacher) and merges it with the audio file
#
# I n s t a l l a t i o n
#
# 1. Install requirements:
#    "sudo apt install python3 python3-pip ffmpeg"
# 2. Install youtube-dl from https://yt-dl.org/ or via python:
#    "sudo pip3 install --upgrade youtube_dl"
# 3. Save this script to "/usr/local/bin/bbb-dl"
# 4. Make it executable:
#    "sudo chmod a+rx /usr/local/bin/bbb-dl"
#
# U s a g e
#
# Run this script with "bbb-dl <presentation-url> <webcam-url>"
# e.g. "bbb-dl https://lb.bbb.uni-due.de/presentation/<ID>/deskshare/deskshare.webm https://lb.bbb.uni-due.de/presentation/<ID>/video/webcams.webm"

# Check non-zero arguments
if [[ -z $1 || -z $2 ]]; then
  echo "Usage: bbb-dl <presentation-url> <webcam-url>"
  exit 1
fi

# Extract file extension from stream url
presentationRaw="presentation.${1##*.}"
webcamRaw="webcam.${2##*.}"

# Download the streams
youtube-dl "$1" -o "$presentationRaw"
youtube-dl "$2" -o "$webcamRaw"

# Convert the MP3 raw webcam output into an audio file
rm "webcam-audio.mp3"
ffmpeg -i "$webcamRaw" "webcam-audio.mp3"

# Merge the files
rm "output.mp4"
ffmpeg -i "$presentationRaw" -i "webcam-audio.mp3" "output.mp4"

# Delete raw output files
rm "$presentationRaw"
rm "$webcamRaw"
rm "webcam-audio.mp3"

exit 0