# Note that we will need to install picamera on the Raspberry Pi 
import picamera

# Set up the camera
camera = picamera.PiCamera()
camera.resolution = ()

# Record and save video
# We can save the video to the sd card by making a directory
video_path = # path to directory + name of file
video_time = # time we want to record for
camera.start_recording(video_path)
camera.wait_recording(video_time)
camera.stop_recording()