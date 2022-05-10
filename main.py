from PyQt5 import QtWidgets, QtCore
from design.main_window import Ui_main_window
from design.additional_window import Ui_additional_window
import sys
import json
import os


class additional_window(QtWidgets.QMainWindow, Ui_additional_window):
    def __init__(self, parent=None):
        super(additional_window, self).__init__(parent)
        self.setupUi(self)


class main_window(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super(main_window, self).__init__(parent)
        self.setupUi(self)

        self.create_note_button.clicked.connect(self.create_note)
        self.save_note_button.clicked.connect(self.save_note)
        self.delete_note_button.clicked.connect(self.delete_note)
        self.add_tag_to_note_button.clicked.connect(self.add_tag_to_note)
        self.unpin_tag_from_note_button.clicked.connect(self.unpin_tag_from_note)
        self.find_notes_by_tag_button.clicked.connect(self.find_note_by_tag)

        self.notes_list.itemClicked.connect(self.selected_note_func)
        self.tags_list.itemClicked.connect(self.selected_tag_func)

        self.selected_note = None
        self.selected_tag = None
        self.notes_json = "notes.json"
        self.notes_dict = dict()
        self.tags_lst = list()

    def update_json(self):
        with open(self.notes_json, "w") as file:
            file.write(json.dumps(self.notes_dict))

    def create_note(self):
        self.additional_window = additional_window()
        self.additional_window.show()

    def save_note(self):
        title = self.additional_window.note_title_line.text()
        content = self.additional_window.note_content_text.toPlainText()

        self.notes_dict.update({title: [None, content]})
        self.update_json()
        self.notes_list.addItem(title)
        self.additional_window.close()

    def delete_note(self):
        current_item_index = self.notes_list.currentRow()
        current_item_value = self.notes_list.currentItem().text()

        self.notes_dict.pop(current_item_value)
        self.update_json()
        self.notes_list.takeItem(current_item_index)

    def selected_note_func(self, item):
        self.selected_note = item.text()
        self.text_of_note.clear()
        self.text_of_note.setText(self.notes_dict[item.text()][1])

    def selected_tag_func(self, item):
        self.selected_tag = item.text()

    def create_tag(self):
        name_tag = self.input_tag.text()

        if name_tag not in self.tags_lst:
            self.tags_lst.append(name_tag)
            self.tags_list.addItem(name_tag)
            self.input_tag.clear()

        else:
            self.input_tag.clear()
            self.input_tag.setText("Error")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.create_tag()

    def add_tag_to_note(self):
        self.notes_dict[self.selected_note][0] = self.selected_tag
        self.update_json()

    def unpin_tag_from_note(self):
        self.notes_dict[self.selected_note][0] = None
        self.update_json()

    def find_note_by_tag(self):
        if self.selected_tag != None:
            self.notes_list.clear()

            filter_dict = {
                k: v for k, v in self.notes_dict.items() if v[0] == self.selected_tag
            }
            for key in filter_dict:
                self.notes_list.addItem(key)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = main_window()
    main_window.show()

    try:
        sys.exit(app.exec())
    finally:
        if os.path.exists(main_window.notes_json):
            os.remove(main_window.notes_json)
