#!/usr/bin/env python
# coding: utf-8

# In[1]:


#silindirin hacmini hesaplayınız

r=int(input("yarıçapı giriniz:"))
h=int(input("yüksekliği giriniz:"))
pi=3.14
hacim=pi*(r**2)*h
print(hacim)


# In[2]:


#girilen sayının tek mi çift mi olduğunu yazdırınız

sayi=int(input("bir sayı giriniz:"))
if(int(sayi)%2==0):
    print("girilen sayi çift")
else:
    print("girilen sayi tek")


# In[5]:


#girlien sayı tek mi çift mi yoksa sıfır mı?
sayi=input("bir sayi giriniz:")
if (int(sayi)>0):
    print("girilen sayı pozitif")
elif (int(sayi)<0):
    print ("girilen sayı negatif")
else:
    print("sıfır")

