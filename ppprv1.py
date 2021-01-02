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

        
        self.operatorComboBox = QtWidgets.QComboBox(self)
        self.operatorComboBox.addItem("<")
        self.operatorComboBox.addItem(">")
        self.operatorComboBox.addItem("==")

        self.operatorComboBox2 = QtWidgets.QComboBox(self)
        self.operatorComboBox2.addItem("I1")
        self.operatorComboBox2.addItem("I2")
        self.operatorComboBox2.addItem("I3")
        self.operatorComboBox2.addItem("I4")
        self.operatorComboBox2.addItem("I5")
        self.operatorComboBox2.addItem("I6")
        self.operatorComboBox2.addItem("Pocet kroku")

        self.vstup = QtWidgets.QLineEdit(self)

        self.podButton = QtWidgets.QPushButton("PODMÍNKA", self)

        self.kpodButton = QtWidgets.QPushButton("KONEC PODMÍNKY", self) 
        
        self.stopButton = QtWidgets.QPushButton("STOP", self) 
        
        self.vpredButton = QtWidgets.QPushButton("VPRED", self) 
        
        self.vzadButton = QtWidgets.QPushButton("VZAD", self) 
        
        self.levaButton = QtWidgets.QPushButton("VLEVO", self) 
        
        self.pravaButton = QtWidgets.QPushButton("VPRAVO", self) 
       
        self.deleButton = QtWidgets.QPushButton("SMAZAT", self) 
        
        self.setCentralWidget(formular)

        #Serazeni
        boxLayout1.addWidget(self.operatorComboBox2)
        boxLayout1.addWidget(self.operatorComboBox)
        boxLayout1.addWidget(self.vstup)
        boxLayout2.addWidget(self.podButton)
        boxLayout2.addWidget(self.kpodButton)
        boxLayout2.addWidget(self.stopButton)
        boxLayout2.addWidget(self.vpredButton)
        boxLayout2.addWidget(self.vzadButton)
        boxLayout2.addWidget(self.levaButton)
        boxLayout2.addWidget(self.pravaButton)
        boxLayout2.addWidget(self.deleButton)
        
        #Napojeni tlacitek
        self.stopButton.clicked.connect(self.stop)
        self.vpredButton.clicked.connect(self.vpred)
        self.vzadButton.clicked.connect(self.vzad)
        self.levaButton.clicked.connect(self.leva)
        self.pravaButton.clicked.connect(self.prava)
        self.deleButton.clicked.connect(self.dele)
        self.podButton.clicked.connect(self.pod)
        self.kpodButton.clicked.connect(self.kpod)
        
    #Definice funkci tlacitek
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
    def pod(self):
        operator = self.operatorComboBox.currentText()
        operator2 = self.operatorComboBox2.currentText()
        vstup = str(self.vstup.text())
        with open(program, "a", encoding="utf-8") as f:
         f.write("Podmínka\n")
         f.write(operator2 + operator + vstup +"\n")
         f.flush()
         print("Zapsano Podminka\n" + operator2 + operator + vstup)
    def kpod(self):
        with open(program, "a", encoding="utf-8") as f:
         f.write("Konec podminky\n")
         f.flush()
         print("Zapsano Konec podminky")
    def dele(self):
        with open(program, "w", encoding="utf-8") as f:
         f.write()
         f.flush()
aplikace = QtWidgets.QApplication(sys.argv)
okno = Window()
sys.exit(aplikace.exec_())
