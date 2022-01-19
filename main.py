#UI
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHeaderView, QTableWidgetItem,QVBoxLayout
from PyQt5 import QtGui, uic, QtCore

from unidecode import unidecode
import re
from collections import OrderedDict
from num2words import num2words
import random
import math
from collections import Counter

qtCreatorFile = "kryptoUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


 
 
def isUniqueChars(string):
 
    # Counting frequency
    freq = Counter(string)
 
    if(len(freq) == len(string)):
        return True
    else:
        return False
 
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    return (str1.join(s))

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)

        
class MyApp(QMainWindow, Ui_MainWindow):
    def change(self):
        if self.matica_5X5.isChecked():
            self.tableWidget_2.hide()
            self.tableWidget.show()
            self.label_3.show()
            self.label_4.hide()

        elif self.matica_6X6.isChecked():
            self.tableWidget.hide()
            self.tableWidget_2.show()   
            self.label_3.hide()
            self.label_4.show()
            
    def check(self):
        check=False
        if self.matica_5X5.isChecked():
            if self.CheckBox_JazykCZ.isChecked():
                Abeceda=""
                test="ABCDEFGHIKLMNOPQRSTUVWXYZ"
                for i in range(5):
                    for j in range(5):
                        widgetItem=self.tableWidget.item(i,j)
                        Abeceda+=(widgetItem.text())


                if isUniqueChars(Abeceda)==True and sorted(Abeceda)==sorted(test):
                    check=True
                elif isUniqueChars(Abeceda)==False:
                    self.labelVysledek.setText("najdeny duplikat")
                elif sorted(Abeceda)!=sorted(test):
                    self.labelVysledek.setText("pouzite nedovolene znaky <A-J)AND(J-Z>")
                else:
                    self.labelVysledek.setText("stala sa chyba")
            elif self.CheckBox_JazykEN.isChecked():
                Abeceda=""
                test="ABCDEFGHIJKLMNOPRSTUVWXYZ"
                for i in range(5):
                    for j in range(5):
                        widgetItem=self.tableWidget.item(i,j)
                        Abeceda+=(widgetItem.text())


                if isUniqueChars(Abeceda)==True and sorted(Abeceda)==sorted(test):
                    self.labelVysledek.setText("vsetko v poriadku")
                    check=True
                elif isUniqueChars(Abeceda)==False:
                    self.labelVysledek.setText("najdeny duplikat")
                elif sorted(Abeceda)!=test:
                    self.labelVysledek.setText("pouzite nedovolene znaky <A-Q)AND(Q-Z>")
                else:
                    self.labelVysledek.setText("stala sa chyba")
            else:
                self.labelVysledok.setText("stala sa chyba")
        
        elif self.matica_6X6.isChecked():
            Abeceda=""
            test="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            for i in range(6):
                for j in range(6):
                    widgetItem=self.tableWidget_2.item(i,j)
                    Abeceda+=(widgetItem.text())
            if isUniqueChars(Abeceda)==True and sorted(Abeceda)==sorted(test):
                check=True
            elif isUniqueChars(Abeceda)==False:
                self.labelVysledek.setText("najdeny duplikat")
            elif sorted(Abeceda)!=sorted(test):
                self.labelVysledek.setText("pouzite nedovolene znaky pouzi <A-Z>AND<0,9>")
            else:
                self.labelVysledek.setText("stala sa chyba")
        return check
    
        
    def clean(self):
        if self.matica_6X6.isChecked():
            for i in range(6):
                for j in range(6):
                    self.tableWidget_2.setItem(i,j,QTableWidgetItem(""))
        else:
            for i in range(5):
                for j in range(5):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(""))
                
    def generate(self):
        if self.matica_5X5.isChecked():
            self.tableWidget_2.hide()
            self.tableWidget.show()
            self.label_3.show()
            self.label_4.hide()
            Abeceda=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            random.shuffle(Abeceda)
            Abeceda=listToString(Abeceda)
    
            if self.CheckBox_JazykCZ.isChecked():
                Abeceda=Abeceda.replace("J","")
            elif self.CheckBox_JazykEN.isChecked():
                Abeceda=Abeceda.replace("Q","")
            else:
                self.labelVysledek.setText("vyber jazyk")
                
            Abeceda=list(Abeceda)
            f=0
            for i in range(5):
                for j in range(5):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(Abeceda[f]))
                    f+=1
        else:
            self.tableWidget.hide()
            self.tableWidget_2.show()   
            self.label_3.hide()
            self.label_4.show()
            Abeceda=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
            random.shuffle(Abeceda)
            Abeceda=listToString(Abeceda)
            Abeceda=list(Abeceda)
            f=0
            for i in range(6):
                for j in range(6):
                    self.tableWidget_2.setItem(i,j,QTableWidgetItem(Abeceda[f]))
                    f+=1
        return Abeceda

    def encrypt6x6(self):
        
        slovnik={
     "0":"A",
     "1":"D",
     "2":"F",
     "3":"G",
     "4":"V",
     "5":"X"
        }
        
        KlucoveSlovo=str(self.plainTextEdit_A.toPlainText())
        if KlucoveSlovo.isdigit():
            self.labelVysledek.setText("zadajte platne klucove slovo")
            exit()
    
        KlucoveSlovo=unidecode(KlucoveSlovo)
        for k in KlucoveSlovo.split("\n"):
            KlucoveSlovo =(re.sub(r"[^a-zA-Z0-9]+", '', k))    
        KlucoveSlovo=KlucoveSlovo.upper()        
        
        Vstup=str(self.plainTextEdit_Input.toPlainText())   
        Vstup=unidecode(Vstup)
        Vstup=Vstup.replace(" ","XmezeraX")
    
        for k in Vstup.split("\n"):
            Vstup=(re.sub(r"[^a-zA-Z0-9]+",'', k))
               
        Vstup=Vstup.upper()
        
        Substitucia=[]
        
        matica_abeceda=[[0, 0, 0, 0, 0,0],[0,0, 0, 0, 0,0],[0,0, 0, 0, 0, 0],[0,0, 0, 0, 0, 0],[0,0, 0, 0, 0, 0],[0, 0, 0,0, 0, 0]]
        for i in range(6):
            for j in range(6):
                widgetItem=self.tableWidget_2.item(i,j)
                matica_abeceda[i][j]=widgetItem.text()

        i=0   
        j=0
        while i < len(Vstup):
            index1=index_2d(matica_abeceda,Vstup[i])
            j=str(index1[0])
            k=str(index1[1])
            Substitucia.append(j)
            Substitucia.append(k)
            i+=1
        for i in range(len(Substitucia)):
            Substitucia[i]=slovnik[Substitucia[i]]
        Substitucia=listToString(Substitucia)
 
        zoradeny_ks=list(KlucoveSlovo)
        zoradeny_ks.sort()
        
        cols=len(KlucoveSlovo)
        rows=math.ceil(len(Substitucia)/len(KlucoveSlovo))
        transpozicnaMatica = [[0]*cols for y in range(rows)]
    
        k=0    
        i=0
        j=0
    
        for i in range(rows):
            for j in range(cols):
                if k==len(Substitucia):
                    break
                else:
                    transpozicnaMatica[i][j]=Substitucia[k]
                    k+=1

        transpozicia=[]
        i=0
        j=0
        k=0
        KS=list(KlucoveSlovo)

        for i in range(0,len(KlucoveSlovo)):
            for j in range(0,len(KlucoveSlovo)):
                if zoradeny_ks[i]==KS[j]:
                    for k in range(0,len(transpozicnaMatica)):
                        if(transpozicnaMatica[k][j]==0):
                            continue
                        else:
                            transpozicia.append(transpozicnaMatica[k][j])
                    KS[j]="#"
        transpozicia=listToString(transpozicia)
        transpozicia=' '.join([transpozicia[i:i+5] for i in range(0, len(transpozicia), 5)])                    
    
        self.labelVysledek.setText(transpozicia)

    def encrypt(self):
        
        
        slovnik={
     "0":"A",
     "1":"D",
     "2":"F",
     "3":"G",
     "4":"X" 
        }
        
        KlucoveSlovo=str(self.plainTextEdit_A.toPlainText())
        if KlucoveSlovo.isdigit():
            self.labelVysledek.setText("zadajte platne klucove slovo")
            exit()
    
        KlucoveSlovo=unidecode(KlucoveSlovo)
        for k in KlucoveSlovo.split("\n"):
            KlucoveSlovo =(re.sub(r"[^a-zA-Z0-9]+", '', k))
            
        KlucoveSlovo=KlucoveSlovo.upper()        
        
        Vstup=str(self.plainTextEdit_Input.toPlainText())
    
        
        i=0
        while i<len(Vstup):
            if Vstup[i].isdigit():
                if self.CheckBox_JazykCZ.isChecked():
                    x=num2words(Vstup[i],lang="cz")
                elif self.CheckBox_JazykEN.isChecked():
             
                    x=num2words(Vstup[i],lang="en")
                else:
                    self.labelVysledek.setText("Vyberte možnosť jazyka")
                    exit(1)
        
                Vstup=Vstup.replace(Vstup[i],x)
            i+=1
            
        Vstup=unidecode(Vstup)
        Vstup=Vstup.replace(" ","XmezeraX")
    
        for k in Vstup.split("\n"):
            Vstup=(re.sub(r"[^a-zA-Z0-9]+",'', k))
               
        Vstup=Vstup.upper()
        if self.CheckBox_JazykCZ.isChecked():
            Vstup=Vstup.replace("J","I")
        elif self.CheckBox_JazykEN.isChecked():
            Vstup=Vstup.replace("Q","O")

        
        Substitucia=[]

        matica_abeceda=[[0, 0, 0, 0, 0],[0,0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        
        for i in range(5):
            for j in range(5):
                widgetItem=self.tableWidget.item(i,j)
                matica_abeceda[i][j]=widgetItem.text()

        i=0   
        j=0
        while i < len(Vstup):
            index1=index_2d(matica_abeceda,Vstup[i])
            j=str(index1[0])
            k=str(index1[1])
            Substitucia.append(j)
            Substitucia.append(k)
            i+=1
        for i in range(len(Substitucia)):
            Substitucia[i]=slovnik[Substitucia[i]]
        Substitucia=listToString(Substitucia)

        zoradeny_ks=list(KlucoveSlovo)
        zoradeny_ks.sort()
        
        cols=len(KlucoveSlovo)
        rows=math.ceil(len(Substitucia)/len(KlucoveSlovo))
        transpozicnaMatica = [[0]*cols for y in range(rows)]
    
        k=0    
        i=0
        j=0
    
        for i in range(rows):
            for j in range(cols):
                if k==len(Substitucia):
                    break
                else:
                    transpozicnaMatica[i][j]=Substitucia[k]
                    k+=1

        transpozicia=[]
        i=0
        j=0
        k=0
        KS=list(KlucoveSlovo)

        for i in range(0,len(KlucoveSlovo)):
            for j in range(0,len(KlucoveSlovo)):
                if zoradeny_ks[i]==KS[j]:
                    for k in range(0,len(transpozicnaMatica)):
                        if(transpozicnaMatica[k][j]==0):
                            continue
                        else:
                            transpozicia.append(transpozicnaMatica[k][j])
                    KS[j]="#"
        transpozicia=listToString(transpozicia)
        transpozicia=' '.join([transpozicia[i:i+5] for i in range(0, len(transpozicia), 5)])                    
    
        self.labelVysledek.setText(transpozicia)
        
    def decrypt(self):
        
        slovnik={
     "A":0,
     "D":1,
     "F":2,
     "G":3,
     "X":4 
        }
     
        KlucoveSlovo=str(self.plainTextEdit_A.toPlainText())
    
        if KlucoveSlovo.isdigit():
            """self.labelVysledek.setText("zadajte platne klucove slovo")"""
            exit()
    
        KlucoveSlovo=unidecode(KlucoveSlovo)
        for k in KlucoveSlovo.split("\n"):
            KlucoveSlovo =(re.sub(r"[^a-zA-Z0-9]+", '', k))
            
        KlucoveSlovo=KlucoveSlovo.upper()        
        
        Vstup=str(self.plainTextEdit_Input.toPlainText())
    
        Vstup=Vstup.upper()
        Vstup=Vstup.replace(" ","")
        if self.CheckBox_JazykCZ.isChecked():
            Vstup=Vstup.replace("J","I")
        elif self.CheckBox_JazykEN.isChecked():
            Vstup=Vstup.replace("Q","O")
                
        cols=len(KlucoveSlovo)
        rows=math.ceil(len(Vstup)/len(KlucoveSlovo))
        transpozicnaMatica = [[0]*cols for y in range(rows)]
        SortedTranspozicnaMatica = [[0]*cols for y in range(rows)]
      
        if len(Vstup)%len(KlucoveSlovo)>0:
            doplnok=((math.ceil(len(Vstup)/len(KlucoveSlovo))*len(KlucoveSlovo))-len(Vstup))
        else:
            doplnok=0

        if doplnok != 0:
            for i in range(0,doplnok):
                transpozicnaMatica[rows-1][cols-i-1]="#"

        zoradeny_ks=list(KlucoveSlovo)
        zoradeny_ks.sort()
        KS=list(KlucoveSlovo)

        for i in range(0,len(KlucoveSlovo)):
            for j in range(0,len(KlucoveSlovo)):
                if zoradeny_ks[i]==KS[j]:
                    for k in range(0,len(transpozicnaMatica)):
                        SortedTranspozicnaMatica[k][i]=transpozicnaMatica[k][j]
                    zoradeny_ks[i]="@"
                    KS[j]="/"
                

        k=0    
        i=0
        j=0
    
        for i in range(cols):
            for j in range(rows):
                if k==len(Vstup):
                    break
                else:
                    if SortedTranspozicnaMatica[j][i]!="#":
                        SortedTranspozicnaMatica[j][i]=Vstup[k]
                        k+=1
                    else:
                        continue
    
        transpozicia=[]
        i=0
        j=0
        k=0
        zoradeny_ks=list(KlucoveSlovo)
        zoradeny_ks.sort()
        KS=list(KlucoveSlovo)
        
        for i in range(0,len(KlucoveSlovo)):
            for j in range(0,len(KlucoveSlovo)):
                if KS[i]==zoradeny_ks[j]:
                    for k in range(0,len(SortedTranspozicnaMatica)):
                        transpozicnaMatica[k][i]=SortedTranspozicnaMatica[k][j]
                    KS[i]="@"
                    zoradeny_ks[j]="/"

        
        for i in range(0,rows):
            for j in range(0,cols):
                if transpozicnaMatica[i][j]!="#":
                    transpozicia.append(transpozicnaMatica[i][j])
                else:
                    continue
        
        for i in range(len(transpozicia)):
            transpozicia[i]=slovnik[transpozicia[i]]
            
        
        matica_abeceda=[[0, 0, 0, 0, 0],[0,0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
            
        for i in range(5):
            for j in range(5):
                widgetItem=self.tableWidget.item(i,j)
                matica_abeceda[i][j]=widgetItem.text()  

        Substitucia=[]
        i=0  
        k=0
        while i < len(transpozicia):
            j=transpozicia[i]
            l=transpozicia[i+1]
            Substitucia.append(matica_abeceda[j][l])
            i+=2
    
        Substitucia=listToString(Substitucia)
        Substitucia=Substitucia.replace("XMEZERAX"," ")
        if self.CheckBox_JazykCZ.isChecked():
            Substitucia=Substitucia.replace("IEDNA","1").replace("DVA","2").replace("TRI","3").replace("CTYRI","4").replace("PET","5").replace("SEST","6").replace("SEDM","7").replace("OSM","8").replace("DEVET","9").replace("NULA","0")
        elif self.CheckBox_JazykEN.isChecked():
            Substitucia=Substitucia.replace("ONE","1").replace("TWO","2").replace("THREE","3").replace("FOUR","4").replace("FIVE","5").replace("SIX","6").replace("SEVEN","7").replace("EIGHT","8").replace("NINE","9").replace("ZERO","0")
        self.labelVysledek.setText(Substitucia)
    
    def decrypt6x6(self):
        
        slovnik={
     "A":0,
     "D":1,
     "F":2,
     "G":3,
     "V":4,
     "X":5
        }
        
        KlucoveSlovo=str(self.plainTextEdit_A.toPlainText())
    
        if KlucoveSlovo.isdigit():
            """self.labelVysledek.setText("zadajte platne klucove slovo")"""
            exit()
    
        KlucoveSlovo=unidecode(KlucoveSlovo)
        for k in KlucoveSlovo.split("\n"):
            KlucoveSlovo =(re.sub(r"[^a-zA-Z0-9]+", '', k))
            
        KlucoveSlovo=KlucoveSlovo.upper()        
        
        Vstup=str(self.plainTextEdit_Input.toPlainText())
    
        Vstup=Vstup.upper()
        Vstup=Vstup.replace(" ","")

        cols=len(KlucoveSlovo)
        rows=math.ceil(len(Vstup)/len(KlucoveSlovo))
        transpozicnaMatica = [[0]*cols for y in range(rows)]
        SortedTranspozicnaMatica = [[0]*cols for y in range(rows)]
      
        if len(Vstup)%len(KlucoveSlovo)>0:
            doplnok=((math.ceil(len(Vstup)/len(KlucoveSlovo))*len(KlucoveSlovo))-len(Vstup))
        else:
            doplnok=0
        if doplnok != 0:
            for i in range(0,doplnok):
                transpozicnaMatica[rows-1][cols-i-1]="#"
 
        zoradeny_ks=list(KlucoveSlovo)
        zoradeny_ks.sort()
        KS=list(KlucoveSlovo)

        for i in range(0,len(KlucoveSlovo)):
            for j in range(0,len(KlucoveSlovo)):
                if zoradeny_ks[i]==KS[j]:
                    for k in range(0,len(transpozicnaMatica)):
                        SortedTranspozicnaMatica[k][i]=transpozicnaMatica[k][j]
                    zoradeny_ks[i]="@"
                    KS[j]="/"
  
        k=0    
        i=0
        j=0
    
        for i in range(cols):
            for j in range(rows):
                if k==len(Vstup):
                    break
                else:
                    if SortedTranspozicnaMatica[j][i]!="#":
                        SortedTranspozicnaMatica[j][i]=Vstup[k]
                        k+=1
                    else:
                        continue

        transpozicia=[]
        i=0
        j=0
        k=0
        zoradeny_ks=list(KlucoveSlovo)
        zoradeny_ks.sort()
        KS=list(KlucoveSlovo)

        
        for i in range(0,len(KlucoveSlovo)):
            for j in range(0,len(KlucoveSlovo)):
                if KS[i]==zoradeny_ks[j]:
                    for k in range(0,len(SortedTranspozicnaMatica)):
                        transpozicnaMatica[k][i]=SortedTranspozicnaMatica[k][j]
                    KS[i]="@"
                    zoradeny_ks[j]="/"
                    
 
            
        
        for i in range(0,rows):
            for j in range(0,cols):
                if transpozicnaMatica[i][j]!="#":
                    transpozicia.append(transpozicnaMatica[i][j])
                else:
                    continue
        
        for i in range(len(transpozicia)):
            transpozicia[i]=slovnik[transpozicia[i]]
            
        
        matica_abeceda=[[0, 0, 0, 0, 0,0],[0, 0, 0, 0, 0,0],[0, 0, 0, 0, 0,0],[0, 0, 0, 0, 0,0],[0, 0, 0, 0, 0,0],[0, 0, 0, 0, 0,0]]
            
        for i in range(6):
            for j in range(6):
                widgetItem=self.tableWidget_2.item(i,j)
                matica_abeceda[i][j]=widgetItem.text()  
    
        Substitucia=[]
        i=0  
        k=0
        while i < len(transpozicia):
            j=transpozicia[i]
            l=transpozicia[i+1]
            Substitucia.append(matica_abeceda[j][l])
            i+=2
    
        Substitucia=listToString(Substitucia)
        Substitucia=Substitucia.replace("XMEZERAX"," ")
        self.labelVysledek.setText(Substitucia)
        
    def execute(self):
        ks=self.plainTextEdit_A.toPlainText()
        ks=ks.replace(" ","")
        if self.CheckBox_Desifrovat.isChecked() and self.matica_5X5.isChecked() and self.check()==True and  len(ks)>0:
                
            string=self.plainTextEdit_Input.toPlainText()
            string=string.replace(" ","")

            if len(string)%2 ==0 :
                self.decrypt()
            elif len(string)%2 !=0 :
                self.labelVysledek.setText("Nespravny vstup")
            
        elif self.CheckBox_Sifrovat.isChecked() and self.matica_5X5.isChecked() and self.check()==True and  len(ks)>0:
            self.encrypt()
        elif self.CheckBox_Sifrovat.isChecked() and self.matica_6X6.isChecked() and self.check()==True and  len(ks)>0:
            self.encrypt6x6()
        elif self.CheckBox_Desifrovat.isChecked() and self.matica_6X6.isChecked() and self.check()==True and  len(ks)>0:
            string=self.plainTextEdit_Input.toPlainText()
            string=string.replace(" ","")
            if len(string)%2 ==0:
                self.decrypt6x6()
            else:
                self.labelVysledek.setText("Nespravny vstup")

        elif self.check()==False:
             self.labelVysledek.setText("Opravte si maticu a pouzijte tlacidlo skontrolovat")

        elif  len(ks)==0:
            self.labelVysledek.setText("zadajte platne klucove slovo")
        
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Button_Execute.clicked.connect(self.execute)  
        self.Button_Generate.clicked.connect(self.generate)
        self.Button_Reset.clicked.connect(self.clean)
        self.pushButtonSkontrolovat.clicked.connect(self.check)
        self.tableWidget_2.hide()
        self.pushButton.clicked.connect(self.change)
        self.label_4.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())        
 
    
