#Import tkinter library 
from tkinter import*
from tkinter import ttk
from unittest import result
from unitconvert import digitalunits
from tkinter import messagebox

# create an istance of tkinter frame or window
root=Tk()
root.title('Digital Unit Converter')

# Set the geometry of tkinter frame 
root.geometry('600x460+0+0')

#=== Function ===
def digitalUnitConvert():
    if userin.get()=="" or unitfrom.get()=='Select Unit' or unitto.get()=='Select Unit':
        messagebox.showerror('Error:','Please Select Unit to convert', parent=root)
    else:
        try:
            formulaDunit = digitalunits.DigitalUnit(userin.get(),f'{unitfrom.get()}',f'{unitto.get()}').doconvert()
            result.set(formulaDunit)
        except Exception as es:
            messagebox.showerror('Error', f'Due to:{str(es)}', parent=root)
            
#===Function for Reset ===
def resetData():
    userin.set("")
    result.set("")
    unitfrom.set('Select Unit')
    unitto.set('Select Unit')
            
          
        

#=== Variables ===
userin=IntVar()
unitfrom = StringVar()
unitto =StringVar()
result= IntVar()


#=== Top label ===
top_lbl = Label(root,text='Digital Memory Unit Converter', font=('arial',15,'bold'),fg='blue')
top_lbl.place(x=194,y=10)

#=== Main frame ===
main_frame = Frame(root, bd=2, relief=RIDGE,bg='dark blue')
main_frame.place(x=0,y=50,width=800,height=460)
#=== Top label in main frame ===
label_1 = Label(main_frame,text='Enter Value To Convert',font=('arial',18,'bold'), fg='white',bg='dark blue')
label_1.place(x=177,y=20)

#=== Entry field for user input ===
userinput = ttk.Entry(main_frame, textvariable=userin,font=('arial',16), width=20)
userinput.place(x=182,y=60)

#=== Label for 'From' & Combobox ===
lbl_from = Label(main_frame, text='From', font=('arial',16,'bold'), fg='white',bg='dark blue')
lbl_from.place(x=180,y=100)

#=== combobox ==
unitfirst = ttk.Combobox(main_frame,textvariable=unitfrom, font=('arial',16),width=10,state='readonly')
unitfirst['value'] = ('Select Unit','B','KB','KiB','MB','Mib','GB','GiB','TB','TiB','PB','PiB','EB','EiB','ZB','ZiB','YB','YiB')
unitfirst.current(0)
unitfirst.place(x=280,y=100)

#== Lable for 'To' & Combobox==
lbl_to = Label(main_frame, text='To', font=('arial',16,'bold'),fg='white',bg='dark blue')
lbl_to.place(x=180,y=145)

unitsecond = ttk.Combobox(main_frame,textvariable=unitto,font=('arial',16),width=10,state='readonly')
unitsecond ['value'] =('Select Unit','B','KB','KiB','MB','Mib','GB','GiB','TB','TiB','PB','PiB','EB','EiB','ZB','ZiB','YB','YiB')
unitsecond.current(0)
unitsecond.place(x=280,y=145)

# === Result Label & Entry ====
lbl_result = Label(main_frame,text='Result', font=('arial',16,'bold'),fg='white',bg='dark blue')
lbl_result.place(x=180,y=200)

result_disply= Label(main_frame,textvariable=result,font=('arial',16,'bold'),fg='blue')
result_disply.place(x=280,y=200)

#== Button- Convert ===
btn_convert = Button(main_frame,text='Convert', font=('arial',16,'bold'),command=digitalUnitConvert)
btn_convert.place(x=180,y=250)

#=== Button - Reset ==
btn_reset= Button(main_frame,text='Reset',font=('arial',16,'bold'),command=resetData)
btn_reset.place(x=330,y=250)

#=== Bottom Frame ===
bottom_frame = LabelFrame(main_frame,text='Developer Info', bd=2,relief=RIDGE,font=('arial',14),fg='white',bg='dark blue')
bottom_frame.place(x=3,y=320,width=592,height=80)

lbl = Label(bottom_frame,text='Email:yusufphysicist01@gmail.com',font=('arial',12,'bold'),fg='white',bg='dark blue')
lbl.place(x=50,y=10)



root.mainloop()