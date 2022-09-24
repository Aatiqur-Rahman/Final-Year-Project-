import numpy as np
from Stegano import int_to_bin 
from Stegano import bin_to_int 
import cv2


int_value_of_msg = list()
bin_value_of_msg = list()


def msg_conversion (msg):
    print ("msg conversion is called ")
    for i in msg:
        #int_value_of_msg.append(ord(i)) # converting the ascii value and insert it into 1D list 
        int_value_of_msg.append(i) # not eequired any integer conversion
    for i in int_value_of_msg:
        temp = int_to_bin.method(i) # converting the ascii value of character into binary and storing it into temporary variable 
        bin_value_of_msg.append(temp) # insert the list of binary value into list 
    return bin_value_of_msg
    '''print("________________________ insert the all bit into pixel _________________________")
    print(len (bin_value_of_msg))
    print(type(bin_value_of_msg))
    print(bin_value_of_msg)'''

def main (image , shape , length ) : 
    print("_________________________Main function ____________________________________")
    #path1 = "H:\Shaap\Image processing\stinkbug.png" # image path
    global img 
    global img_shape
    global tlength
    tlength = length*8
    img_shape = shape 
    img = image 
    #img = cv2.imread(path1,1) # Reding image in RGB mode 
    #global img_shape 
    #img_shape = img.shape
    #print (img_shape)
    #print (img)
    #print("Shape of image :: __________________" , img_shape)
    #print(img[0,0:313:,])

def value(l,m):
    temp=l*img_shape[1]
    m=m+temp
    i=int(m/8)
    if (m==img_shape[1]):
        None
    else :
        i=int(m/8)
    j=m%8
    value_=bin_value_of_msg[i][j]
    return value_


def blue_pixel(l,m,n):
    red_pxl_of_img = img[l,m,n]
    bin_pxl=int_to_bin.method(red_pxl_of_img) # convert the integer into binary so that we can change last bit of binary value according to data 
    bin_pxl[7]=value (l,m) # inserting data in last bit of binary value #value
    int_pxl=bin_to_int.method(bin_pxl) # converting the binary value in to corresponding integer 
    print("blue pixed insertion " , int_pxl)
    img[l,m,n]=int_pxl


def green_pixel(l,m,n):
    green_pxl_of_img = img[l,m,n]
    print("green pixel ",green_pxl_of_img)
    bin_pxl=int_to_bin.method(green_pxl_of_img) # convert the integer into binary so that we can change last bit of binary value according to data 
    bin_pxl[7]=value(l,m) # inserting data in last bit of binary value 
    int_pxl=bin_to_int.method(bin_pxl) # converting the binary value in to corresponding integer 
    print(int_pxl)
    img[l,m,n]=int_pxl

def red_pxl():
    print("________________________________________________ red pixel of img ____________________________________________________________________")
    #length = length(msg)*8
    #tlength = tlength * 8 
    print(tlength)
    l_range = int(tlength/img_shape[1])+1
    
    m_range = img_shape[1]
    print(l_range)
    print (m_range)
    for l in range (0,l_range):
        if(l==l_range-1):
            m_range=tlength%img_shape[1]
        for m in range(0,m_range): #img_shape[1]
            for n in range(0,1): # picking red pixel of image 
                red_pxl_of_img = img[l,m,n]
                bin_of_red_pxl=int_to_bin.method(red_pxl_of_img)
                if (bin_of_red_pxl[7]==0):
                    green_pixel(l,m,n+1)
                elif (bin_of_red_pxl[7]==1):
                    blue_pixel(l,m,n+2)
       
        if(l_range==img_shape[0]):
            break




#print("________________________ stego Image ______________________________________________________________")
#print (img)
#print(bin_value_of_msg)
#print(len(bin_value_of_msg))
#cv2.imshow("Stego Image",img)
#cv2.waitKey(0)
#cv2.imwrite("stego_image1.png",img)

#cv2.destroyAllWindows()
