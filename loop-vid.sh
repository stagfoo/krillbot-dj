#!/bin/bash

ffmpeg -f concat -i gif.txt -c copy videos/${1}

