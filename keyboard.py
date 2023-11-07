import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller, Key


cap = cv2.VideoCapture(0)


kb=Controller()
cap.set(3, 1280)
cap.set(4, 720)
finaltext=""
detector = HandDetector(detectionCon=0.8)
keys = [["Q", "w", "E", "R", "T", "Y", "U", "I", "O", "p"], ["A", "S", "D", "F", "G", "H", "J", "K", "L","-"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

def draw(img,buttonlist):
    
    for button in buttonlist:
            
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img,  button.pos, (x+w, y+h), (30, 30, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    4, (255, 255, 255), 4)
    return img

class Button():
    def __init__(self, pos, text, size=(85, 85)):
        self.pos = pos
        self.text = text
        self.size = size




buttonList = []
for i in range(len(keys)):
    
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100*j+50, 100*i+50], key))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)
    
    if hands:
        
        hand1=hands[0]
        
        lmlist=hand1["lmList"]
        bbox1=hand1["bbox"]
        img=draw(img,buttonList)
    
    
        for button in buttonList:
            x,y=button.pos
            w,h=button.size
            if x< lmlist[8][0]<w+x and y<lmlist[8][1]< h+y:
                cv2.rectangle(img,  button.pos, (x+w, y+h), (25,10,150), cv2.FILLED)
                cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    4, (255, 255, 255), 4)
                lenght,_,_=detector.findDistance((lmlist[8][0],lmlist[8][1]),(lmlist[4][0],lmlist[4][1]),img)
                # print(lenght)
                
                if lenght<33:
                    
                    
                    
                    
                    cv2.rectangle(img,  button.pos, (x+w, y+h), (0,255,0), cv2.FILLED)
                    cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    4, (255, 255, 255), 4)
                    
                    if button.text=="-":
                        kb.press(Key.backspace)
                        kb.release(Key.backspace)
                        finaltext=finaltext[:-1]
                        sleep(0.4)
                    else:
                        kb.press(button.text)
                        finaltext+=button.text
                        sleep(0.2)
                    print(finaltext)

    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
