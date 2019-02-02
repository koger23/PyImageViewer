from PySide2.QtWidgets import QFileSystemModel, QTreeView, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PySide2.QtCore import QDir
import sys



class PyImageViewer(QMainWindow):

    def __init__(self):

        super(PyImageViewer, self).__init__()
        self.setWindowTitle("PyImageViewer")


        self.centralWidget = QWidget()
        mainLayout = QHBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)


app = QApplication(sys.argv)
window = PyImageViewer()
window.show()
app.exec_()