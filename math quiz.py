''' importing all modules from tkinter'''
from tkinter import *

''' Declare parent class called MathsQuiz, All objects created from parent class'''
class MathsQuiz:
    ''' use init method for all widgets'''
    def __init__(self,parent):
        
        '''Widget for Welcome Frame '''
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        self.TitleLable = Label(self.Welcome, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.TitleLable.grid(columnspan = 2)
        
        self.NextBUtton = Button(self.Welcome, text = 'Next', command = self.show_Questions)
        self.NextBUtton.grid(row = 8, column = 1)
        
        ''' Widgets for questions frame'''
        
        self.Questions = Frame(parent)
        #self.Questions.grid(row=0, column=1)
        
        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)
        
        self.HomeButton = Button(self.Questions, text = 'Next', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 1)
        
        ''' a method that removes quesitons frame'''
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()
            
#Main Routine
if __name__ == "__main__":
    root =Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()
        