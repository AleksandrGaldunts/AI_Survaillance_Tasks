import cv2
import os
import argparse

parser = argparse.ArgumentParser(description="Capture images with a specified name prefix.")
parser.add_argument("name", type=str, help="The name of the person to capture images for.")
args = parser.parse_args()
person_name = args.name

num_images =10
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

output_folder = "captured_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Press 's' to start capturing images.")

image_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        print("Starting image capture...")

        while image_counter < num_images:
            ret, frame = cap.read()

            if ret:
                image_path = os.path.join(output_folder, f"{person_name}_{image_counter + 1}.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Saved {image_path}")
                image_counter += 1

            cv2.imshow("Webcam", frame)

            cv2.waitKey(500)

        print(f"{num_images} images captured.")
        break

    elif key == ord("q"):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
