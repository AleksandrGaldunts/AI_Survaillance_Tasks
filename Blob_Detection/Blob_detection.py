import cv2
import numpy as np

im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)

detector_default = cv2.SimpleBlobDetector_create()

keypoints_default = detector_default.detect(im)

im_with_keypoints_default = cv2.drawKeypoints(
    im, keypoints_default, np.array([]), (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.imshow("Blobs with Default Parameters", im_with_keypoints_default)
cv2.imwrite("blobs_default.jpg", im_with_keypoints_default)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200
params.filterByArea = True
params.minArea = 500
params.filterByCircularity = True
params.minCircularity = 0.1
params.filterByConvexity = True
params.minConvexity = 0.87
params.filterByInertia = True
params.minInertiaRatio = 0.01

detector_custom = cv2.SimpleBlobDetector_create(params)

keypoints_custom = detector_custom.detect(im)

im_with_keypoints_custom = cv2.drawKeypoints(
    im, keypoints_custom, np.array([]), (0, 255, 0),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.imshow("Blobs with Custom Parameters", im_with_keypoints_custom)
cv2.imwrite("blobs_custom.jpg", im_with_keypoints_custom)

cv2.waitKey(0)
cv2.destroyAllWindows()
