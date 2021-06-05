import pyautogui
import time
import webbrowser
import subprocess


def sign_in():
    # join class button
    for i in range(10):
        print("Searching for Join Class button", i)
        time.sleep(10)
        join = pyautogui.locateOnScreen('join_class.PNG', confidence=0.9)

        if(join != None):
            pyautogui.moveTo(join)
            pyautogui.click()
            print("Joining Class")

            # switch to zoom button
            print("Searching for Switch to Zoom")
            for j in range(5):
                time.sleep(3)
                switch = pyautogui.locateOnScreen(
                    'switch2.PNG', confidence=0.9)
                if(switch != None):
                    pyautogui.moveTo(switch)
                    pyautogui.click()
                    # print(switch)
                    print('Switching to Zoom', j)
                    time.sleep(20)
                    break
                else:
                    print("Cannot Switch to Zoom")

            # launch zoom button
            # print("Opening zoom")
            # for k in range(5):
            #     launch = pyautogui.locateOnScreen('launch.PNG', confidence=0.9)
            #     time.sleep(5)

            #     if(launch != None):
            #         pyautogui.moveTo(launch)
            #         pyautogui.click()
            #         print('launch zoom')
            #         break
            #     else:
            #         print("Cannot launch zoom")

            # Enable continue button

            print("Searching for Enable recording in zoom")
            for k in range(8):
                time.sleep(3)
                continue_btn = pyautogui.locateOnScreen(
                    'continue.PNG', confidence=0.9)
                if(continue_btn != None):
                    pyautogui.moveTo(continue_btn)
                    pyautogui.click()
                    print('Enabling Recording Continue Button in Zoom', k)
                    break
                else:
                    print("Cannot launch recording continue button in zoom", k)

            # join with audio button
            print("Searching for Enabling Join with Audio Button in Zoom")
            for l in range(5):
                time.sleep(3)
                join_with_audio = pyautogui.locateOnScreen(
                    'join_with_audio.PNG', confidence=0.9)
                if(join_with_audio != None):
                    pyautogui.moveTo(join_with_audio)
                    pyautogui.click()
                    print('Joining with Audio of Zoom', l)
                    break
                else:
                    print("Cannot Joining with Audio of Zoom", l)

            # launch mute in zoom button
            print("Searching for Disabling Mute Button in Zoom")
            for m in range(5):
                time.sleep(2)
                mute = pyautogui.locateOnScreen('mute.PNG', confidence=0.9)
                if(mute != None):
                    pyautogui.moveTo(mute)
                    pyautogui.click()
                    print('Mute Button Clicked', m)
                    date_time = time.strftime("%I:%M %p")
                    print("Current Time is", date_time)
                    print("Waiting 1:00 hr for Class to Finish")
                    time.sleep(3600)
                    break
                else:
                    print("Cannot Mute button in Zoom", m)

            # Finding zoom.exe
            # traverse the software list
            try:
                for h in range(3):
                    Data = subprocess.check_output(
                        ['wmic', 'process', 'list', 'brief'])
                    a = str(Data)
                    # try block
                    #  arrange the string
                    for i in range(len(a)):
                        d = a.split("\\r\\r\\n")[i]
                        flag = 1
                        if"Zoom.exe" in d:
                            flag = 1
                            print("Zoom in Background is Found")
                            date_time = time.strftime("%I:%M %p")
                            print("Current Time is", date_time)
                            print("Waiting 30 min more for Class to Finish")
                            time.sleep(1800)
                            break
                        else:
                            print("Zoom in Background is Not Found")
                            flag = 0
                    if(flag == 1):
                        continue

            except IndexError as e:
                print("All Done", e)

            if(flag == 0):
                webbrowser.open(
                    "https://sagarmatha.student.fuseclassroom.com/live-class/schedule")

        else:
            print('Join Class Not Found')

    if(join == None):
        print('Still Class Not Found, so Waiting for 5 mins')
        time.sleep(300)
    else:
        print("Continue the loop")


# open browser
webbrowser.open(
    "https://sagarmatha.student.fuseclassroom.com/live-class/schedule")

# main body
while(True):
    # print("signing in")
    sign_in()
