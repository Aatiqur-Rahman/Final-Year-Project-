from cgitb import text
from distutils.cmd import Command
from fileinput import filename
from tkinter import*
from tkinter import filedialog
from turtle import bgcolor, right
from PIL import Image, ImageTk 
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from RSA import gen_prime
from Stegano import Insert_using_cv2
from Stegano import decryption
import cv2
import time

root=Tk()
root.title("Steganography Hide a Secret Text Message in an Image")
root.geometry("1080x820+100+100") 

encrypted_value = list ()
binary_value=list()
binary_value_extract = list()
text_ascii = list()
org_text = list()

def Showimage():
    
    f_types = [('Jpg Files', '*.jpg'),('PNG files' , '*.png')]
    global filename 
    filename = filedialog.askopenfilename(filetypes=f_types)
    print ("after open "+filename )
    global img
    img = Image.open(filename)
    
    #img.resize ((100,100) , Image.ANTIALIAS)+
    img = ImageTk.PhotoImage(img.resize ((290,290) , Image.ANTIALIAS))
    
    label = Label(f, image = img )
    label.pack()

    IM =  cv2.imread(filename,1)
    size = IM.shape
    temp = int(size[1]/8)
    res = size[0] * temp
    print (res) 
    
    note["text"] = "Image inserted.You can write ",  res , "letter ... " 

    #b2 =tk.Button(root,image=img) # using Button 
    #b2.grid(row=3,column=1)

def Encrypt(): 
    
    msg = text1.get(1.0, 'end-1c') # take input 
    gen_prime.main()
    temp = gen_prime.msg_encryption(msg)
    global encrypted_value
    for x in temp : 
        encrypted_value.append(x)
    #for x in encrypted_value : 
        #note_text.append(chr (x))
    if ( msg == "" ) :
        note["text"] = "Please Enter Your Message . "
    else :
        note["text"] = "Your Message is Encrypted . "
     
def Decrypt():
    if (filename == "") :
        note["text"] = "Please insert image " 

    print (cipher_ascii)
    gen_prime.main()
    text_ascii = gen_prime.msg_decryption(cipher_ascii)
    org_text = decryption.int_to_ascii(text_ascii)
    
    note["text"] =  org_text

def save(): 

    f_types = [('PNG files' , '*.png')]
    file = filedialog.asksaveasfilename(filetypes=f_types)

    cv2.imwrite(file,im)
    sizeofmsg = len (binary_value)
    note["text"] = "stego image is created . Your message size is " , sizeofmsg 

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

    global binary_value

    binary_value =  Insert_using_cv2.msg_conversion(encrypted_value)
    sizeofmsg = len ( binary_value ) 
    print (sizeofmsg)
    Insert_using_cv2.main (im,img_shape,sizeofmsg)
    Insert_using_cv2.red_pxl ()

    note["text"] = "Cipher text embedded with image "

def Extract() : 
    try :
        sizeofmsg =  int ( text5_1.get(1.0, 'end-1c') ) 
        path = filename
        try :
            st_img = cv2.imread(path,1) 
            print (st_img)
            img_shape = st_img.shape
    
            decryption.main (st_img,img_shape,sizeofmsg*8)
            global binary_value_extract
            binary_value_extract = decryption.red_pxl()
            print (binary_value_extract)
            global cipher_ascii
            cipher_ascii = decryption.decrypt()
            note["text"] = "Cipher text extracted from image "
        except TypeError : 
            note["text"] = "Please insert a stego image "
    except ValueError:
        note["text"] = "Please insert your message size "
        
    
    

#icon
image_icon=PhotoImage(file="logo.jpg") 
root.iconphoto(False,image_icon)

#logo
logo1=PhotoImage(file="logo.png") 
Label(root,image=logo1 , bg="steel blue").place(x=50,y=16) 
logo2=PhotoImage(file="logo.png") 
Label(root,image=logo2 , bg="steel blue").place(x=940,y=16) 

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Cryptography and Image Steganography",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)

