import cv2

img = cv2.imread("solar-system.jpg")

text_show1 = "Sun"
text_show2 = "Mercury"
text_show3 = "Venus"
text_show4 = "Earth"
text_show5 = "Mars"
text_show6 = "Jupiter"
text_show7 = "Saturn"
text_show8 = "Uranus"
text_show9 = "Neptune"
cv2.putText(img,
            text_show1,
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show2,
            (110,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show3,
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show4,
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show5,
            (385,175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show6,
            (550,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show7,
            (765,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show8,
            (965,125),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))
cv2.putText(img,
            text_show9,
            (1105,125),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            color=(255,255,255))

cv2.imshow("output",img)

cv2.waitKey(0)