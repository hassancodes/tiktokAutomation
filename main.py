import pyautogui
import time
import random

# time.sleep(5)
# pyautogui.press("down")
def uparrow():
    time.sleep(5)
    pyautogui.press("up")

def downarrow():
    time.sleep(5)
    pyautogui.press("Down")


def like():
    time.sleep(5)
    # pyautogui.press("l")
    start = pyautogui.locateCenterOnScreen('liked.png')#If the file is not a png file it will not work
    # print(start)
    if start:
        print("already Liked")
    else:
        print("Bot liked")
        pyautogui.press("l")

# like()
commentlist = ["🏆🏆🏆", "king 👑", "Drop it 🔥" ,
                "Wow " , "Dope" , "💪💪" ,"👍👍","Fireeee" , "My man👑" ,
                "❤️❤️❤️" ,"Hell yeah" , "Lets goooooo ❤️‍🔥❤️‍🔥" ,
                "Wooo" , "Dope af" , "crazy af 💞",
                "won my heard", "Bro drop this asap",
                "Sad for those who havnt yet discovered this music",
                "Sin the best", "God level", "💪💪" , "🙏🙏🙏", "Weeeew 🙂" ,
                "Greateeee", "Real Barz" ,"Rap Gold", "This is some real ..." ,
                "Holly Molly"]



def writeComment():
    int  = random.randint(0,len(commentlist)-1)
    # print(int,":" ,commentlist[int])
    comment = commentlist[int]
    time.sleep(4)
    commentarea = pyautogui.locateCenterOnScreen("realcomment.png")
    pyautogui.moveTo(commentarea)
    print(commentarea)

    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.typewrite(comment)
    pyautogui.press("enter")
    print("entered")

    # to get out of the comment section.

# change over here
# we can fetch the video count somehow. and store it in totalVideos Variable.
totalVideos = 53
def mainup():
    counter =0
    Up =True
    while Up:
        counter +=1
        if counter<totalVideos:
            uparrow()
        else:
            print("No More Up")
            up = False
            maindown()

def maindown():
    counter =0
    Down =True
    while Down:
        counter +=1
        like()
        # writeComment()
        # time.sleep(1)
        # pyautogui.press("tab")
        if counter<totalVideos:
            downarrow()
        else:
            print("No More down")
            mainup()
            Down = False

maindown()
