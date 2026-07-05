import cv2
from fer import FER

detector = FER()

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotion
    result = detector.top_emotion(frame)
    if result:
        emotion, score = result
        print(f"Emotion: {emotion}, Score: {score}")

    cv2.imshow('JeevanNet - Emotion Detector', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
