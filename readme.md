# SiteStream

## Description

The end goal is to mimic the open source, Windows software OBS Studio which allows users to stream content to websites using a custom made linux, server based solution. This solution will allow for an extremely scalable and automable solution with web-based customization controls.

My current design is to use Python + Flask to generate a Motion JPEG livestream using image snapshots. Ffmpeg can then be used to redirect that localhost livestream to Youtube or any other platform.

## Status Reports

### May 6, 2019

Able to successfully generate a localhost mjpeg livestream using Flask with image stills located in a "video" directory

Ffmpeg stream to Youtube kind of works using the command `ffmpeg -re -f mjpeg -framerate 60 -i "http://127.0.0.1:8000/video_feed" -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -acodec aac -ab 128k -strict experimental -s 1280x720 -vcodec h264 -pix_fmt yuv420p -g 10 -vb 700k -preset ultrafast -crf 31 -framerate 60 -f flv "rtmp://a.rtmp.youtube.com/live2/hfqe-md8c-hg11-3hre"`

* Ends abruptly for some reason.
* Requires both audio + video to work (silent track)
* Explore paramaters for possible fix
