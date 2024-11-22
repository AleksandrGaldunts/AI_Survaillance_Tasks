import cv2

src = cv2.imread("threshold.png", cv2.IMREAD_GRAYSCALE);

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY);
cv2.imwrite("opencv-threshold-example.jpg", dst);

th, dst = cv2.threshold(src, 0, 128, cv2.THRESH_BINARY);
cv2.imwrite("opencv-thresh-binary-maxval.jpg", dst);

th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY);
cv2.imwrite("opencv-thresh-binary.jpg", dst);

th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY_INV);
cv2.imwrite("opencv-thresh-binary-inv.jpg", dst);

th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TRUNC);
cv2.imwrite("opencv-thresh-trunc.jpg", dst);

th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO);
cv2.imwrite("opencv-thresh-tozero.jpg", dst);

th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO_INV);
cv2.imwrite("opencv-thresh-to-zero-inv.jpg", dst);