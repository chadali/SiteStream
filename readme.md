# SiteStream

## Description

Flask webservice will generate a stream (motion jpeg).

ffmpeg is used to redirect that stream to Youtube


## Status Reports

### May 6, 2019

Mjpeg stream works using image stills located inside video directory.

ffmpeg stream to Youtube kinda works using command `ffmpeg -re -f mjpeg -framerate 60 -i "http://127.0.0.1:8000/video_feed" -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -acodec aac -ab 128k -strict experimental -s 1280x720 -vcodec h264 -pix_fmt yuv420p -g 10 -vb 700k -preset ultrafast -crf 31 -framerate 60 -f flv "rtmp://a.rtmp.youtube.com/live2/hfqe-md8c-hg11-3hre"` but it ends abdrubtly for some reason.

Explore paramaters to find fix. Youtube requires both Video + Audio so silent track is necessary.
