# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(1080, 720)
        self.text_of_note = QtWidgets.QTextEdit(main_window)
        self.text_of_note.setGeometry(QtCore.QRect(13, 24, 671, 671))
        self.text_of_note.setTabChangesFocus(True)
        self.text_of_note.setObjectName("text_of_note")
        self.notes_label = QtWidgets.QLabel(main_window)
        self.notes_label.setGeometry(QtCore.QRect(690, 25, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.notes_label.setFont(font)
        self.notes_label.setObjectName("notes_label")
        self.create_note_button = QtWidgets.QPushButton(main_window)
        self.create_note_button.setGeometry(QtCore.QRect(700, 250, 191, 28))
        self.create_note_button.setObjectName("create_note_button")
        self.delete_note_button = QtWidgets.QPushButton(main_window)
        self.delete_note_button.setGeometry(QtCore.QRect(900, 250, 171, 28))
        self.delete_note_button.setObjectName("delete_note_button")
        self.save_note_button = QtWidgets.QPushButton(main_window)
        self.save_note_button.setGeometry(QtCore.QRect(700, 280, 371, 28))
        self.save_note_button.setObjectName("save_note_button")
        self.tags_list = QtWidgets.QListWidget(main_window)
        self.tags_list.setGeometry(QtCore.QRect(700, 351, 371, 241))
        self.tags_list.setObjectName("tags_list")
        self.input_tag = QtWidgets.QLineEdit(main_window)
        self.input_tag.setGeometry(QtCore.QRect(700, 600, 371, 28))
        self.input_tag.setAutoFillBackground(True)
        self.input_tag.setInputMask("")
        self.input_tag.setText("")
        self.input_tag.setFrame(False)
        self.input_tag.setReadOnly(False)
        self.input_tag.setClearButtonEnabled(False)
        self.input_tag.setObjectName("input_tag")
        self.find_notes_by_tag_button = QtWidgets.QPushButton(main_window)
        self.find_notes_by_tag_button.setGeometry(QtCore.QRect(700, 670, 371, 28))
        self.find_notes_by_tag_button.setObjectName("find_notes_by_tag_button")
        self.unpin_tag_from_note_button = QtWidgets.QPushButton(main_window)
        self.unpin_tag_from_note_button.setGeometry(QtCore.QRect(900, 640, 171, 28))
        self.unpin_tag_from_note_button.setObjectName("unpin_tag_from_note_button")
        self.add_tag_to_note_button = QtWidgets.QPushButton(main_window)
        self.add_tag_to_note_button.setGeometry(QtCore.QRect(700, 640, 191, 28))
        self.add_tag_to_note_button.setObjectName("add_tag_to_note_button")
        self.tags_label = QtWidgets.QLabel(main_window)
        self.tags_label.setGeometry(QtCore.QRect(700, 320, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.tags_label.setFont(font)
        self.tags_label.setObjectName("tags_label")
        self.notes_list = QtWidgets.QListWidget(main_window)
        self.notes_list.setGeometry(QtCore.QRect(700, 60, 371, 181))
        self.notes_list.setObjectName("notes_list")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Умные заметки"))
        self.notes_label.setText(_translate("main_window", "Список заметок "))
        self.create_note_button.setText(_translate("main_window", "Создать заметку"))
        self.delete_note_button.setText(_translate("main_window", "Удалить заметку"))
        self.save_note_button.setText(_translate("main_window", "Сохранить заметку"))
        self.input_tag.setPlaceholderText(_translate("main_window", "Введите тег ..."))
        self.find_notes_by_tag_button.setText(_translate("main_window", "Искать заметки по тегу"))
        self.unpin_tag_from_note_button.setText(_translate("main_window", "Открепить от заметки"))
        self.add_tag_to_note_button.setText(_translate("main_window", "Добавить к заметке"))
        self.tags_label.setText(_translate("main_window", "Список тегов "))
