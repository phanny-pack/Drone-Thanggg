# Note that we will need to install picamera on the Raspberry Pi 
import picamera

# Set up the camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)

# Record and save video
# We can save the video to the sd card by making a directory
video_path = '/home/pi/Videos/test_video_480.h264' # path to directory + name of file
video_time = 10 # time we want to record for
camera.start_recording(video_path)
print("camera start")
camera.wait_recording(video_time)
camera.stop_recording()
print("camera done")