import cv2

def activate_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Jarvis Vision', frame)
        # Sohail bhai, yahan AI model lage ga jo cheezon ko pehchanay ga
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
