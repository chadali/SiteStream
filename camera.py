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

    def __init__(self):
        self.images = [open('video/' + f + '.jpg', 'rb').read() for f in [str(x) for x in range(1, 1318)]]
        if self.thread is None:
            self.last_access = time.time() 
            self.thread = threading.Thread(target=self.myThread)
            self.thread.start()

            while self.get_frame() is None:
                time.sleep(1)

    def get_frame(self):
        self.last_access = time.time()
        
        self.event.wait()
        self.event.clear()

        return self.frame

    def generate_frames(self):
        while True:
            time.sleep(1/60)
            self.index += 1
            if self.index == 1317:
                self.index = 0
            yield self.images[self.index]

    def myThread(self):
        frames_iterator = self.generate_frames()
        for frame in frames_iterator:
            self.frame = frame
            self.event.set()
            time.sleep(0)

            if time.time() - self.last_access > 3:
                self.event.clear()
                frames_iterator.close()
                break

        self.thread = None
