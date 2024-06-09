import cv2
import os
import string

img=cv2.imread("abc.jpg")
msg = input("enter secret message")
password=input("enter a password")


d={}
c={}


for i in range(255):
     d[chr(i)]=i
     c[i]=chr(i)



n=0;
m=0;
z=0;

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3


cv2.imwrite("encriptedImage.jpg",img)
os.startfile("encriptedImage.jpg")
message=""
n=0
m=0
z=0

pas=input("enter password for decryption")
if(password==pas):
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("decripted message =",message)
else:
    print("you are not authenticated")
        
