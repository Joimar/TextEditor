from Interface.mainWindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Editor()
    test.show()
    app.exec_()
