# Display a dialog for execute an application


from qt import *
import sys, os

class QExeFile(QDialog):
    def initConections (self):
        self.connect (self.qtOK, SIGNAL ("clicked()"), self.onOk)
	
    def onOk (self):
        file = self.qtExeFile.text()
        os.system (str(file)+" &")
        sys.exit (0)

    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("QExeFile")

        self.setCaption("Execute an application")

        self.qtExeFile = QLineEdit(self,"qtExeFile")
        self.qtExeFile.setGeometry(QRect(180,40,190,40))

        self.qtOK = QPushButton(self,"qtOK")
        self.qtOK.setGeometry(QRect(40,130,141,35))
        self.qtOK.setText("OK")

        self.qtBtExeFile = QPushButton(self,"qtBtExeFile")
        self.qtBtExeFile.setGeometry(QRect(20,40,140,40))
        self.qtBtExeFile.setText("File to execute...")

        self.qtCancel = QPushButton(self,"qtCancel")
        self.qtCancel.setGeometry(QRect(210,130,141,35))
        self.qtCancel.setText("Cancel")

        self.resize(QSize(398,194).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.initConections ()

################ MAIN #############################
app = QApplication (sys.argv)
wdg = QExeFile ()
app.setMainWidget (wdg)
wdg.show ()
app.exec_loop ()

