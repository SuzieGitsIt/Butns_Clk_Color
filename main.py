# https://stackoverflow.com/questions/65325062/change-colour-of-tkinter-button-created-in-a-loop
# https://www.plus2net.com/python/tkinter-button.php
# https://www.programiz.com/python-programming/if-elif-else
# https://stackoverflow.com/questions/74412503/cannot-access-local-variable-a-where-it-is-not-associated-with-a-value-but

#################################################      CLASSES OF LIBRARIES TO USE      ################################################  
import tkinter as tk                                    # Tkinter's Tk class
import tkinter.ttk as ttk                               # Tkinter's Tkk class
from PIL import ImageTk, Image

#################################################      INITIALIZING STANDARD DISPLAY     ################################################# 
GUI = tk.Tk()
GUI.title("LAL Measurement")
GUI.geometry("600x300")                                 # Set the geometry of Tkinter frame
GUI.configure(bg = 'white')                             # Set background color
GUI.option_add("*Font", "Helvetica 12 bold")            # set the font and size for entire GUI
GUI.option_add("*fg", "black")                          # set the text color, hex works too "#FFFFFF"
GUI.option_add("*bg", "white")                          # set the background to white

#################################################            BUTTON PRESS STYLE           ################################################ 
style = ttk.Style();        # style must be spelled out and cannot be .s
style.theme_use('clam'); # 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'
style.configure('T.Button',borderwidth='20')            # This is for ttk.Label
style.configure('T.Button',highlightthickness='10')     # This is for ttk.Label
style.configure('T.Button',highlightcolor='pink')       # This is for ttk.Label
style.map('T.TButton',background=[('active', 'pressed', 'cyan'),('!active','white'), ('active','!pressed','grey')]) # active, not active, not pressed
style.map('T.TButton',foreground=[('active', 'pressed', 'blue'),('!active','black'), ('active','!pressed','white')]) # active, not active, not pressed
#style.map('T.TButton',relief    =[('pressed','sunken'),('!pressed','raised')]) # pressed, not pressed

#################################################           LAL BACKGROUND IMAGE          ################################################  
def resize_image(event):
    new_width = event.width
    new_height = event.height
    background_image = copy_of_image.resize((new_width, new_height))
    bkgnd_img = ImageTk.PhotoImage(background_image)
    lbl_photo.config(image = bkgnd_img)
    lbl_photo.background_image = bkgnd_img                                          # avoid garbage collection

background_image = Image.open(r"C:\Users\Susan\OneDrive\Documents\Python/LAL.png")
copy_of_image = background_image.copy()
bkgnd_img = ImageTk.PhotoImage(background_image)

lbl_photo = ttk.Label(GUI, image = bkgnd_img)
lbl_photo.bind('<Configure>', resize_image)
lbl_photo.pack(fill=tk.BOTH, expand = True)

# Python is serial, so each widget will output in the order listed below;
#################################################             MAIN BODY               ################################################  
# Display the command label before the entry box to indicate what information the Opterator is to type
lbl_cmd_cred = tk.Label(text="Enter Operator Credentials:", bg="White", width= 20).place(x=50,y=50) 
lbl_cmd_WO   = tk.Label(text="Enter Work Order Number:",    bg="White", width= 20).place(x=50,y=100)   
# Entry boxes to take information from operator
entry_cred = tk.Entry(GUI, bg= "white", width= 10) 
entry_cred.focus_set()                                                      # Places cursor in the first entry box.
entry_cred.place(x=250,y=50) 
entry_WO   = tk.Entry(GUI, bg= "white", width= 10) 
entry_WO.place(x=250,y=100) 
# Display the inputs as outputs
lbl_disp_cred = tk.Label(GUI, text="Credentials:",       bg= "white", width= 9) .place(x=50, y=200) 
lbl_disp_WO   = tk.Label(GUI, text="Work Order Number:", bg= "white", width= 16).place(x=50, y=250) 
# Display the user inputs as outputs 
lbl_out_cred = tk.Label(GUI, text= "", bg= "white", width= 3) 
lbl_out_cred.place(x=200, y=200) 
lbl_out_WO   = tk.Label(GUI, text= "", bg= "white", width= 10)
lbl_out_WO.place(x=200, y=250) 
# Display user inputs
def display_cred(): 
   global entry 
   cred = entry_cred.get()[:3]                                              # entry_cred is the variable we are passing. Limit 3 characters
   lbl_out_cred.configure(text = cred)
   print(entry_cred.get()[:3])                                              # Print can be removed after developed.

def display_WO():                        
   global entry 
   WO = entry_WO.get()[:10]                                                 # entry_WO is the variable we are passing. Limit 10 characters
   lbl_out_WO.configure(text = WO) 
   print(entry_WO.get()[:10]) 

###########################################################  TEST SCRIPT  ###############################################################
btn_pres_cnt = 0   
def pink(event):                     
    global btn_pres_cnt                                                     # initializing btn_pres_cnt as a global varaible so that it adds through every iteration
    if(btn_pres_cnt==5 or btn_pres_cnt==10 or btn_pres_cnt==15 or btn_pres_cnt==20 or btn_pres_cnt==25):            # button turns pink when btn_pres_cnt=100, and =200 and = 300.
        style.map('T.TButton',background=[('active', 'pressed', '#FF69B4'),('!active','white'), ('active','!pressed','grey')]) # active, not active, not pressed
    else:
        style.map('T.TButton',background=[('active', 'pressed', 'cyan'),('!active','white'), ('active','!pressed','grey')])
    print("btn_pres_cnt = ", btn_pres_cnt)                                  # This is always executed at the end of the if else
    btn_pres_cnt +=1                                                        # This is always executed at the end of the if else

btn_cred = ttk.Button(GUI, text= "Confirm", style='T.TButton', width= 10, command= display_cred)    # button must have ttk. in order to have style.
btn_cred.bind("<Button-1>", pink)
btn_cred.place(x=350,y=50)  

btn_WO   = ttk.Button(GUI, text= "Confirm", style='T.TButton', width= 10, command= display_WO)
btn_WO.bind("<Button-1>", pink)
btn_WO.place(x=350,y=100)  

GUI.mainloop()  
