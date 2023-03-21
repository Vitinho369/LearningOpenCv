import cv2 as cv

cap = cv.VideoCapture(0)
codec = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter('out.avi', codec, 20, (640, 480))

while True:

    ok, frame = cap.read()

    if not ok:
        break

    writer.write(frame)
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv.destroyAllWindows()