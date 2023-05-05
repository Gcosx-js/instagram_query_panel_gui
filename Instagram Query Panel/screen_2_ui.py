

from PyQt5 import QtCore, QtGui, QtWidgets


class Screen_2_UI_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(623, 834)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 70, 641, 611))
        self.label.setStyleSheet("image: url(:/newPrefix/screen-2.JPG);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/screen-2.JPG"))
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 140, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.follow_label = QtWidgets.QLabel(Form)
        self.follow_label.setGeometry(QtCore.QRect(300, 290, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(24)
        self.follow_label.setFont(font)
        self.follow_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.follow_label.setObjectName("follow_label")
        self.following_label = QtWidgets.QLabel(Form)
        self.following_label.setGeometry(QtCore.QRect(370, 370, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(24)
        self.following_label.setFont(font)
        self.following_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.following_label.setObjectName("following_label")
        self.post_label = QtWidgets.QLabel(Form)
        self.post_label.setGeometry(QtCore.QRect(230, 450, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(24)
        self.post_label.setFont(font)
        self.post_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.post_label.setObjectName("post_label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 540, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton,\n"
"QPushButton:focus,\n"
"QPushButton:focus {\n"
"  background-color: black;\n"
"  border: 1px solid white;\n"
"  color: white;\n"
"  padding: 3px 20px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:hover:focus {\n"
"  background-color: #2196f3;\n"
"  border-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:pressed:focus {\n"
"  background-color: #f50057;\n"
"  border: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  color: #cccccc;\n"
"  background-color: #cccccc;\n"
"  border: none;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Username"))
        self.follow_label.setText(_translate("Form", "1234"))
        self.following_label.setText(_translate("Form", "1234"))
        self.post_label.setText(_translate("Form", "1234"))
        self.pushButton.setText(_translate("Form", "URL"))
import screen_2_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Screen_2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
