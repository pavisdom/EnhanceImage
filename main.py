# This is a sample Python script.
import os
import re
from time import sleep

from cutout import CutoutProClient
from email_service import TempMail

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



cutout = CutoutProClient()
folder= 'C:\\Users\\pavit\\Downloads\\t\\p'
for f in [os.path.join(folder,f) for f in os.listdir(folder)]:
    cutout.image_enhance(f)