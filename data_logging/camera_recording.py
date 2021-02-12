# Note that we will need to install picamera on the Raspberry Pi 
class camera:
    def __init__(self, x, y):
        import picamera

        # Set up the camera
        self.x = x
        self.y = y
        camera = picamera.PiCamera()
        camera.resolution = (x, y)
        # camera.resolution = (640, 480) # best quality, 60 fps
        # camera.resolution = (1280, 720) # 30 fps
        # camera.resolution = (1920, 1080) # 30 fps

        # Record and save video
        # We can save the video to the sd card by making a directory
        video_path = '/home/pi/Videos/test_video_480p.h264' # path to directory + name of file
        video_time = 60 # time we want to record for
        camera.start_recording(video_path)
        print("camera start")
        camera.wait_recording(video_time)
        camera.stop_recording()
        print("camera done")