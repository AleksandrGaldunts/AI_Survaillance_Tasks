import cv2

# fuzzy_logo = cv2.imread("logo.png")
# cv2.imshow("logo",fuzzy_logo)
# if cv2.waitKey()==ord("q"):
#     cv2.destroyAllWindows()
# imgg = cv2.resize(fuzzy_logo,(18,18),cv2.INTER_NEAREST)
# cv2.imshow("imgg",imgg)
# if cv2.waitKey()==ord("q"):
#     cv2.destroyAllWindows()
# print(imgg)
# print(fuzzy_logo)

cola_img = cv2.imread("coca-cola.jpg")
resized = cv2.resize(cola_img,(700,500),cv2.INTER_CUBIC)
#cv2.imshow("Coca-Cola", resized)
# if cv2.waitKey()==ord("q"):
#     cv2.destroyAllWindows()
reversed = resized[:,:,::-1]
cv2.imshow("Coca-Cola", reversed)
if cv2.waitKey()==ord("q"):
    cv2.destroyAllWindows()