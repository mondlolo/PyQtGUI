import sys
from PyQt4 import QtGui,QtCore
from random import *

class GuessingGame(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)                                              
        self.setGeometry(250,250,400,300)
        self.setWindowTitle("Guessing Game")
        #self.setLayout(QtGui.GridLayout())
        self.setPalette(QtGui.QPalette(QtGui.QColor("Yellow")))
        
        '''Create buttons'''
        
        guess = QtGui.QPushButton("Guess")
        guess.setMinimumSize(80,20)
        guess.setMaximumSize(100,25)
        change = QtGui.QPushButton("Change")
        change.setMinimumSize(80,20)
        change.setMaximumSize(100,25)
        newGame = QtGui.QPushButton("New Game")
        newGame.setMinimumSize(80,20)
        newGame.setMaximumSize(100,25)
        close = QtGui.QPushButton("Close") 
        close.setMinimumSize(80,20)
        close.setMaximumSize(100,25)
        
        '''Create Labels'''
        guessHeading = QtGui.QLabel("Guesses:",self)
        interfaceHeading = QtGui.QLabel("Interface:",self)
        guessHeading.setFont(QtGui.QFont('Times',20,2))
        interfaceHeading.setFont(QtGui.QFont('Times',20,2))        
        Guess1 = QtGui.QLabel('Guess1:',self)
        Guess2 = QtGui.QLabel('Guess2:',self)
        Guess3 = QtGui.QLabel('Guess3:',self)
        
        self.pictureLabel = QtGui.QLabel('Picture:',self)
        self.colorLabel = QtGui.QLabel('Color:',self)
        
        # Picture
        self.pixMap = QtGui.QPixmap("pluto.gif") 
        self.picLabel = QtGui.QLabel() 
        self.picLabel.setPixmap(self.pixMap)
        
        '''Create Line eddit'''             # take Note
        self.GuessEdit = QtGui.QLineEdit()
        
        self.dispText_1 = QtGui.QLabel("")
        self.dispText_12 = QtGui.QLabel("")
        
        self.dispText_2 = QtGui.QLabel("")
        self.dispText_21 = QtGui.QLabel("")
        
        self.dispText_3 = QtGui.QLabel("")
        self.dispText_31 = QtGui.QLabel("")
        
        #self.userInput = self.GuessEdit.displayText()
        
        #self.dispText_1.setText(self.userInput)
        #self.GuessEdit.clear()
        
        
        
        '''Create combo'''
        self.pic_combo = QtGui.QComboBox()
        self.pic_combo.addItem("mickey")
        self.pic_combo.addItem("pluto")
        
        self.color_combo = QtGui.QComboBox()
        self.color_combo.addItem("red")
        self.color_combo.addItem("blue")
        
        '''Insert into grid'''
        grid = QtGui.QGridLayout()
        grid.addWidget(self.picLabel,0,0,8,2) # keep Track
        grid.addWidget(guessHeading,0,2)
        
        '''adding the labels'''
        
        grid.addWidget(self.dispText_1,1,3)
        grid.addWidget(self.dispText_12,1,4)
        grid.addWidget(self.dispText_2,2,3)
        grid.addWidget(self.dispText_21,2,4)
        grid.addWidget(self.dispText_3,3,3)
        grid.addWidget(self.dispText_31,3,4)
        
        grid.addWidget(Guess1,1,2)
        grid.addWidget(Guess2,2,2)
        grid.addWidget(Guess3,3,2)
        grid.addWidget(self.GuessEdit,4,3)
        grid.addWidget(guess,4,4)
        grid.addWidget(interfaceHeading,5,2)
        grid.addWidget(self.pictureLabel,6,2)
        grid.addWidget(self.pic_combo,6,3)
        grid.addWidget(self.colorLabel,7,2)
        grid.addWidget(self.color_combo,7,3)
        grid.addWidget(change,7,4)
        grid.addWidget(close,8,2)
        grid.addWidget(newGame,8,3)
        self.setLayout(grid)
        self.gCounter = 3
        self.randNum = 0
        
        '''Event handling '__close__' button'''
        close.clicked.connect(self.cancelButton)
        change.clicked.connect(self.changeButton)
        guess.clicked.connect(self.guessButton)
        newGame.clicked.connect(self.newGameButton)
        
        ''''__ColorCombo__'''''
        
        
        
    def cancelButton(self):
        self.close()
        
    def changeButton(self):
        colorOption = self.color_combo.currentText()
        picOption = self.pic_combo.currentText()
        
        if colorOption =="red" and picOption == "mickey":
            self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
            self.pixMap = QtGui.QPixmap("mickey.gif")
            self.picLabel.setPixmap(self.pixMap)
            
        elif colorOption =="blue" and picOption == "mickey":
            self.setPalette(QtGui.QPalette(QtGui.QColor("blue")))
            self.pixMap = QtGui.QPixmap("mickey.gif")
            self.picLabel.setPixmap(self.pixMap)
            
        elif colorOption =="blue" and picOption == "pluto":
            self.setPalette(QtGui.QPalette(QtGui.QColor("blue")))
            self.pixMap = QtGui.QPixmap("pluto.gif") 
            self.picLabel.setPixmap(self.pixMap)
            
        elif colorOption =="red" and picOption == "pluto":
            self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
            self.pixMap = QtGui.QPixmap("pluto.gif")  
            self.picLabel.setPixmap(self.pixMap)
            
    '''def newGameButton(self):
           
    
    '''
        
        
    
    def guessButton(self):
        '''create random number generator'''
        randzu = randint(1,11)  
        #randzu = 3
        '''method to set random number only when there is a new game. (i.e new game begins when there gCounter(chances) is equal to three )'''
        if self.gCounter ==3:
            self.randNum = randzu
        userInput = self.GuessEdit.displayText()
        self.GuessEdit.clear()
        
        if int(userInput) == self.randNum:
            
            if self.gCounter == 3:
                self.dispText_1.setText(userInput)
                self.dispText_12.setText("Correct!")
                self.gCounter += 1          # add 1 and the gounter increases to 4, that avoids the program to continue when a person has a correct guess as the
                                            # programme is not evaluated
                #print(self.gCounter)
            elif self.gCounter == 2:
                self.dispText_2.setText(userInput)
                self.dispText_21.setText("Correct!")
                self.gCounter += 2          # add 1 and the gounter increases to 4, that avoids the program to continue when a person has a correct guess
            elif self.gCounter == 1:
                self.dispText_3.setText(userInput)
                self.dispText_31.setText("Correct!")
                self.gCounter += 3
        elif int(userInput) > self.randNum:
            if self.gCounter == 3:
                self.dispText_1.setText(userInput)
                self.dispText_12.setText("To Big!")
                self.gCounter -=1
            elif self.gCounter == 2:
                self.dispText_2.setText(userInput)
                self.dispText_21.setText("To big!")
                self.gCounter -= 1
            elif self.gCounter == 1:
                self.dispText_3.setText(userInput)
                self.dispText_31.setText("To big!")
                self.gCounter -= 1  
    
        elif int(userInput) < self.randNum:
            if self.gCounter == 3:
                self.dispText_1.setText(userInput)
                self.dispText_12.setText("To small!")
                self.gCounter -=1
            elif self.gCounter == 2:
                self.dispText_2.setText(userInput)
                self.dispText_21.setText("To small!")
                self.gCounter -=1
            elif self.gCounter == 1:
                self.dispText_3.setText(userInput)
                self.dispText_31.setText("To small!")
                self.gCounter -=1 
    
    '''function to control the new game button'''
    def newGameButton(self):
        
        self.dispText_1.clear()
        self.dispText_12.clear()
        
        self.dispText_2.clear()
        self.dispText_21.clear()
        
        self.dispText_3.clear()
        self.dispText_31.clear()
        self.gCounter = 3
        
    
      
        #userInput = self.GuessEdit.displayText() 
        #self.dispText.setText(userInput)
        #self.GuessEdit.clear()
        
        '''guessNum2 = self.userInput = self.GuessEdit.displayText() 
        self.dispText.setText(guessNum2)
        self.GuessEdit.clear()     
        
        guessNum3 = self.userInput = self.GuessEdit.displayText() 
        self.dispText.setText(guessNum3)
        self.GuessEdit.clear()'''        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    theGame = GuessingGame()
    theGame.show()
    sys.exit(app.exec_())
main()