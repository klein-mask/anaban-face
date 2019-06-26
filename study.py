import cv2
import os


IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images/'


img = cv2.imread(IMG_DIR + "01.png")



if __name__ == "__main__":
    print(img)

