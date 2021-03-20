import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path

import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top=tk.Tk()
top.geometry('500x500')
top.title('Cartoonify any Image !')
top.configure(background='black')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload():
""" opens the filebox to choose image from the device """

    ImagePath=easygui.fileopenbox() # an easy method in easyGUI that returns path as a string
    cartoonify(ImagePath)


