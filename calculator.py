'''
Andrew Grant
1/07/2024
Calculator with user interface
'''

from tkinter import *
import tkinter.font as font


class Interface():
    """Class for the GUI built with TK Inter"""

    def __init__(self, window):
        """Sets up the window, labels and layout"""
        self.__window = window
        self.__window.title("Calculator")
        self.__window.configure(background="black")

        self._FontSize = font.Font(size=20)

        # Widgets
        # Number Field
        self._calcZone = Entry(window, width=25, font='comic 20', borderwidth=5, relief="sunken")
        self._calcZone.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('X', 3, 3), ('÷', 4, 3),
            ('C', 4, 0), ('=', 4, 2)
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
            
        self.runCalc()
        self.bind_keys()

    def create_button(self, text, row, col):
        button = Button(self.__window, text=text, padx=20, pady=20, font=self._FontSize, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        if value == 'C':
            self._calcZone.delete(0, END)
        elif value == '=':
            try:
                expression = self._calcZone.get().replace('X', '*').replace('÷', '/')
                result = eval(expression)
                self._calcZone.delete(0, END)
                self._calcZone.insert(0, str(result))
            except:
                self._calcZone.delete(0, END)
                self._calcZone.insert(0, "Error")
        else:
            current_text = self._calcZone.get()
            self._calcZone.delete(0, END)
            self._calcZone.insert(0, current_text + value)

    def runCalc(self, _event=None):
        """Calculator running"""
        self._calcZone.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

    def bind_keys(self):
        """Bind keys to their corresponding functions"""
        keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', 'C', '=', 'Return', 'BackSpace']
        for key in keys:
            self.__window.bind(f'<KeyPress-{key}>', self.key_input)
        self.__window.bind('<Return>', self.key_input)
        self.__window.bind('<BackSpace>', self.key_input)

    def key_input(self, event):
        if event.char in '0123456789':
            self.button_click(event.char)
        elif event.char in '+-*/':
            if event.char == '*':
                self.button_click('X')
            elif event.char == '/':
                self.button_click('÷')
            else:
                self.button_click(event.char)
        elif event.keysym == 'C':
            self.button_click('C')
        elif event.keysym == 'Return':
            self.button_click('=')
        elif event.keysym == 'BackSpace':
            current_text = self._calcZone.get()
            self._calcZone.delete(0, END)
            self._calcZone.insert(0, current_text[:-1])

def main():
    """Main Runner for the program"""
    window.mainloop()

if __name__ =="__main__":
    window = Tk()
    Interface(window)
    main()
