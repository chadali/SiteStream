import time
import threading

class CameraEvent(object):
    def __init__(self):
        self.event = threading.Event()

    def wait(self):
        return self.event.wait()

    def set(self):
        if not self.event.isSet():
            self.event.set()

    def clear(self):
        self.event.clear()

class Camera():
    frame = None
    last_access = 0
    index = 0
    thread = None
    event = CameraEvent()
    images = [open('video/' + f + '.jpg', 'rb').read() for f in [str(x) for x in range(1, 1318)]]

    def __init__(self):
        if Camera.thread is None:
            print("Starting background thread")
            Camera.last_access = time.time() 
            Camera.thread = threading.Thread(target=self.myThread)
            Camera.thread.start()

            while self.get_frame() is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        
        Camera.event.wait()
        Camera.event.clear()

        return Camera.frame

    @staticmethod
    def generate_frames():
        while True:
            time.sleep(1/60)
            Camera.index += 1
            if Camera.index == 1317:
                Camera.index = 0
            yield Camera.images[Camera.index]

    @classmethod
    def myThread(cls):
        frames_iterator = cls.generate_frames()
        for frame in frames_iterator:
            Camera.frame = frame
            Camera.event.set()
            time.sleep(0)

            if time.time() - Camera.last_access > 5:
                print("Stop thread due to inactivity")
                Camera.event.clear()
                frames_iterator.close()
                break

        Camera.thread = None
