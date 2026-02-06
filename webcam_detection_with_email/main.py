import cv2

import mail


from news_api.send_email import send_email

video = cv2.VideoCapture(0)
first_frame = None
status_list = []
while True:
    status = 0

    check , frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow("My video", frame)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)


    thresh_frame = cv2.threshold(delta_frame, 65, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)


    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("My video", thresh_frame)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y ,w, h = cv2.boundingRect(contour)
        rect = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0),3)

        if rect.any():
            status = 1

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] ==1 and status_list[1] == 0:
        mail.send_mail()


    cv2.imshow("My video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
print(frame)