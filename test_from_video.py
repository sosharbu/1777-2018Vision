import cv2
import networktables as nt
from typing import NoReturn

from constants import *
import camera_settings as cs
import vision_utils as vu
import processors.contour_processor


def main() -> NoReturn:
	cap = cv2.VideoCapture("test_videos/test_video.mp4")
	
	rval, _ = cap.read()
	if not rval: raise RuntimeError("rval test failed")
	
	rval = True
	cs.load_settings(SETTINGS_FILE)
	processor = processors.contour_processor.Processor()
	
	print("starting...")
	
	try:
		while rval:
			vu.start_time('reading')
			rval, frame = cap.read()
			if not rval:
				break
			frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)
			vu.end_time('reading')
			data, processed_frame = processor.process(frame, annotate=True)
			# if data != []:
			# 	print data[0].angle
			cv2.imshow('k', processed_frame)
			cv2.waitKey(1)
	except KeyboardInterrupt:
		print("wrapping up!")
		vu.report()
	finally:
		cap.release()


main()

