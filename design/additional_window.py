# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additional_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_additional_window(object):
    def setupUi(self, additional_window):
        additional_window.setObjectName("additional_window")
        additional_window.resize(480, 480)
        self.note_title_line = QtWidgets.QLineEdit(additional_window)
        self.note_title_line.setGeometry(QtCore.QRect(10, 40, 461, 28))
        self.note_title_line.setAutoFillBackground(True)
        self.note_title_line.setObjectName("note_title_line")
        self.note_title_label = QtWidgets.QLabel(additional_window)
        self.note_title_label.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.note_title_label.setFont(font)
        self.note_title_label.setObjectName("note_title_label")
        self.note_text_label = QtWidgets.QLabel(additional_window)
        self.note_text_label.setGeometry(QtCore.QRect(10, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.note_text_label.setFont(font)
        self.note_text_label.setObjectName("note_text_label")
        self.note_content_text = QtWidgets.QTextEdit(additional_window)
        self.note_content_text.setGeometry(QtCore.QRect(10, 110, 461, 361))
        self.note_content_text.setObjectName("note_content_text")

        self.retranslateUi(additional_window)
        QtCore.QMetaObject.connectSlotsByName(additional_window)

    def retranslateUi(self, additional_window):
        _translate = QtCore.QCoreApplication.translate
        additional_window.setWindowTitle(_translate("additional_window", "Добавить заметку"))
        self.note_title_label.setText(_translate("additional_window", "Заголовок заметки"))
        self.note_text_label.setText(_translate("additional_window", "Текст заметки"))
