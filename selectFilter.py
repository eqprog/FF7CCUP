from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os


class selectFilter():

	def __init__(self, root):

		self.root=root
		self.splash_img = ImageTk.PhotoImage(Image.open("evaluator.png"))

		self.splashFrame = Frame(self.root, width = 960)
		self.splashFrame.pack(side=LEFT, anchor=N)
		self.splash_label=Label(self.splashFrame, image=self.splash_img)
		self.splash_label.pack(side=TOP, anchor=CENTER)

