# P08_videoStreaming

## Ziele
- Das Programm aus P07_rcControll erweitern, damit das Video der Kamera angezeigt auf dem Computer angezeigt wird.
- Kennenlernen von Multithreading
- Bonus: Auf dem Videostream soll die aktuelle Battery angezeigt werden.

## Neue Befehle
- get_battery()
- streamon()
- get_frame_read()
- from time import sleep
- sleep(timeInSeconds)
- from threading import Thread
- Thread(tagret=<TARGET_METHOD>)
- thread.start()
- thread.join()
- import cv2
- cv2.resize(frame, (x,y))
- cv2.imshow(windowname, frame)
- cv2.waitKey(1)
- cv2.rectangle(frame, pt1=(x,y), pt2=(x2y), color=(r,g,b), thickness=t)
