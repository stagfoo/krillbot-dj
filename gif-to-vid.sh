#!/bin/bash
rm -rf tmp/gif.mp4;
rm -rf tmp/gif-scale.mp4;
ffmpeg -i ${1} -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" tmp/gif.mp4;
ffmpeg -i tmp/gif.mp4 -vf scale=1920:1080 tmp/gif-scale.mp4;
ffmpeg -i tmp/gif-scale.mp4 -i logo.png -filter_complex "overlay=0:0" ${2}
