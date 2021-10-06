#setup for converting to exe by py2exe - old
import pygame
pygame.init()
from distutils.core import setup
import py2exe
import os

setup(console=[r"C:\Users\Mariusz\Desktop\Projects\Python\SimpleCipher\Data\SimpleCipher-Decipher.py"])
os.system(r'pause')