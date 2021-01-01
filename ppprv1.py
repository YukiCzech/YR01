from PyQt5 import QtWidgets, QtGui
import sys
program = "program.txt"
class Window(QtWidgets.QMainWindow):
    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.setWindowTitle("Programovaci prostredi")
        self.init_gui()
        self.show()

    def init_gui(self):
        formular = QtWidgets.QWidget()
        formularLayout = QtWidgets.QVBoxLayout()
        formular.setLayout(formularLayout)
        boxLayout1 = QtWidgets.QHBoxLayout()
        boxLayout2 = QtWidgets.QHBoxLayout()

        formularLayout.addStretch()
        formularLayout.addLayout(boxLayout1)
        formularLayout.addLayout(boxLayout2)
        formularLayout.addStretch()
    def init_gui(self):
        formular = QtWidgets.QWidget()
        formularLayout = QtWidgets.QVBoxLayout()
        formular.setLayout(formularLayout)

        boxLayout1 = QtWidgets.QHBoxLayout()
        boxLayout2 = QtWidgets.QHBoxLayout()

        formularLayout.addStretch()
        formularLayout.addLayout(boxLayout1)
        formularLayout.addLayout(boxLayout2)
        formularLayout.addStretch()

        self.stopButton = QtWidgets.QPushButton("STOP", self) 
        boxLayout2.addWidget(self.stopButton)
        self.vpredButton = QtWidgets.QPushButton("VPRED", self) 
        boxLayout2.addWidget(self.vpredButton)
        self.vzadButton = QtWidgets.QPushButton("VZAD", self) 
        boxLayout2.addWidget(self.vzadButton)
        self.levaButton = QtWidgets.QPushButton("VLEVO", self) 
        boxLayout2.addWidget(self.levaButton)
        self.pravaButton = QtWidgets.QPushButton("VPRAVO", self) 
        boxLayout2.addWidget(self.pravaButton)
        self.deleButton = QtWidgets.QPushButton("SMAZAT", self) 
        boxLayout1.addWidget(self.deleButton)

        self.setCentralWidget(formular)
        self.stopButton.clicked.connect(self.stop)
        self.vpredButton.clicked.connect(self.vpred)
        self.vzadButton.clicked.connect(self.vzad)
        self.levaButton.clicked.connect(self.leva)
        self.pravaButton.clicked.connect(self.prava)
        self.deleButton.clicked.connect(self.dele)
    def stop(self):
        with open(program, "a", encoding="utf-8") as f:
         f.write("Zastav\n")
         f.flush()
         print("Zapsano STOP")
    def vpred(self):
        with open(program, "a", encoding="utf-8") as f:
         f.write("Jed vpred\n")
         f.flush()
         print("Zapsano VPRED")
    def vzad(self):
        with open(program, "a", encoding="utf-8") as f:
         f.write("Jed vzad\n")
         f.flush()
         print("Zapsano VZAD")
    def leva(self):
        with open(program, "a", encoding="utf-8") as f:
         f.write("Otocit vlevo\n")
         f.flush()
         print("Zapsano DOLEVA")    
    def prava(self):
        with open(program, "a", encoding="utf-8") as f:
         f.write("Otocit vpravo\n")
         f.flush()
         print("Zapsano DOPRAVA")
    def dele(self):
        with open(program, "w", encoding="utf-8") as f:
         f.write()
         f.flush()
aplikace = QtWidgets.QApplication(sys.argv)
okno = Window()
sys.exit(aplikace.exec_())
