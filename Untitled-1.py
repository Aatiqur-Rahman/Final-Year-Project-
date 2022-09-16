from cgitb import text
from fileinput import filename
import imp
from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk 
import os 
from stegano import lsb #pip install stegano
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from RSA import gen_prime
from Stegano import Insert_using_cv2
from Stegano import decryption
import cv2

root=Tk()
root.title("Steganography Hide a Secret Text Message in an Image")
root.geometry("1200x700+100+100") 

encrypted_value = list ()
binary_value=list()
binary_value_extract = list()
text_ascii = list()

def showimage():
    
    f_types = [('Jpg Files', '*.jpg'),('PNG files' , '*.png')]
    global filename 
    filename = filedialog.askopenfilename(filetypes=f_types)
    print ("after open "+filename )
    global img
    img = Image.open(filename)
    
    #img.resize ((100,100) , Image.ANTIALIAS)+
    img = ImageTk.PhotoImage(img.resize ((497,497) , Image.ANTIALIAS))
    
    label = Label(f, image = img )
    label.pack()
    #b2 =tk.Button(root,image=img) # using Button 
    #b2.grid(row=3,column=1)

def Encrypt(): 
    
    msg = text1.get(1.0, 'end-1c') # take input 
    gen_prime.main()
    temp = gen_prime.msg_encryption(msg)
    for x in temp : 
        encrypted_value.append(x)
     
def Decrypt():
    print (cipher_ascii)
    gen_prime.main()
    text_ascii = gen_prime.msg_decryption(cipher_ascii)
    decryption.int_to_ascii(text_ascii)
def save():
    f_types = [('PNG files' , '*.png')]
    file = filedialog.asksaveasfilename(filetypes=f_types)
    print (file)
    print (im)
    cv2.imwrite(file,im)
    print ("stego image is created ")
def Hide():
    global im
    path = filename 
    im = cv2.imread(path,1) # Reding image in RGB mode 
    
    #cv2.imshow("Stego Image",img)
    #cv2.waitKey(0)
    img_shape = im.shape
    print (img_shape)
    print (im)
    print("Shape of image :: __________________" , img_shape)

    binary_value =  Insert_using_cv2.msg_conversion(encrypted_value)
    sizeofmsg = len ( binary_value ) 
    print (sizeofmsg)
    Insert_using_cv2.main (im,img_shape,sizeofmsg)
    Insert_using_cv2.red_pxl ()
    print (im)

def Extract() : 
    path = filename
    print ("extract filename " + filename )
    st_img = cv2.imread(path,1) 
    print (st_img)
    img_shape = st_img.shape
    sizeofmsg =  int ( text5_1.get(1.0, 'end-1c') ) 
    decryption.main (st_img,img_shape,sizeofmsg*8)
    binary_value_extract = decryption.red_pxl()
    print (binary_value_extract)
    global cipher_ascii
    cipher_ascii = decryption.decrypt()
    
    

#icon
image_icon=PhotoImage(file="logo.jpg") 
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png") 
Label(root,image=logo, bg="#2f4155").place(x=10,y=0)

Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

#first Frame
f=Frame (root, bd=3, bg="black", width=600,height=500, relief=GROOVE , ) 
f.place(x=10,y=80)

#Second Frame
frame2=Frame (root, bd=3,width=500,height=500, bg="white", relief=GROOVE) 
frame2.place(x=610,y=80)

#text1=Text (frame2, font="Robote 20",bg="white", fg="black", relief=GROOVE, wrap=WORD ) 
#text1.place(x=0,y=0, width=500,height=250)


#scrollbar1=Scrollbar(frame2)
#crollbar1.place(x=480, y=0,height=250)

#scrollbar1.configure(command=text1.yview) 
#text1.configure(yscrollcommand=scrollbar1.set)

Label (frame2, text= "Heloo world " ,  bg="Yellow" ,  width=500 , height= 250 ).place(x=0,y=0 ) #font= "arial 35" ,

#third Frame
frame3=Frame (root, bd=3, bg="#2f4155",width=700, height=100, relief=GROOVE) 
frame3.place(x=10,y=600)

Button (frame3, text="Open Image", width=10,height=2, font="arial 14 bold", command=showimage).place (x=20,y=30) 
Button (frame3, text="Save Image", width=10,height=2, font="arial 14 bold", command=save).place (x=160,y=30) 
Button (frame3, text="Hide", width=10,height=2, font="arial 14 bold", command=Hide).place (x=300,y=30)
Button (frame3, text="Extract", width=10,height=2, font="arial 14 bold", command=Extract).place (x=450,y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155",fg="yellow").place (x=20,y=5)

#fourth Frame
frame4=Frame (root, bd=3, bg="#2f4155",width=500, height=100, relief=GROOVE) 
frame4.place(x=710,y=600)



Button (frame4, text="Encrypt Message", width=15,height=2, font="arial 14 bold", command=Encrypt).place (x=20, y=30) 
Button (frame4, text="Decrypt Message", width=15,height=2, font="arial 14 bold", command=Decrypt).place (x=280,y=30) 

#5th frame 
frame5=Frame (root, bd=3, bg="#2f4155",width=500, height=500, relief=GROOVE) 
frame5.place(x=1210,y=80)
Label (frame5, text="Enter your message size : ", bg="#2f4155", fg="yellow").place (x=20,y=5)
text5_1=Text (frame5, font="Robote 10",bg="white", fg="black", relief=GROOVE, wrap=WORD ) 
text5_1.place(x=161,y=5, width=200,height=20)
Label (frame5, text="Enter your private key : ", bg="#2f4155", fg="yellow").place (x=20,y=25)
text5_2=Text (frame5, font="Robote 10",bg="white", fg="black", relief=GROOVE, wrap=WORD ) 
text5_2.place(x=161,y=25, width=200,height=20)



root.mainloop()