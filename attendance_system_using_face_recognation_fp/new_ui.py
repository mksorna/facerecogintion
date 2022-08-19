import tkinter as tk       #IMPORTS
import os
from tkinter import messagebox
from cv2 import COLOR_BAYER_BG2RGB, COLOR_BGR2RGB
import mysql.connector 
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
def face_cropped(imgf):   #JUST CROPS FACE
    face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    rgb=cv2.cvtColor(imgf,COLOR_BGR2RGB)
    faces=face_classifier.detectMultiScale(rgb,1.3,5)
    for(x,y,w,h)in faces:
        face_cropped=imgf[y:y+h,x:x+w]
        return face_cropped

def parse_image(name,idd):          #OPENS DEFAULT CAMERA AND MONITORS FACE,FRAME IS CAPTURED ON PRESSING SPACEBAR
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Python hub Scanner")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Python hub Scanner", frame)
        k = cv2.waitKey(1)
        if k%256 == 32:
            break
    cam.release()
    cv2.destroyAllWindows()
    if face_cropped(frame) is not None: #CROPS FACE FOR BETTER OPTIMIZATION
            face=cv2.resize(face_cropped(frame),(450,450))   
            cv2.imshow('Cropped Face',face)
            cv2.waitKey(0)
            
    file_name_path=f'data/{str(idd)}_{str(name)}.jpg'   
    cv2.imwrite(file_name_path,face) #SAVES PHOTO IN DATA FILE
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('Result','Your data is ready to be saved!') #CONFIRMATION ALERT

def push_data(dep,sem,namee,idd):
    db=mysql.connector.connect(host="localhost",
                        user="root",
                        passwd="root",
                        database="test",
                        )
    cursorr=db.cursor()
    #cursorr.execute("CREATE TABLE Systemm (Department VARCHAR(50),Year_Semester VARCHAR(50),Student_ID smallint unsigned,Student_name VARCHAR(50))")
    cursorr.execute("SELECT * FROM Systemm")
    existing=False
    #i[3]==namee and i[1]==sem and (i[0]==dep and i[2]==int(idd))
    for i in cursorr:
        if i[2]==int(idd):
            existing=True
            break
    if not existing:
        cursorr.execute("INSERT INTO Systemm (Department,Year_Semester,Student_ID,Student_name) VALUES (%s,%s,%s,%s)",(dep,sem,int(idd),namee))
        db.commit()
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo('Result',f'{namee} was registered successfully!')
    if existing:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo('Error','ID already exists in database!')
        messagebox.showinfo('Error','Every register must have a unique ID')

class Ui_Dialog(object):#GUI ELEMENTS STARTS HERE
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1368, 700)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 80, 1381, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(f"{os.getcwd()}//image//white_back.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(0, 0, 1371, 81))
        self.title.setStyleSheet("font: 75 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.banner = QtWidgets.QLabel(Dialog)
        self.banner.setGeometry(QtCore.QRect(550, 80, 301, 61))
        self.banner.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap(f"{os.getcwd()}//image//boubanner1.png"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 1321, 561))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(70, 200, 20, 471))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(80, 190, 21, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 180, 201, 41))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(250, 190, 321, 20))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(560, 200, 16, 471))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(80, 660, 491, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(710, 180, 201, 41))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(840, 190, 461, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(1290, 200, 16, 471))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(670, 190, 41, 20))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(660, 200, 20, 471))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(670, 660, 631, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.search_by = QtWidgets.QComboBox(Dialog)
        self.search_by.setGeometry(QtCore.QRect(780, 230, 101, 21))
        self.search_by.setObjectName("search_by")
        self.search_by.addItem("")
        self.search_by.addItem("")
        self.search_by.addItem("")
        self.search_by.addItem("")
        self.search_by.addItem("")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(700, 220, 71, 41))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.table_data = QtWidgets.QTableWidget(Dialog)
        self.table_data.setGeometry(QtCore.QRect(700, 290, 581, 361))
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(4)
        self.table_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(3, item)
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(700, 200, 591, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(680, 210, 41, 61))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setGeometry(QtCore.QRect(1290, 210, 3, 61))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_15 = QtWidgets.QFrame(Dialog)
        self.line_15.setGeometry(QtCore.QRect(700, 250, 591, 41))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.search_box = QtWidgets.QLineEdit(Dialog)
        self.search_box.setGeometry(QtCore.QRect(890, 230, 161, 22))
        self.search_box.setObjectName("search_box")
        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(1060, 230, 101, 21))
        self.search.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.search.setObjectName("search")
        self.search_all = QtWidgets.QPushButton(Dialog)
        self.search_all.setGeometry(QtCore.QRect(1180, 230, 101, 21))
        self.search_all.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.search_all.setObjectName("search_all")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 220, 101, 41))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(90, 260, 141, 41))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(90, 300, 141, 41))
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(90, 340, 141, 41))
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.dep_combo = QtWidgets.QComboBox(Dialog)
        self.dep_combo.setGeometry(QtCore.QRect(370, 230, 171, 22))
        self.dep_combo.setObjectName("dep_combo")
        self.dep_combo.addItem("")
        self.dep_combo.addItem("")
        self.dep_combo.addItem("")
        self.dep_combo.addItem("")
        self.ys_combo = QtWidgets.QComboBox(Dialog)
        self.ys_combo.setGeometry(QtCore.QRect(370, 270, 171, 22))
        self.ys_combo.setObjectName("ys_combo")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.ys_combo.addItem("")
        self.sid = QtWidgets.QLineEdit(Dialog)
        self.sid.setGeometry(QtCore.QRect(370, 310, 171, 22))
        self.sid.setObjectName("sid")
        self.sname = QtWidgets.QLineEdit(Dialog)
        self.sname.setGeometry(QtCore.QRect(370, 350, 171, 22))
        self.sname.setObjectName("sname")
