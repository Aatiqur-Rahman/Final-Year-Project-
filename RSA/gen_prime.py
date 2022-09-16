from RSA import EEA_gcd



def key_generation ():
    prime_1 = 11
    prime_2 = 13
    multip_of_prime = 11*13 # multip is used as the modulus for both key
    totient = (prime_1-1)*(prime_2-1)
    for i in range(2,totient):
        gcd_value,x,y = EEA_gcd.GCD(i,totient,1,0) # a.x + b.y = 1 
        if (gcd_value==1):
            if (x<0): # if coefficient of a is negative , converting it into positive 
                x=-x
            if (y<0): 
                y=-y
            if((i*x)%(totient*y)==1):
                d=x
                e=i
                k=y
                break
    return (e,multip_of_prime,d)
def main ():
    print("___________________ Main ________________________________________")
    global e , n, d
    e,n,d=key_generation()
    print(e,d,n)

ascii_value_of_msg_for_encryption=list()
ascii_value_of_msg_for_decryption=list()
encrypted_value_of_msg = list()

def msg_encryption (msg):
    print (msg) 
    for i in msg: 
        ascii_value_of_msg_for_encryption.append(ord(i))
    print(ascii_value_of_msg_for_encryption)
    for i in ascii_value_of_msg_for_encryption:
        temp = i**e % n
        encrypted_value_of_msg.append(temp)
    print(encrypted_value_of_msg)
    return encrypted_value_of_msg
def msg_decryption (value):
    for i in value:
        temp = i**d % n
        ascii_value_of_msg_for_decryption.append(temp)
    return ascii_value_of_msg_for_decryption



