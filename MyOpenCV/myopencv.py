import numpy as np
import cv2


def get__video_from_url(url):
    """Returns a video stream from a Url."""
    import pafy
    return pafy.new(url).getbest()

def opencv_video_capture(video):
    """Make OpenCV stream a video online."""
    video_capture = cv2.VideoCapture(video)

    while True:
        frame = video_capture.read()

        cv2.imshow('VideoCaptureOCV2', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()

opencv_video_capture(get__video_from_url(input('Please enter online video url: ')))
