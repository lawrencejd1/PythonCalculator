import tkinter as tk
from tkinter.ttk import *

class Calculator:

    def main(self):
    #Window Dimensions and Location
        width = 400
        height = 625
        positionX = 100
        positionY = 100

    #Window Creation
        window = tk.Tk()

    #Things being calculated and values stored
        self.entryText = ""
        self.entryOperator = ""
        self.firstClick = True #Decides if user pushed a function button already
        self.clearAll = False
    #EntryBox creation and validating int-only input
        #vcmd = (window.register(self.isInt), '%S')
        #validate="key", vcmd=vcmd
        self.entryBox = tk.Entry(window, state="readonly", font="Arial_Black 50", disabledbackground="grey", bd=0, highlightthickness=0)
        self.entryBox.focus()
        self.entryBox.place(x=5,y=5, width=width-10, height=115)

    #Button Creation

        numberButtons = []

        buttonWidth = 100
        buttonHeight = 125

        #Button Numbers
        zeroBtnX = width/4
        ZeroBtnY = height-buttonHeight

        #Place buttons on screen depending on the button number
        for num in range(10):
            buttonText = f"{num}"
            button = Button(window, text=buttonText, command=lambda j=num: self.ButtonPressed(j))
            numberButtons.append(button)

            if(num == 0):

                button.place(x=zeroBtnX, y=ZeroBtnY, width=buttonWidth, height=buttonHeight)

            elif(num > 0 and num <=3):

                if(num == 1):
                    startX = 0
                    startY = height-(buttonHeight*2)
                    button.place(x=startX, y=startY, width=buttonWidth, height=buttonHeight)
                    startX += 100
                else:
                    button.place(x=startX, y=startY, width=buttonWidth, height=buttonHeight)
                    startX += 100

            elif(num > 3 and num <=6):

                if(num == 4):
                    startX = 0
                    startY = height-(buttonHeight*3)
                    button.place(x=startX, y=startY, width=buttonWidth, height=buttonHeight)
                    startX += 100
                else:
                    button.place(x=startX, y=startY, width=buttonWidth, height=buttonHeight)
                    startX += 100
            
            elif(num > 6 and num <=9):

                if(num == 7):
                    startX = 0
                    startY = height-(buttonHeight*4)
                    button.place(x=startX, y=startY, width=buttonWidth, height=buttonHeight)
                    startX += 100
                else:
                    button.place(x=startX, y=startY, width=buttonWidth, height=buttonHeight)
                    startX += 100


        #Function Buttons

        #Plus
        plusBtn = Button(window, text="+", command=lambda j="+": self.ButtonPressed(j))
        plusBtn.place(x=300, y=125, width=buttonWidth, height=buttonHeight)
        numberButtons.append(plusBtn)

        #Minus
        minusBtn = Button(window, text="-", command=lambda j="-": self.ButtonPressed(j))
        minusBtn.place(x=300, y=250, width=buttonWidth, height=buttonHeight)
        numberButtons.append(minusBtn)

        #Multiply
        multiplyBtn = Button(window, text="*", command=lambda j="*": self.ButtonPressed(j))
        multiplyBtn.place(x=300, y=375, width=buttonWidth, height=buttonHeight)
        numberButtons.append(multiplyBtn)

        #Divide
        divideBtn = Button(window, text="/", command=lambda j="/": self.ButtonPressed(j))
        divideBtn.place(x=300, y=500, width=buttonWidth, height=buttonHeight)
        numberButtons.append(divideBtn)

        #Equal
        equalBtn = Button(window, text="=", command=lambda j="=": self.equalPressed(j))
        equalBtn.place(x=200, y=500, width=buttonWidth, height=buttonHeight)
        numberButtons.append(equalBtn)

        #Clear
        clearBtn = Button(window, text="Clear", command=lambda j="Clear": self.clearPressed(j))
        clearBtn.place(x=0, y=500, width=buttonWidth, height=buttonHeight/3)
        numberButtons.append(clearBtn)

        #Parenthesis
            #Left
        leftParentBtn = Button(window, text="(", command=lambda j="(": self.parentPressed(j))
        leftParentBtn.place(x=0, y=(500+(buttonHeight/3)), width=buttonWidth/2, height=buttonHeight/3)
        numberButtons.append(leftParentBtn)

            #Right
        rightParentBtn = Button(window, text=")", command=lambda j=")": self.parentPressed(j))
        rightParentBtn.place(x=50, y=(500+(buttonHeight/3)), width=buttonWidth/2, height=buttonHeight/3)
        numberButtons.append(rightParentBtn)

        #Negative
        negativeBtn = Button(window, text="(-)", command=lambda j="(-)": self.negativePressed(j))
        negativeBtn.place(x=0, y=(500+((buttonHeight/3)*2)), width=buttonWidth, height=buttonHeight/3)
        numberButtons.append(negativeBtn)

        #Window
        window.title('Python Calculator Using Tkinter')
        window.geometry(f"{width}x{height}+{positionX}+{positionY}")
        window.mainloop()

    #If a number or operator buttons are clicked
    def ButtonPressed(self, text):

        text = str(text)
        self.entryBox.configure(state="normal")

        #Checks if int or operator
        if(self.isInt(text)):

            self.entryText += text
            self.entryBox.insert(tk.END, text)

        elif(self.isOperator(text) and self.isOperator(self.entryText[-1]) != True):

            self.entryOperator = text
            self.entryText += text

        else:pass

        #Prevents consecutive function buttons from being used

        lastChar = self.entryText[-1]

        if(self.entryText != ""):
            
            if(self.isOperator(self.entryText[-1]) == True and self.isOperator(text) == True and self.firstClick == False):
                self.entryText = self.entryText[:-1]
                self.entryText += text
                print("reset? yes")

            elif( (self.isOperator(self.entryText[-1]) == True) and (self.firstClick == True)):    
                self.entryBox.delete(0, 'end')
                self.entryText.replace(lastChar, text)
                self.firstClick = False
                print("reset? no")
        
            else:pass
        #----------------------------------------------------

        self.entryBox.configure(state="readonly")

    def isInt(self, S):
        if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        return False

    def isOperator(self, S):
        if S in ['+', '-', '*', '/']:
            return True
        return False

    def equalPressed(self, text):
        self.entryBox.configure(state="normal")
        self.total = eval(self.entryText)
        self.entryBox.delete(0, tk.END)
        self.entryBox.insert(tk.END, self.total)
        self.entryText = str(self.total)
        self.firstClick = True
        self.clearAll = False
        self.entryBox.configure(state="readonly")

    def clearPressed(self, text):

        if(self.clearAll == False):
            self.entryBox.configure(state="normal")
            self.entryBox.delete(0, tk.END)
            self.entryBox.insert(tk.END, "")

            while(True):
                print(self.entryText)
                try:
                    if(self.isOperator(self.entryText[-1]) != True):
                        self.entryText = self.entryText[:-1]
                    else:
                        break
                except IndexError:
                    print("No more values")
                    break


            self.firstClick = True
            self.clearAll == True
            self.entryBox.configure(state="readonly")
        elif(self.clearAll == True):
            self.entryBox.configure(state="normal")
            self.entryBox.delete(0, tk.END)
            self.entryBox.insert(tk.END, "")
            self.entryText = ""
            self.firstClick = False
            self.clearAll == False
            self.entryBox.configure(state="readonly")
        else:pass
    
    def parentPressed(self, text):
        pass

    def negativePressed(self, text):
        pass


if __name__ == "__main__":
    calc = Calculator()
    calc.main()


