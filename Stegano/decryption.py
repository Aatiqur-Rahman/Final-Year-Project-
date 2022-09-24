import imghdr
from operator import length_hint
import numpy as np
import cv2
from Stegano import int_to_bin
from Stegano import bin_to_int

bin_data_list = list() # for store binary bit 
int_data_list = list() # for store conrrespinding integer of binary 
cipher = list()

def int_to_ascii(int_list) :
    for i in int_list:
        cipher.append(chr(i))
    return cipher


def green_pixel(l,m,n): # function call of green pixel value 
    green_pxl_of_img = img[l,m,n]
    bin_pxl=int_to_bin.method(green_pxl_of_img) # convert the integer into binary so that we can store last bit of binary value according to data 
    print ("green pixel : "  ,  bin_pxl)
    data_bit=bin_pxl[7] # decrypt the last bit of data and store it into temporary variable data _bit 

    print ("green pixel " , data_bit)
    bin_data_list.append(data_bit) # insert the last bit into bin_data_list 
    #int_pxl=bin_to_int.method(bin_pxl) # converting the binary value in to corresponding integer 
    #print(int_pxl)
    #img[l,m,n]=int_pxl

def blue_pixel(l,m,n):

    red_pxl_of_img = img[l,m,n]
    bin_pxl = int_to_bin.method(red_pxl_of_img)
    data_bit=bin_pxl[7]
    bin_data_list.append(data_bit)

def main (Image , Image_shape , sizeofmsg) : 
    global length
    global img
    global img_shape

    length = sizeofmsg
    img= Image
    img_shape = Image_shape  
    #path1 = "H:\Shaap\Image processing\stego_image.png" # image path
    #img = cv2.imread(path1,1) # Reding image in RGB mode 
    #print("____________________ original image _________________________")
    #print (img)
    #print("_____________________Red Pixel _________________________________")
    #print()
    #img_shape = img.shape
    #length = len(Insert_using_cv2.bin_value_of_msg)*8
    #print(length)

def red_pxl(): 
    l_range= int(length/img_shape[1])+1
    m_range = img_shape[1]  
    for l in range (0,l_range):
        if (l==l_range-1):
            m_range=length%img_shape[1]
        for m in range(0,m_range): #img_shape[1]
            for n in range(0,1): # picking red pixel of image 
                red_pxl_of_img = img[l,m,n]
                bin_of_red_pxl=int_to_bin.method(red_pxl_of_img)
                #print(bin_of_red_pxl)
                if (bin_of_red_pxl[7]==0):
                    green_pixel(l,m,n+1)
                elif (bin_of_red_pxl[7]==1):
                    blue_pixel(l,m,n+2)
    
    return bin_data_list      
        
#print (bin_data_list)
#print(len(bin_data_list))


def decrypt () : 

    length = len(bin_data_list) # determine the length of the list so that easily convert to numpy 2D array 
    bin_data_array=np.array(bin_data_list).reshape(int(length/8),8) # converting the list into numpy 2D  array
    for i in bin_data_array:
        int_of_data = bin_to_int.method(i)
        int_data_list.append(int_of_data)
    print (int_data_list)
    return int_data_list



