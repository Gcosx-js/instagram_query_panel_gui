
from PyQt5 import QtCore, QtGui, QtWidgets


class Screen_1_UI_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1435, 808)
        Form.setStyleSheet("#Form{\n"
"    \n"
"    background-color: rgb(1, 1, 1);\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, -70, 761, 391))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("image: url(:/newPrefix/Capture.JPG);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Capture.JPG"))
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 690, 301, 101))
        self.label_2.setStyleSheet("image: url(:/newPrefix/border.JPG);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/border.JPG"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.exit_app_button = QtWidgets.QPushButton(Form)
        self.exit_app_button.setGeometry(QtCore.QRect(90, 720, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.exit_app_button.setFont(font)
        self.exit_app_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_app_button.setStyleSheet("QPushButton{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    \n"
"    color: rgb(235, 113, 239);\n"
"}")
        self.exit_app_button.setObjectName("exit_app_button")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 580, 301, 101))
        self.label_3.setStyleSheet("image: url(:/newPrefix/border.JPG);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/border.JPG"))
        self.label_3.setScaledContents(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.about_button = QtWidgets.QPushButton(Form)
        self.about_button.setGeometry(QtCore.QRect(90, 610, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.about_button.setFont(font)
        self.about_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_button.setStyleSheet("QPushButton{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    \n"
"    color: rgb(235, 113, 239);\n"
"}")
        self.about_button.setObjectName("about_button")
        self.search_button = QtWidgets.QPushButton(Form)
        self.search_button.setGeometry(QtCore.QRect(640, 540, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setStyleSheet("QPushButton{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    color: rgb(164, 221, 188);\n"
"}")
        self.search_button.setObjectName("search_button")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(570, 510, 301, 111))
        self.label_4.setStyleSheet("image: url(:/newPrefix/border-2.JPG);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/border-2.JPG"))
        self.label_4.setScaledContents(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(440, 380, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:4px solid transparent;\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:white;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(22)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("Instagram username...")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(570, 620, 301, 111))
        self.label_5.setStyleSheet("image: url(:/newPrefix/border-2.JPG);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/border-2.JPG"))
        self.label_5.setScaledContents(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName("label_5")
        self.check_button = QtWidgets.QPushButton(Form)
        self.check_button.setGeometry(QtCore.QRect(630, 650, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.check_button.setFont(font)
        self.check_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_button.setStyleSheet("QPushButton{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px solid transparent;\n"
"    border-radius:13px;\n"
"    \n"
"    color: rgb(164, 221, 188);\n"
"}")
        self.check_button.setObjectName("check_button")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(400, 340, 671, 141))
        self.label_6.setStyleSheet("image: url(:/newPrefix/border.JPG);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/border.JPG"))
        self.label_6.setScaledContents(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_6.setObjectName("label_6")
        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("color: rgb(255, 255, 127);")
        self.status.setObjectName("status")
        self.label_6.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.exit_app_button.raise_()
        self.label_3.raise_()
        self.about_button.raise_()
        self.search_button.raise_()
        self.lineEdit.raise_()
        self.label_5.raise_()
        self.check_button.raise_()
        self.status.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exit_app_button.setText(_translate("Form", "EXIT APP"))
        self.about_button.setText(_translate("Form", "ABOUT"))
        self.search_button.setText(_translate("Form", "SEARCH "))
        self.check_button.setText(_translate("Form", "CHECK"))
        self.status.setText(_translate("Form", "Status : None"))
import screen_1_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Screen_1_UI_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
