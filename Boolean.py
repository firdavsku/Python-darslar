# Masala 1
# successful
# a = int(input("Istalgan sonni kiriting="))
# if a>0:
#     print(True)
# if a<-0:
#     print(False)

# Masala 2
# successful
# a = int(input("Sonni kiriting="))
# if a%2==0:
#     print("Juft son")
# else:
#     print("Musbat son")

# Masala 3
# successful
# a = int(input("Sonni kiriting="))
# if a%2==0:
#     print(a+1,"A juft son")
# else:
#     print("Toq son")

# Masala 4
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a>2:
#     print("A soni ikkidan katta bo'lsin!")
# elif b<=3:
#     print("B soni 3 dan kichkina bo'lsin!")
# else:
#     print("Xato")


# Masala 5
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a>=0:
#     print(True)
# elif b<-2:
#     print(False)

# Masala 6
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# c = int(input("C sonni kiriting="))
# print(a<=b<=c)

# Masala 7
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# c = int(input("C sonni kiriting="))
# print(a < b < c) or (c < b < a)

# Masala 8
# error
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a%2==0:
#     print("Toq son")
# elif b%2==0:
#     print("Toq son")

# Masala 9
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a%2==0:
#     print(True)
# elif b%2==0:
#     print(True)

# Masala 10
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a%2==0:
#     print(f"{a} juft son")
# elif b%2==0:
#     print(f"{b} juft son")
# elif a%3==0:
#     print(f"{a} toq son")
# elif b%3==0:
#     print(f"{b} toq son")
# else:
#     print(f"{a} {b} toq son")

# Masala 11
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a%2==0 and b%2==0:
#     print(f"{a} va {b} juft son")
# elif a%3==0 and b%3==0:
#     print(f"{a} va {b} toq son")
# else:
#     print(f"{a} {b} toq son")

# Masala 12
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# c = int(input("C sonni kiriting="))
# if a>0 or b>0 or c>0:
#     print(a,b,c,"soni musbat")

# Masala 13
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# c = int(input("C sonni kiriting="))
# if a>0:
#     print("A soni musbat")
# elif a<0:
#     print("A soni manfiy")
# if b>0:
#     print("B soni musbat")
# elif b<0:
#     print("B soni manfiy")
# if c>0:
#     print("C soni musbat")
# elif c<0:
#     print("C soni manfiy")

# Masala 14
# successful
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# c = int(input("C sonni kiriting="))
# if a>=0:
#     print("A soni musbat")
# elif b<0:
#     print("B musbat son")
# elif c<0:
#     print("C soni manfiy")

# Masala 15
# successful
# musbat = 0
# manfiy = 0
# a = int(input("Birinchi sonni kiriting="))
# b = int(input("Ikkinchi sonni kiriting="))
# c = int(input("Uchinchi sonni kiriting="))
# if a>0:
#     musbat +=1
# elif a<0:
#     manfiy +=1
# if b>0:
#    musbat +=1
# elif b<0:
#    manfiy +=1
# if c>0:
#     musbat +=1
# elif c<0:
#     manfiy +=1
# print("Positive numbers",musbat)
# print("Negative numbers",manfiy)


# Masala 16
# successful
# a = int(input("Enter two number type of postive="))
# if a%2==0:
#     print("Juft son")
# elif a==0:
#     print("Toq ham Juft emas")
# else:
#     print("Toq son")


#  Masala 17
# successful
# a = int(input("Uch xonali son kiriting="))
# if a%2==0:
#     print(a+1,"Toq son ")
# elif a!=2:
#     print(a,"Toq son")   
# else:
#     print("Error")     

# Masala 18
# successful
# a = int(input("Birinchi son kiriting="))
# b = int(input("Ikkinchi son kiriting="))
# c = int(input("Uchinchi son kiriting="))
# if a==b:
#     print("Birinchi va ikkinchisi teng")
# elif a==c:
#     print("Birinchi va uchinchi")
# elif b==c:
#     print("Ikkinchi va uchinchi")
# else:
#     print("Hech qaysi teng emas")

# Masala 19
# successful
# a = int(input("Birinchi sonni kiriting="))
# b = int(input("Ikkinchi sonni kiriting="))
# c = int(input("Uchinchi sonni kiriting="))
# if a or b or c %+ 2 == 0:
#     print(0-a)
#     print(0-b)
#     print(0-c)
# else :
#     print(False)

# Masala 20
# successful
# num = int(input("Sonni kiriting="))
# result = len(set(str(num))) == len(str(num))
# print(result)

# Masala 21
# successful
# a = (input("Uch xonali sonni kiriting="))
# if len(a)==3:
#     print("Raqamlar ketma-ketligi"(sorted(a)))
# else:
#     print("Faqat uch xonali sonni kiriting")

# Masala 22
# error
# a = (input("Uch xonali sonni kiriting="))
# if len(a)==3:
#     print("Raqamlar ketma-ketligi",(sorted(a), " bu o'suvchi"))
# elif len(a):
#     print("Raqamlar kamayishi",a[0],a[1],a[-1])
# else :
#     print("Faqat uch xonali sonni kiriting!")

# Masala 23
# successful
# a = (input("Uch xoanli sonni kiriting="))
# if len(a)==3:
#     print("Sonni chapdan o'nga qarab o'qilishi",a[::-1])
# else:
#     print("Faqat 3 xonali sonni kiriting!")

# Masala 24
# successful
# print("Uchta son kiriting va bu sonlarning diskriminantini topib beraman" )
# a = int(input("Enter first number="))
# b = int(input("Enter second number="))
# c = int(input("Enter third number="))
# print("Diskriminant=",b**2-4*a*c)

# Masala 25
# successful
# x = float(input("X o'qini kiriting="))
# y = float(input("Y o'qini kiriting="))
# if x>0:
#     print("X o'qida musbat chorakda")
# elif x<0:
#     print("X o'qida manfiy chorakda")
# if y>0:
#     print("Y o'qida musbat chorakda")
# elif y<0:
#     print("Y o'qida manfiy chorakda")

# Masala 26
# successful
# x = float(input("X o'qini kiriting="))
# y = float(input("Y o'qini kiriting="))
# if x>0 or y>0:
#     print("Sonlar birinchi chorakda yotadi")
# elif x<0 or y<0:
#     print("Sonlar to'rtinchi chorak manfiyida yotadi")

# Masala 27
# successful
# x = float(input("X o'qini kiriting="))
# y = float(input("Y o'qini kiriting="))
# if x>0 or y>0:
#     print("Sonlar ikkinchi chorakda yotadi")
# elif x<0 or y<0:
#     print("Sonlar uchinchi chorakda yotadi")

# Masala 28
# 
# x = float(input("X o'qini kiriting="))
# y = float(input("Y o'qini kiriting="))
# if x>0 or y>0:
#     print("Sonlar birinchi chorakda yotadi")
# elif x<0 or y<0:
#     print("Sonlar uchinchi chorakda yotadi")

# Masala 29
# 
