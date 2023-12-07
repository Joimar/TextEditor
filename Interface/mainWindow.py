# This is a sample Python script.
import sys

from PySide2.QtWidgets import QApplication, QWidget
from InterfaceQTFiles.telaSimples import Ui_Dialog

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from InterfaceQTFiles import telaSimples


class Editor(QWidget, Ui_Dialog):
    def __int__(self) -> None:
        super(Editor, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Editor Teste")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.

    window = Editor()

    window.show()

    # Start the event loop.
    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
