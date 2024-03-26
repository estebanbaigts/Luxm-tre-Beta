import cv2
import time

KNOWN_DISTANCE = 50
KNOWN_FACE_WIDTH = 14.5
focal_length = None

def calculate_distance(face_width):
    return (KNOWN_FACE_WIDTH * focal_length) / face_width

def screen_and_measure_brightness():
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    resolution = width * height
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    global focal_length
    while True:
        start_time = time.time() 
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mean_brightness = int(gray.mean())
        text_brightness = f"Mean brightness: {mean_brightness}"
        cv2.putText(frame, text_brightness, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        quality_percentage = int((resolution / (1920 * 1080)) * 100)
        text_quality = f"Camera quality: {quality_percentage}%"
        cv2.putText(frame, text_quality, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_width = w
            
            if focal_length is None:
                focal_length = (face_width * KNOWN_DISTANCE) / KNOWN_FACE_WIDTH
            distance = calculate_distance(face_width)
            text_distance = f"Distance: {distance:.2f} cm"
            cv2.putText(frame, text_distance, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.putText(frame, "FPS: {}".format(int(1 / (time.time() - start_time))), (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Capture Image', frame)
        cv2.waitKey(max(1, int(1000 / 100 - (time.time() - start_time) * 1000)))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

screen_and_measure_brightness()
