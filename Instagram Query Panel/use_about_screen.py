from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtWidgets import *
from about_screen_ui import Ui_Form
import webbrowser




class About_screen_c(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.about_c = Ui_Form()
        self.about_c.setupUi(self)
        self.about_c.github_butotn.clicked.connect(self.github)
        self.about_c.instagram_button.clicked.connect(self.instagram)
        self.about_c.twitter_button.clicked.connect(self.twitter)
    
    def github(self):
        webbrowser.open('https://github.com/Gcosx-js')
    
    def instagram(self):
        webbrowser.open('https://www.instagram.com/gcosx.js/')
    
    def twitter(self):
        webbrowser.open('https://twitter.com/gcosx_js')