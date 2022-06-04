#    Copyright (C) 2022 IdotMaster1
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This is used for testing, too lazy to write the name everytime. 

# name = 'balls'

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QMainWindow
import sys
from apirequests import *

print("All credit goes to MangaDex (https://mangadex.org)")
name = input('Search any manga author on MangaDex: ')

# QT GUI stuff (Testing)
class DemoWidget(QMainWindow):
    def __init__(self):
        super(DemoWidget, self).__init__()
        # Load the .ui file
        uic.loadUi('mainwindow.ui', self)
        # Show the widget
        self.show()


app = QApplication(sys.argv)
window = DemoWidget()
app.exec_()

print("The author of " + name + " is:")
author(name)

getchapters(name)

wantmangacover = input("Do you want the cover? ")
if wantmangacover == ('y'):
    getcoverart(name)
else:
 wantid = input("Do you want " + name + "'s ID? ")
 if wantid == ('y'):
     getid(name)
 else:
     exit()
