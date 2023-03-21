import cv2 as cv

cap = cv.VideoCapture(0) #index 0 corresponde a webcam local da máquina

n = 0

while True:
    ok, frame = cap.read()# flag que infroma se conseguimos ler o video, o próprio frame que ler o vídeo

    if not ok:
        break

    n = n + 1

    cv.putText(frame, f"Frames: {n}", (100,200), cv.FONT_ITALIC, 1, (255,0,0), cv.LINE_4)
    cv.imshow('Video', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break