from flask import Flask, flash, Response, redirect, render_template, request, session, abort
from camera import Camera

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html') 

@app.route('/adjust')
def adjustSize():
    height = request.args.get('height')
    width = request.args.get('width')
    return Camera(False).adjustSize(width, height)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera(True)),
    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True) 
