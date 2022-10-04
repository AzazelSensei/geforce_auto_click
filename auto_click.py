import pyautogui
import schedule
import time

pyautogui.FAILSAFE = True

def job():
    for i in range(2):
        pyautogui.moveTo(1600,650,duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(300,300,duration=0.5)

schedule.every(30).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("15:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
