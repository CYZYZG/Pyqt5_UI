import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QMessageBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.is_saved = True                                            # 1

        self.textedit = QTextEdit(self)                                 # 2
        self.textedit.textChanged.connect(self.on_textchanged_func)

        self.button = QPushButton('Save', self)                         # 3
        self.button.clicked.connect(self.on_clicked_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def on_clicked_func(self):
        self.save_func(self.textedit.toPlainText())
        self.is_saved = True

    def save_func(self, text):
        with open('saved.txt', 'w') as f:
            f.write(text)

    def closeEvent(self, QCloseEvent):                                  # 4
        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.textedit.toPlainText())
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())