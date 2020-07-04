from PyQt5 import QtCore, QtGui, QtWidgets
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import time
from selenium import webdriver

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 587)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 430, 391, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEdit.setPalette(palette)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit.returnPressed.connect(self.enter)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 20, 601, 391))
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 470, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))

    def enter(self):
        question = self.lineEdit.text()
        self.textEdit.append(">>> User : ")
        self.textEdit.append(question)
        self.lineEdit.clear()
        question.strip()
        response = "Oops! Sorry, something went wrong! Try again"
        if (question.isspace() == False) and (question != ""):
            response = chatbot_response(question)
            import responses
            if (response == "Courses") :
                response = responses.open_UV('nsassine', "Naim/98")
            elif (response == "Schedule") :
                response = responses.open_gehol('nsassine', "Naim/98")
            elif (response == "Grades") :
                response = responses.show_grades('nsassine', "Naim/98")
            elif (response == "GInformation") :
                response = responses.get_more_info()
            elif (response == "SInformation") :
                response = responses.studies_information()
            elif (response == "Erasmums") :
                response = responses.erasmums_information()
            elif (response == "Applications") :
                response = responses.application_information()
            elif (response == "Research") :
                response = responses.phd_information()
            elif (response == "Engagement") :
                response = responses.engagement_information()
            elif (response == "SLife") :
                response = responses.student_life_information()
            elif (response == "Greeting") :
                response = responses.greeting()
            elif (response == "Howudoin") :
                response = responses.howudoin()
            elif (response == "GoodBye") :
                response = responses.goodbye()
            elif (response == "Thanks") :
                response = responses.thanks()
            elif (response == "NoAnswer") :
                response = responses.noanswer()
            elif (response == "Options") :
                response = responses.options()
            elif (response == "Food") :
                response = responses.food()
        else :
            response = "Don't be shy! Type in your question"
        self.textEdit.append(">>> SAL_BOT : ")
        self.textEdit.append(response)


class First_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 567)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 300, 211))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.netID = QtWidgets.QTextEdit(self.centralwidget)
        self.netID.setGeometry(QtCore.QRect(220, 350, 131, 31))
        self.netID.setAutoFillBackground(False)
        self.netID.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.netID.setObjectName("netID")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(210, 470, 151, 51))
        self.signInButton.setObjectName("signInButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 400, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 350, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 400, 81, 31))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Welcome</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Welcome to SAL!</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">The ULB\'s first ChatBot!</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ready to ask some questions?</span></p></body></html>"))
        self.netID.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.signInButton.setText(_translate("MainWindow", "Let\'s Go!"))
        self.label_2.setText(_translate("MainWindow", "         NetID : "))
        self.label_3.setText(_translate("MainWindow", "    Password : "))



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = Ui_MainWindow()
        self.uiFirstWindow = First_Window()
        self.startuiFirstWindow()

    def startuiFirstWindow(self):
        self.uiFirstWindow.setupUi(self)
        self.uiFirstWindow.signInButton.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.uiWindow.setupUi(self)
        self.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