##        self.take_photo_sample = QtWidgets.QRadioButton(Dialog)
##        self.take_photo_sample.setGeometry(QtCore.QRect(100, 410, 141, 20))
##        self.take_photo_sample.setObjectName("take_photo_sample")
##        self.no_photo_sample = QtWidgets.QRadioButton(Dialog)
##        self.no_photo_sample.setGeometry(QtCore.QRect(390, 410, 141, 20))
##        self.no_photo_sample.setObjectName("no_photo_sample")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(110, 480, 101, 21))
        self.save.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.save.setObjectName("save")
        self.deletee = QtWidgets.QPushButton(Dialog)
        self.deletee.setGeometry(QtCore.QRect(110, 520, 101, 21))
        self.deletee.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.deletee.setObjectName("deletee")
        self.take_photo = QtWidgets.QPushButton(Dialog)
        self.take_photo.setGeometry(QtCore.QRect(390, 520, 101, 21))
        self.take_photo.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.take_photo.setObjectName("take_photo")
        self.update = QtWidgets.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(390, 480, 101, 21))
        self.update.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.update.setObjectName("update")
##        self.reset = QtWidgets.QPushButton(Dialog)
##        self.reset.setGeometry(QtCore.QRect(390, 520, 101, 21))
##        self.reset.setStyleSheet("background-color: rgb(0, 85, 0);\n"
##"font: 75 9pt \"MS Shell Dlg 2\";\n"
##"color: rgb(255, 255, 255);\n"
##"")
##        self.reset.setObjectName("reset")
##        self.update_photo = QtWidgets.QPushButton(Dialog)
##        self.update_photo.setGeometry(QtCore.QRect(390, 560, 101, 21))
##        self.update_photo.setStyleSheet("background-color: rgb(0, 85, 0);\n"
##"font: 75 9pt \"MS Shell Dlg 2\";\n"
##"color: rgb(255, 255, 255);\n"
##"")
##        self.update_photo.setObjectName("update_photo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)#GUI ELEMENTS END HERE
        #SIGNALS
        self.save.clicked.connect(self.process)     #ALL THE SIGNALS TO FUNCTIONS ARE HERE
        self.take_photo.clicked.connect(self.Photo)
        self.search.clicked.connect(self.searchh)
        self.search_all.clicked.connect(self.tablecount)
        self.update.clicked.connect(self.updatee)
        self.deletee.clicked.connect(self.removee)
        #SIGNALS
    def process(self):  #AFTER ALL THE DATA IS PROVIDED,PUSHES THE DATA INTO DATABASE
        s=self.dep_combo.currentText()
        y=self.ys_combo.currentText()
        i=self.sid.text()
        n=self.sname.text()
        if ((f"{i}_{n}.jpg" not in os.listdir(f"{os.getcwd()}\\data")) or n=="" or self.dep_combo.currentIndex()==0 or self.ys_combo.currentIndex()==0 or (self.sid.text()=="" or (not i.isnumeric()))):
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo('Error','One or more data samples were not found')
        else:
            push_data(s,y,n,i)  #THIS FUNCTION CALL SENDS ALL THE DATA TO ANOTHER FUNCTION WHERE DATA IS FINALLY STORED
            
        
    def Photo(self):
        n=self.sname.text()
        if n=="" or self.dep_combo.currentIndex()==0 or self.ys_combo.currentIndex()==0 or self.sid.text()=="":  #CHECKS IF OTHER DATA IS CORRECTLY PROVIDED
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo('Error','Please complete the above fields first')
        else:
            if(f"{self.sid.text()}_{self.sname.text()}.jpg" not in os.listdir(f"{os.getcwd()}\\data")): #CHECKS IF PHOTO SAMPLE IS ALREADY AVAILABLE
                parse_image(n,int(self.sid.text())) #READY TO TAKE PHOTO IF NOT
                #Thread(target=parse_image,args=(n,int(self.sid.text())),daemon=True).start()
            else:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo('Error','Provide Unique ID first!')
    def searchh(self):              #SEARCHES FOR DB CONTENT THROUGH 4 DIFFERENT CRITERIA
        if self.search_by.currentIndex()==0 or self.search_box.text()=="":  #CHECK IF ALL SEARCH FIELDS ARE PROVIDED
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo('Error','Complete all the search fields first')#DISPLAY IF NOT

        else:
            search_index=0
            queryy=self.search_box.text()  #GETTING SEARCH CRITERION
            comboo_index=self.search_by.currentIndex()
            if comboo_index==1:   #MAPPING COMBOBOX INDEX WITH SEARCHBOX INDEX 
                search_index=2
            elif comboo_index==2:
                search_index=1
            elif comboo_index==3:
                search_index=3
            elif comboo_index==4:
                search_index=0
            db=mysql.connector.connect(host="localhost",
                        user="root",
                        passwd="root",
                        database="test",
                        )
            cursorr=db.cursor()
            cursorr.execute("SELECT * FROM Systemm")
            u=0  #BELOW CHECKS WHETHER DATA ARE CORRECTLY TYPED AND THEN FINDS THE CRITERION
            l=[] #STORES SEARCH RESULT HERE
            if (((search_index==1 or search_index==3 or search_index==0) and (not queryy.isnumeric())) or (search_index==2 and (queryy.isnumeric()))):
                if search_index==2:
                    queryy=int(queryy)
                for i in cursorr:
                    if i[search_index]==queryy:
                        u+=1
                        l.append(i)
                self.table_data.setColumnCount(4) 
                self.table_data.setRowCount(u)
                for i in range(u): #l IS FLATTENED AND DISPLAYED HERE
                    for j in range(4):
                        self.table_data.setItem(i,j,QTableWidgetItem(str(l[i][j])))
            else:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo('Error','PROVIDE VALID DATA TYPE')       #IF INVALID SEARCH CRITERION
    def tablecount(self):                                                               #THIS FUNCTION DISPLAYS ALL DATA OF DB
        db=mysql.connector.connect(host="localhost",                                    #DB INITIALIZATION
                        user="root",
                        passwd="root",
                        database="test",
                        )
        cursorr=db.cursor()
        queryrow = "SELECT count(*) AS New_column_name FROM information_schema.columns where table_name = 'Systemm';"      #GETTING COLUMN
        cursorr.execute(queryrow)
        myresult = cursorr.fetchall()
        nrow=myresult[-1][-1]                                                           #GETTING ROW
        cursorr.execute("SELECT * FROM Systemm")
        ncol=len(cursorr.fetchall())
        self.table_data.setColumnCount(nrow)                                    #SETTING TABLE
        self.table_data.setRowCount(ncol)
        cursorr.execute("SELECT * FROM Systemm")
        x=cursorr.fetchall()
        for j in range(nrow):                                      #DISPLAYING TABLE DYNAMICALLY
            for i in range(ncol):
                self.table_data.setItem(i,j,QTableWidgetItem(str(list(x)[i][j])))
    def updatee(self):
        db=mysql.connector.connect(host="localhost",
                        user="root",
                        passwd="root",
                        database="test",
                        )
        cursorr=db.cursor(buffered=True)
        s=self.dep_combo.currentText()
        y=self.ys_combo.currentText()
        i=self.sid.text()
        n=self.sname.text()
        valid=False
        cursorr.execute("SELECT * FROM Systemm")
        if i.isnumeric() and n!="" and self.dep_combo.currentIndex()!=0 and self.ys_combo.currentIndex()!=0 and self.sid.text()!="":
            for j in cursorr:
                if j[2]==int(i):
                    valid=True
                    break
            if valid:
                ss="""UPDATE Systemm
        SET Department=%s, Year_Semester=%s,Student_name=%s
        WHERE Student_ID=%s"""
                cursorr.execute(ss,(s,y,n,int(i)))
                db.commit()
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo('Error',f'ID {i} was updated successfully!')
            if not valid:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo('Error','ID not found!')
        else:
           root = tk.Tk()
           root.withdraw()
           messagebox.showinfo('Error','Enter valid ID or proper data')
    def removee(self):                                                           #THIS  FUNCTION REMOVES USER FROM DATABASE AND ALSO REMOVES HIS/HER PICTURE FROM LOCAL STORAGE
        db=mysql.connector.connect(host="localhost",                             #INITIALISING DATABASE
                        user="root",
                        passwd="root",
                        database="test",
                        )
        cursorr=db.cursor(buffered=True)                                         #SETTING CURSOR
        s=self.dep_combo.currentText()
        y=self.ys_combo.currentText()
        i=self.sid.text()                                                        #GETTING ID OF USER TO DELETE
        n=self.sname.text()
        valid=False                                                              #FLAG TO CHECK IF ENTERED ID IS VALID
        cursorr.execute("SELECT * FROM Systemm")                                 #FETCH ALL DATA FROM DB
        if i.isnumeric():
            for j in cursorr:                                                    #LOOP THROUGH DATA
                if j[2]==int(i):
                    valid=True                                                   #IF ID IS VALID,SET valid TO True
                    break
            if valid:                                                            #IF VALID,DELETE ENTIRE COLUMN WHERE ID IS FOUND
                ss="""DELETE FROM Systemm
WHERE Student_ID=%s"""
                
                cursorr.execute(ss,(int(i),))
                db.commit()
                for m in os.listdir(f"{os.getcwd()}\\data"):                     #FINDING RESPECTIVE IMAGE AND DELETING IT FROM LOCAL STORAGE
                    iddd=m.split('.')[0].split('_')[0]
                    if int(iddd)==int(i):
                        os.remove(f"{os.getcwd()}\\data\\{m}")
                        break
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo('Error',f'ID {i} was removed successfully!')
            if not valid:                                                        #SHOW THIS IF ID IS ENTERED INVALID
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo('Error','ID not found!')
        else:
           root = tk.Tk()
           root.withdraw()
           messagebox.showinfo('Error','Enter valid ID')
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))   #STRING AND HTML PARSER STARTS
        self.title.setText(_translate("Dialog", "ATTENDANCE SYSTEM USING FACE RECOGNITION"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Register for system</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Student database</span></p></body></html>"))
        self.search_by.setItemText(0, _translate("Dialog", "Select"))
        self.search_by.setItemText(1, _translate("Dialog", "ID number"))
        self.search_by.setItemText(2, _translate("Dialog", "Year&Semester"))
        self.search_by.setItemText(3, _translate("Dialog", "Name"))
        self.search_by.setItemText(4, _translate("Dialog", "Department"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:400;\">Search by</span></p></body></html>"))
        item = self.table_data.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Department"))
        item = self.table_data.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Year & Semester"))
        item = self.table_data.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Student ID"))
        item = self.table_data.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Student Name"))
        self.search.setText(_translate("Dialog", "Search"))
        self.search_all.setText(_translate("Dialog", "Show all"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Department:</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Year &amp; semester:</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Student ID:</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Student name:</span></p></body></html>"))
        self.dep_combo.setItemText(0, _translate("Dialog", "Select department"))
        self.dep_combo.setItemText(1, _translate("Dialog", "CSE"))
        self.dep_combo.setItemText(2, _translate("Dialog", "MDMR"))
        self.dep_combo.setItemText(3, _translate("Dialog", "MPH"))
        self.ys_combo.setItemText(0, _translate("Dialog", "Select Year & Semester"))
        self.ys_combo.setItemText(1, _translate("Dialog", "1st Year & 1st Semester"))
        self.ys_combo.setItemText(2, _translate("Dialog", "1st Year & 2nd Semester"))
        self.ys_combo.setItemText(3, _translate("Dialog", "2nd Year & 1st Semester"))
        self.ys_combo.setItemText(4, _translate("Dialog", "2nd Year & 2nd Semester"))
        self.ys_combo.setItemText(5, _translate("Dialog", "3rd Year & 1st Semester"))
        self.ys_combo.setItemText(6, _translate("Dialog", "3rd Year & 2nd Semester"))
        self.ys_combo.setItemText(7, _translate("Dialog", "4th Year & 1st Semester"))
        self.ys_combo.setItemText(8, _translate("Dialog", "4th Year & 2nd Semester"))
##        self.take_photo_sample.setText(_translate("Dialog", "Take photo sample"))
##        self.no_photo_sample.setText(_translate("Dialog", "No photo sample"))
        self.save.setText(_translate("Dialog", "Save"))
        self.deletee.setText(_translate("Dialog", "Delete"))
        self.take_photo.setText(_translate("Dialog", "Take photo"))
        self.update.setText(_translate("Dialog", "Update"))
##        self.reset.setText(_translate("Dialog", "Reset"))
##        self.update_photo.setText(_translate("Dialog", "Update photo"))    #STRING AND HTML PARSER STARTS


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
