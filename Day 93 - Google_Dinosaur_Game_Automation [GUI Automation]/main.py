import pyautogui
from PIL import ImageGrab
from time import sleep

def click(key):
    pyautogui.keyDown(key)
    return

if __name__ == "__main__":
    sleep(3)
    click('space')
    
def handle_collision(data):
    # Look for cactuses:
    for i in range(710, 800):
        for j in range(455, 495):
            if data[i, j] < 100:
                click("down")
                return
    # Look for birds:
    for i in range(710, 760):
        for j in range(410, 445):
            if data[i, j] < 150:
                click("space")
                return
    return

while True:
    screen = ImageGrab.grab().convert('L')   
    data = screen.load()
    handle_collision(data)