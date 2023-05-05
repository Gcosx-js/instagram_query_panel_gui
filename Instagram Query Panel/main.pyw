from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtWidgets import *
import instaloader
import os
from screen_1_ui import Screen_1_UI_Form
from screen_2_ui import Screen_2_UI_Form
from PyQt5.QtCore import pyqtSignal
from function import *
from PyQt5.QtWidgets import QMessageBox
import requests
import ctypes
import webbrowser
from use_about_screen import About_screen_c

#python -m PyQt5.uic.pyuic -x about-screen-2.ui -o about_screen_ui-2.py
#pyrcc5 about-img.qrc -o about_screen_img.py
def pp_check(username_n):
        try:
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username_n)
            return True
        except instaloader.exceptions.ProfileNotExistsException:
            return False

class Screen_1_class(QWidget):
    username_data = pyqtSignal(str)
    def __init__(self) -> None:
        super().__init__()
        self.s_2_c = Screen_2_class()
        self.screen_1 = Screen_1_UI_Form()
        self.screen_1.setupUi(self)
        self.screen_1.search_button.clicked.connect(self.search)
        self.screen_1.about_button.clicked.connect(self.about)
        self.about_screen_s = About_screen_c()
        self.screen_1.check_button.clicked.connect(self.check)
        self.screen_1.exit_app_button.clicked.connect(self.exit)
    def exit(self):
        QApplication.quit()
    
    def check(self):
        self.username_n = self.screen_1.lineEdit.text()

        if pp_check(self.username_n):
            self.screen_1.status.setStyleSheet('color:green')
            self.screen_1.status.setText('Status : True')
        else:
            self.screen_1.status.setStyleSheet('color:red')
            self.screen_1.status.setText('Status : False')

    

    def about(self):
        self.about_screen_s.show()

    def search(self):
        if self.screen_1.lineEdit.text() != '':
            self.username = self.screen_1.lineEdit.text()
            try:
                pp_down(self.username)
                rename_image(self.username)
                self.s_2_c.start(self.username)
                self.s_2_c.show()
            except Exception as e:
                QMessageBox.about(self,"Error", str(e))

def pp_down(username):
    ig = instaloader.Instaloader()
    return ig.download_profile(username, profile_pic_only=True)
                
def rename_image(username):

    current_dir = os.getcwd()
    image_dir = os.path.join(current_dir, username)

    try:
        for filename in os.listdir(image_dir):
            if filename.endswith('.jpg'):
                os.rename(os.path.join(image_dir, filename), os.path.join(current_dir, f'{username}.jpg'))
                print(f"{filename} renamed to {username}.jpg")
    except:
        print('This problem has passed')

class Screen_2_class(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.s_2 = Screen_2_UI_Form()
        self.s_2.setupUi(self)
        self.profil_fotografi_label = QLabel(self)
        self.profil_fotografi_label.setGeometry(70, 105, 140, 140)
        self.username_al = ''
        self.s_2.pushButton.clicked.connect(self.url)

    def url(self):
        try:
            webbrowser.open(self.beq_deta['profile']['profileurl'])
        except:
            QMessageBox.about(self,"Requests Error", "An error occurred during the request")

    def start(self, username):
        self.username_al = username
        try:
            self.beq_deta = main(username)
            self.follow = self.beq_deta['profile']['followers']
            self.s_2.follow_label.setText(self.follow)
            self.following = self.beq_deta['profile']['following']
            self.s_2.following_label.setText(self.following)
            self.s_2.label_2.setText(username)
            self.s_2.post_label.setText(str(say(username)))
            profil_sekli = QPixmap(f"{username}.jpg")
            dairevi_profil = self.profili_dairevi(profil_sekli, QSize(131, 131))
            self.profil_fotografi_label.setPixmap(dairevi_profil)
        except Exception as e:
            QMessageBox.about(self,"Error", str(e))
        
        

    def profili_dairevi(self, pixmap, boyut):
        yuvarlak_pixmap = QPixmap(boyut)
        yuvarlak_pixmap.fill(Qt.transparent)
        painter = QPainter(yuvarlak_pixmap)

        painter.setPen(Qt.transparent)

        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(pixmap.scaled(boyut, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)))
        painter.drawEllipse(QPoint(boyut.width() // 2, boyut.height() // 2), boyut.width() // 2, boyut.height() // 2)
        painter.end()

        return yuvarlak_pixmap
        

app = QApplication([])
ekran = Screen_1_class()
ekran.show()
app.exec_()
