#!/bin/bash
rm -rf mashup.mp3
python index.py
ffmpeg -i mashup.mp3 -filter_complex movie=videos/${1}.mp4:loop=0,setpts=N/FRAME_RATE/TB -shortest /home/alex/Dropbox/youtube/${2}.mp4
