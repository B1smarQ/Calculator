import tkinter as tk

win = tk.Tk()
InputField = tk.Entry(win,justify= tk.RIGHT)
InputField.grid(row = 0, column= 0, columnspan=4,sticky = 'we')

def addDigit(number):
    value = InputField.get()
    if value[0] == '0':
        value = value[1:]
    InputField.delete(0,tk.END)
    InputField.insert(0, value+str(number))
def AddOperation(operation):
    value = InputField.get()
    if value[-1] in '+-/*' :
        value = value[:-1]
    InputField.delete(0,tk.END)
    InputField.insert(0,value+operation)
def calculate():
    value = InputField.get()
    InputField.delete(0,tk.END)
    InputField.insert(0,eval(value))
InputField.insert(0,'0')
btn_1 = tk.Button(win,text = '1',command = lambda:addDigit(1)).grid(row=1,column=0,sticky='wens')
btn_2 = tk.Button(win,text = '2',command = lambda:addDigit(2)).grid(row=1,column=1,sticky='wens')
btn_3 = tk.Button(win,text = '3',command = lambda:addDigit(3)).grid(row=1,column=2,sticky='wens')
btn_4 = tk.Button(win,text = '4',command = lambda:addDigit(4)).grid(row=2,column=0,sticky='wens')
btn_5 = tk.Button(win,text = '5',command = lambda:addDigit(5)).grid(row=2,column=1,sticky='wens')
btn_6 = tk.Button(win,text = '6',command = lambda:addDigit(6)).grid(row=2,column=2,sticky='wens')
btn_7 = tk.Button(win,text = '7',command = lambda:addDigit(7)).grid(row=3,column=0,sticky='wens')
btn_8 = tk.Button(win,text = '8',command = lambda:addDigit(8)).grid(row=3,column=1,sticky='wens')
btn_9 = tk.Button(win,text = '9',command = lambda:addDigit(9)).grid(row=3,column=2,sticky='wens')
btn_0 = tk.Button(win,text = '0',command = lambda:addDigit(0)).grid(row=4,column=0,columnspan=3,sticky='wens')
btn_minus = tk.Button(win,text = '-',command = lambda:AddOperation('-')).grid(row=1,column=3,sticky='wens')
btn_plus = tk.Button(win,text = '+',command = lambda:AddOperation('+')).grid(row=2,column=3,sticky='wens')
btn_multiply = tk.Button(win,text = '*',command = lambda:AddOperation('*')).grid(row=3,column=3,sticky='wens')
btn_divide = tk.Button(win,text = '/',command = lambda:AddOperation('/')).grid(row=4,column=3,sticky='wens')
btn_result = tk.Button(win,text = '=',command = lambda:calculate()).grid(row=5,column=0,sticky='wens',columnspan=4)
btn_clear = tk.Button(win,text = 'Clear', command = lambda:InputField.delete(0,tk.END)).grid(row=6,column=0,sticky='wens',columnspan=4)
win.columnconfigure(0,minsize=60)
win.columnconfigure(1,minsize=60)
win.columnconfigure(2,minsize=60)
win.columnconfigure(3,minsize=60)
win.rowconfigure(0,minsize=60)
win.rowconfigure(1,minsize=60)
win.rowconfigure(2,minsize=60)
win.rowconfigure(3,minsize=60)
win.rowconfigure(4,minsize=60)
win.rowconfigure(5,minsize=60)
win.rowconfigure(6,minsize=60)
win.mainloop()
