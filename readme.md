# SiteStream

## Description

The end goal is to remake features of the open source GUI program OBS Studio. OBS allows for users to stream their desktops, video recorders, audio, etc. with huge amounts of customization. A growing feature of OBS is streaming HTML content from other websites (live subscriber count numbers for youtube channel). My goal is to make a linux based, serverside solution where users can achieve the same end-goal through a website based solution and pain-free hosting. Such a solution would be extremely scalable and automable, with good stream stability/reliability. 

My current design is to use Python + Flask to generate a Motion JPEG livestream using image snapshots. Ffmpeg can then be used to redirect that localhost livestream to Youtube or any other platform.

## Running

`gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 app:app`

## Status Reports

### May 5, 2019

Able to successfully generate a localhost mjpeg livestream using Flask with image stills located in a "video" directory

Ffmpeg stream to Youtube kind of works using the command `ffmpeg -re -f mjpeg -framerate 60 -i "http://127.0.0.1:8000/video_feed" -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -acodec aac -ab 128k -strict experimental -s 1280x720 -vcodec h264 -pix_fmt yuv420p -g 10 -vb 700k -preset ultrafast -crf 31 -framerate 60 -f flv "rtmp://a.rtmp.youtube.com/live2/{stream key}"`

* Ends abruptly for some reason.
* Requires both audio + video to work (silent track)
* Explore paramaters for possible fix

### May 6, 2019

* The above command does actually work. I believe stream was going offline because my personal connection was cutton off for a bit and ffmpeg isn't able to recover.
* In the future a job needs to continously scan Youtube for stream health and restart ffmpeg if it goes offline.
* Research the most optimized way of retrieving jpg screenshots of a website
* Research how to stream audio, possibly from Youtube itself using youtube-dl package
* Research what all the ffmpeg command arguments are doing actually
* Research why flask debug/production environment is bad and the purpose of GUnicorn + Gevent 

### May 8, 2019

Big thanks to [Miguel](https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited/page/0) for the template

* Learned how Python works with OOP, fixed so that only one background thread runs for multiple clients.
* Gunicorn is just a better production tool.
* Gevent allows by defaults thousands of threads. Miguel added time.sleep(0) to allow for it, not sure how it works.
* Need to fix ffmpeg stream getting stuck at a certain frame. Again, study parameters and maybe add reconnect parameters.
* Prototype of webpage to jpg to stream works. What I really need to do is start a headless chrome/firefox browser which generates the frames.


### May 9, 2019

* Launching a headless firefox instance, and spamming screenshots does currently work.
* It takes a huge amount of CPU usage which NEEDS to be solved. 
* High fps is only possible with a tiny resolution, which is fine for my intended purposes.

### May 10, 2019

* Added new route to test driver window resizing
* I guess we can continue, CPU is going to be a problem no matter what so I'll have to limit FPS ~15-20
* Two customizable size drivers both generate frames. PIL library is used to combine frames into a final frame which ffmpeg streams.
* End result will not be pretty, will not be smooth, will not be practical.
