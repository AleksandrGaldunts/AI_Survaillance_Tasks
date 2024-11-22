# # import cv2
# # import matplotlib.pyplot as plt
# #
# # img = cv2.imread("logo.png")
# # dimensions = img.shape
# # print(dimensions)
# # print(img.size)
# # print(img.dtype)
# # # cv2.imshow("logo",img)
# # # cv2.waitKey()
# #
# # # for x in range(1,300):
# # #     for y in range(0,487):
# # #         img[x,y] = (255, 255,255)
# # #
# #
# # # i = img[200, 40]
# # # print(i)
# # #top_left = img[0:50, 0:50]
# # #img[6, 40] = (0,0,255)
# # #cv2.imshow("logo",img)
# # # cv2.waitKey()
# #
# #
# # ######################
# #
# # # b,g,r = cv2.split(img)
# # # img_matplotlib = cv2.merge([r,g,b])
# # #
# # #
# # # plt.subplot(121)
# # # plt.imshow(img)
# # # plt.subplot(122)
# # # plt.imshow(img_matplotlib)
# # # plt.show()
# #
# #
# #
# #
# import cv2
# vid_capture = cv2.VideoCapture('image.mp4')
# if (vid_capture.isOpened() == False):
#     print("Error opening the video file")
# else:
#     fps = vid_capture.get(5)
#     print('Frames per second : ', fps, 'FPS')
#
#     frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
#     print('Frame count : ', frame_count)
#
#     frame_width = vid_capture.get(3)
#     print("frame width", frame_width)
#
# while (vid_capture.isOpened()):
#     ret, frame = vid_capture.read()
#     if ret == True:
#         cv2.imshow('Frame', frame)
#         key = cv2.waitKey(20)
#
#         if key == ord('q'):
#             break
#     else:
#         break
#
# vid_capture.release()
# cv2.destroyAllWindows()