#first Frame
#f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
#f1.pack(side=LEFT)
f=Frame (root, bd=6, width=300,height=300, relief=SUNKEN ) 
f.place (x = 180 , y = 150) 
img=PhotoImage(file="logo.png") 
imglabel = Label(f,image=img).place(x=100,y=110) 


frame2 = Frame (root, bd=6, width=300,height=300, relief=SUNKEN)
frame2.place(x=500, y = 150) 
textlabel = Label (frame2, font=( 'aria' ,20, ), text= "Text Box"   , width=13, height= 1 , wraplength=500 ,  bd=4 , fg="steel blue")
textlabel.place (x =0,y=0)
text1=Text (frame2, font="Robote 20",bg="white", fg="black", relief=GROOVE, wrap=WORD ) 
text1.place(x=0,y=50, width=280,height=248)


scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=270, y=50,height=250,)

scrollbar1.configure(command=text1.yview) 
text1.configure(yscrollcommand=scrollbar1.set)


#third Frame
frame3=Frame (root, bd=3, bg="white",width=1080, height=120, relief=SUNKEN) 
frame3.pack (side=BOTTOM)

Button (frame3, bd = 12, padx=5 , pady= 5 , bg="powder blue" , text="Open Image", width=10,height=2, font="arial 14 bold", command=Showimage).place(x=10 , y=10) 
Button (frame3, bd = 12, padx=5 , pady= 5 , bg="powder blue" , text="Save Image", width=10,height=2, font="arial 14 bold", command=save).place (x=170,y=10) 
Button (frame3, bd = 12, padx=5 , pady= 5 , bg="powder blue" , text="Embed", width=10,height=2, font="arial 14 bold", command=Hide).place (x=330,y=10)
Button (frame3,  bd = 12, padx=5 , pady= 5 , bg="powder blue", text="Extract", width=10,height=2, font="arial 14 bold", command=Extract).place (x=490,y=10)
Button (frame3, bd = 12, padx=5 , pady= 5 , bg="powder blue", text="Encrypt Message", width=14,height=2, font="arial 14 bold", command=Encrypt).place (x=650, y=10) 
Button (frame3, bd = 12, padx=5 , pady= 5 , bg="powder blue", text="Decrypt Message", width=14,height=2, font="arial 14 bold", command=Decrypt).place (x=860,y=10)
#Label(frame3, text="Picture, Image, Photo File", bg="#2f4155",fg="yellow").place (x=20,y=5)




frame4 = Frame (root, bd=6,  width=600,height=110, relief=SUNKEN)
frame4.place(x=180, y = 460) 
 
note = Label (frame4, text= "Notification ...."   , width=53, height= 4 , font= "arial 15" , wraplength=500 , fg="steel blue") #font= "arial 35" 
note.place (x = 0 , y = 0 )
note.bind("<Button-1>", Encrypt)
note.bind("<Button-2>", Showimage)
note.bind("<Button-3>", Hide )
note.bind("<Button-4>", save)
note.bind("<Button-5>", Extract)
note.bind("<Button-5>", Decrypt)




#5th frame 
frame5=Frame (root, bd=5, width=600, height=100, relief= SUNKEN ) 
frame5.place(x=180,y=580)
Label (frame5, text="Enter your message size : " , width = 25 , height= 2 ,font=( 'aria' ,15, ) , fg="steel blue").place (x=30,y=5)
text5_1=Text (frame5, font="Robote 15",bg="white", fg="black", relief=SUNKEN, wrap=WORD, width=20,height=1 ) 
text5_1.place (x=300,y=20)
#Label (frame5, text="Enter your private key : ").place (x=20,y=25)
##text5_2=Text (frame5, font="Robote 10",bg="white", fg="black", relief=GROOVE, wrap=WORD ) 
#text5_2.place(x=161,y=25, width=200,height=20)



root.mainloop()