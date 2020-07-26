#count frames
from imutils.video import count_frames
import argparse
import os
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video ", required=True,
	help="path to input video file")
ap.add_argument("-o", "--override", type=int, default=-1,
	help="whether to force manual frame count")
args = vars(ap.parse_args())


override = False if args["override"] < 0 else True
total = count_frames(args["video"], override=override)
print("[INFO] {:,} total frames read from {}".format(total,
	args["video"][args["video"].rfind(os.path.sep) + 1:]))

#generating barcode
import argparse
import json
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", required=True,
	help="path to input video")
ap.add_argument("-o", "--output D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", required=True,
	help="path to output JSON file containing frame averages")
ap.add_argument("-s", "--skip D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", type=int, default=0,
	help="# of frames to skip (to create shorter barcodes)")
args = vars(ap.parse_args())

avgs = []
total = 0

print("[INFO] looping over frames in video (this will take awhile)...")
video = cv2.VideoCapture(args["video"])

while True:
	(grabbed, frame) = video.read()
 
	if not grabbed:
		break

	total += 1

	if args["skip"] == 0 or total % args["skip"] == 0:
		avg = cv2.mean(frame)[:3]
		avgs.append(avg)

video.release()
print("[INFO] saving frame averages..

#visualize barcode
import numpy as np
import argparse
import json
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--avgs D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", required=True,
	help="path to averages JSON file")
ap.add_argument("-b", "--barcode D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", required=True,
	help="path to output barcode visualization image")
ap.add_argument("-t", "--height D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", type=int, default=250,
	help="height of output barcode image")
ap.add_argument("-w", "--barcode-width D:\Summer 2020\AI theory\MRS Project\movie-barcode\videos\jurassic_park_trailer.mp4", type=int, default=1,
	help="width of each bar in output image")
args = vars(ap.parse_args())
avgs = json.loads(open(args["avgs"]).read())
avgs = np.array(avgs, dtype="int")

bw = args["barcode_width"]
barcode = np.zeros((args["height"], len(avgs) * bw, 3),
	dtype="uint8")

for (i, avg) in enumerate(avgs):
	cv2.rectangle(barcode, (i * bw, 0), ((i + 1) * bw,
		args["height"]), avg, -1)
cv2.imwrite(args["barcode"], barcode)
cv2.imshow("Barcode", barcode)
cv2.waitKey(0)

