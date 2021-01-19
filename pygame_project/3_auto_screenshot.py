import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1,11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2)