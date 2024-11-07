import pandas as pd
import imp
import QR_Code_VCard_WC_copy
import imp
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
import os
from pathlib import Path

global current_path
current_path=Path.cwd()


def open_file():
    global file_path
    file_path = askopenfile(mode='r', filetypes=[('Excel', '*csv')])
    #print(file_path)
    file.set(os.path.basename(file_path.name))
    percent.set("")
    adhar.pack_forget()
    window.update_idletasks()
    if file_path or logo is not None:
        pass
def open_logo():
    global logo
    logo = askopenfile(mode='r')
    #print(file_path)
    image.set(os.path.basename(logo.name))
    percent.set("")
    adhar.pack_forget()
    button_status.set("Create QR Code")
    button.pack()
    window.update_idletasks()
    if logo or file_path is not None:
        pass
def close():
    window.quit()
    exit()
def start():
    #Path location
    if file_path == "":
        path=r"{current_path}/BR+A Bussiness Card/01_CSV/Employee Information.csv".format(current_path=current_path)
    else:
        path=r"{}".format(file_path.name)
    #Workbook Path
    global employee_data
    employee_data = pd.read_csv(path)

    #Creating QR Code
    global Employee_info
    global x
    x=0
    bar['value'] = 0
    percent.set("")
    for i in employee_data.itertuples():
        Employee_info=i
        x=x+1
        percentage = round((x/len(employee_data.index))*100)
        #print(percentage)
        
        file_total.set("QR Code(s) created: "+str(x))
        imp.reload(QR_Code_VCard_WC_copy)
        if percentage >= bar['value']+2:
            bar['value'] = percentage
             
        window.update_idletasks()
    try:
        bar['value'] = 100
        percent.set("QR Code(s) Created and CSV file Updated Succesfully !!!")
        window.update_idletasks()
        employee_data.to_csv(r"{current_path}/01_CSV/Employee Information.csv".format(current_path=current_path), index=False, sep=',')
        #print("QR Code(s) Created and CSV file Updated Succesfully !!!")
        button.pack_forget()
        button2.pack()
        button_status.set("Close")
        window.update_idletasks()
    except:
        
        #print("CSV file opened by another user and not updated!!! Please close csv file and restart script.")
        percent.set("CSV file opened by another user and not updated!!! Please close csv file and restart script.")
        button_status.set("Try again")
        window.update_idletasks()
        

    #exit()

#Window Interface
window = Tk()

window.title("BR+A-Virtual QR Code Generator")
window.geometry("400x200")
percent = StringVar()
file = StringVar()
image = StringVar()
file_total = StringVar()
button_status = StringVar()
file.set('Choose File')
image.set('Choose Background')
button_status.set("Create QR Code(s)")


Title_label = Label(window, text="Virtual QR Code Generator").pack()
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10,padx=10)

percent_label = Label(window, textvariable=percent)
percent_label.pack()
file_label = Label(window, textvariable=file_total).pack()


adhar = Label(window,text='Upload Excel')
adhar.pack()

adharbtn = Button(window,textvariable=file,command=lambda: open_file())
adharbtn.pack()
adharbtn = Button(window,textvariable=image,command=lambda: open_logo())
adharbtn.pack()


button = Button(window,textvariable=button_status, command=start)
button2 = Button(window,textvariable=button_status, command=close)




window.mainloop()
window.quit()
exit()
