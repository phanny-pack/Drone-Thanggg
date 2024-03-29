# Note that we will need to install picamera on the Raspberry Pi 
class camera:
    def __init__(self, x, y):
        import picamera
        # Set up the camera
        self.x = x
        self.y = y
        self.c = picamera.PiCamera()
        # possibly able to change the framerate at higher resolution:
        # camera = picamera.PiCamera(resolution=(x, y), framerate=60)
        self.c.resolution = (x, y)
        
        # camera.resolution = (640, 480) # best quality, 60 fps
        # camera.resolution = (1280, 720) # 30 fps
        # camera.resolution = (1920, 1080) # 30 fps        

    """
    Records a video for a given time and saves in file_path
    """
    # Note: moved to a separate function so we can use the threading specifically for recording
    def record_video(self, file_path, time):
        # We can save the video to the sd card by making a directory
        # video_path = '/home/pi/Videos/test_video_480p.h264' # path to directory + name of file
        # video_time = 60 # time we want to record for
        self.c.start_recording(file_path)
        print("camera start")
        self.c.wait_recording(time)
        self.c.stop_recording()
        print("camera done")