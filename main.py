import cv2 as cv
import tensorflow as tf
import numpy as np
from playsound import playsound
import threading


def alarm():
    print("*****************ALARM********************")
    playsound('static/fire_alarm.mp3')


# Load saved model
model = tf.keras.models.load_model('static/mobile_model.h5')


def prepare_image(image):
    image = cv.resize(image, (224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("error opening camera")
    exit()
itr = 0

# Create thread for alarm
t1 = threading.Thread(target=alarm, args=())
while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    # if frame is read correctly ret is True
    if not ret:
        print("error in retrieving frame")
        break
    img = frame
    cv.imshow('Frame', img)

    preprocessed_image = prepare_image(img)
    predictions = model.predict(preprocessed_image)
    print("Fire :", str(predictions[0][0] * 100)[:4] + "%", " | Not Fire:", str(predictions[0][1] * 100)[:4] + "%")
    labels = (predictions > 0.5).astype(int)
    if labels[0][0] == 1:
        itr += 1
        print("Fire detected")
        if itr == 3:
            # Alarm
            t1.start()
    else:
        print("No Fire detected")
    print("\n\n")

    if cv.waitKey(1) == ord('q'):
        cam.release()
        cv.destroyAllWindows()
        if t1.is_alive():
            t1.join()
        break
