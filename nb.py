import cv2
import pytesseract
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Function to perform license plate detection and OCR
def detect_and_ocr_plate(image, count):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect license plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            # Crop the detected plate region
            img_roi = gray[y:y + h, x:x + w]

            # Preprocess the plate image
            img_roi = cv2.resize(img_roi, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            img_roi = cv2.equalizeHist(img_roi)

            # Set a custom Tesseract configuration
            custom_config = '--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

            # Use Tesseract OCR with the custom configuration
            detected_text = pytesseract.image_to_string(img_roi, config=custom_config).strip()

            if len(detected_text) == 10:  # Check if the detected text has exactly 10 characters
                print("Detected License Plate:", detected_text)

                # Save the detected text to a text file
                file_path = os.path.join("Resources", "detected_plate_numbers.txt")
                with open(file_path, "a") as file:
                    file.write("Licence Number: " + detected_text + "\n")

                # Display "Number Plate detected" on the image
                cv2.putText(image, "Number Plate detected", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # Save the image
                img_path = os.path.join("Resources", "plate_img", "scanned_img_" + str(count) + ".jpg")
                cv2.imwrite(img_path, img_roi)
                print("Image saved:", img_path)
                count += 1

    return count

# Path to the Haar Cascade XML file for license plate detection
harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

min_area = 500  # Minimum area of plate wxh

# Create a "Resources" directory if it doesn't exist
if not os.path.exists("Resources"):
    os.mkdir("Resources")
    os.mkdir("Resources/plate_img")

reading_plate = False  # State variable to control reading
count = 0  # Initialize count

while True:
    success, img = cap.read()

    # Initialize the plate cascade classifier
    plate_cascade = cv2.CascadeClassifier(harcascade)

    if not reading_plate:
        count = detect_and_ocr_plate(img, count)

    cv2.imshow("Result:", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') or key == ord('S'):
        reading_plate = False
    elif key == ord('q') or key == ord('Q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
