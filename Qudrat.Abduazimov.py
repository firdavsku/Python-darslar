# successful
# a = int(input("Metrni kiriting cm aylantirib beraman="))
# print(a*100, "cm" )

# successful 
# b = int(input("Tonnani kiriting kilogramga aylantiraman="))
# print(b*1000, "kg")

# successful
# c = int(input("Kilobaytni kiriting baytga aylantiraman="))
# print(c*1024, "bayt")

#successful
# A = int(input("A sonni kiriting="))
# B = int(input("B sonni kiriting="))
# if A>B:
#    print(A//B)
# else:
#    print("Xato")

# successful
# son = int(input("Istalgan sonni kiriting="))
# print("Raqamlari yig'indisi=", , "ga teng")

# successful
# son = (input("Ikki xonali son kiriting="))
# son//10 + son//10
# print(son[-1],son[-2],son[0])

# successful
# a = int(input("Uch xonali sonni kiriting="))
# print("Men birliklar va o'nliklar xonasidagi sonni aytaman")
# birliklar_raqami = (a%10)
# onliklar_raqami = (a//10)%10
# print("Birliklar xonasidagi son=",birliklar_raqami)
# print("O'nlilar xonasidagi son=",onliklar_raqami)

# successful
# a = int(input("Uch xonali sonni kiriting="))
# yuzlar_raqami =(a//100)%10
# print("Yuzlar xonasidagi raqam=",yuzlar_raqami)

# successful
#  a = (input("Uch xonali sonni kiriting="))
# print(a[0], "Yuzlar xonasi", a[-2], "O'nlar xonasi", a[-1], "Birlar xonasi")

# successful
# son = input("Uch xonali sonni kiriting=")
# a,b,c = son
# Narx = int(a)+int(b)+int(c)
# if len(son)==3:
#     print(f"{a} + {b} + {c} = {Narx}")
# else:
#     print("Xato")

# homework
# successful
# a = input("Uch xonali sonni kiriting teskari qilib beraman=")
# print(a[-1],a[-2],a[0])

# successful
# a = input("Uch xonali son kiriting o'nliklar xonasidagi sonni yuzliklar xonasiga o'tkazaman =")
# print(a[-2], a[0], a[-1])

# successful
# a = input("Uch xonali son kiriting o'nliklar xonasidagi sonni birliklar xonasiga o'tkazaman = ")
# print(a[0], a[-1], a[-2])

# successful
# a = int(input("To'rt xonali sonni kiriting="))
# birinchi_raqam = (a//100)
# ikkinch_raqam = (a//10)%10
# uchinchi_raqam = (a%10)
# tortinchi_raqam = (a/1)
# new_number = (birinchi_raqam*100+ikkinch_raqam*10+uchinchi_raqam*1+tortinchi_raqam)
# print("The new number is=", new_number)


# a = (input("To'rt xonali sonni kiriting="))
# if len(a) == 4:
#     print(f'{a[0]}000 + {a[1]}00 + {a[2]}0 + {a[3]}')
# else:
#     print(False)


# successful
# N = int(input("Siz so`a`tni kiriting sekundga aylantirib beraman="))
# print(N*3600, "sekund ishlagansiz")

# successful
# N = int(input("Ishlagan sekundingizni kiriting soatga aylantiramiz="))
# print(N//3600, "soat ishlagansiz")

#successful
# N = int(input("Sekund kiriting qancha soat va qancha sekund ishlaganingizni aniqlaymiz, qani kettik!"))
# print(N//3600, "soat", N/60, "minut")

# pastroqda javob berilgan
# def haftaning_kuni(k):
#     haftaning_kunlari = ["yakshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]
#     boshlanish_kuni = 1  # Yanvarning 1-dushi dushanba bo'lsa
#     natija_kuni = (boshlanish_kuni + k - 1) % 7
#     return haftaning_kunlari[natija_kuni]

# Namuna foydalanish
# k = int(input("1 va 365 oralig'ida bo'lgan biror sonni kiriting: "))
# kun =(k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")

# a = input("Raqam kiriting=")
# def haftaning_kuni(a):
#     haftaning_kunlari = ["yakshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]
#     boshlanish_kuni = 1  
#     natija_kuni = (boshlanish_kuni + a - 1) % 7
#     return haftaning_kunlari[natija_kuni]

# # error
# def haftaning_kuni(a):
# k = int(input("1 dan 365 gacha bo'lgan sonni kiriting="))haftaning_kuni = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
# boshlanish_kuni = 1
# natija_kuni = (boshlanish_kuni + a -1) % 7
# return haftaning_kuni[natija_kuni]
# k = int(input("1 va 365 oralig'ida bo'lgan biror sonni kiriting: "))
# kun = (k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")
# a = input("365 gacha bo'lgan sonni kiriting qaysi hafta kuniga to'g'ri kelishini aytaman=")
# def haftaning_kuni(a):
# k = int(input("1 dan 365 gacha bo'lgan sonni kiriting="))haftaning_kuni = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
# boshlanish_kuni = 1
# natija_kuni = (boshlanish_kuni + a -1) % 7
# return haftaning_kuni[natija_kuni]
# k = int(input("1 va 365 oralig'ida bo'lgan biror sonni kiriting: "))
# kun = (k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")

# # shart operatorlari
# # a = int(input("Biror bir son kiriting="))
# # if a == -1:
# #     print("Iltimos musbat son")

# float sonni 7 ga bulinganda uni qoldiqini chiqaradi


# def haftaning_kuni(k):
#     haftaning_kunlari = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
#     boshlanish_kuni = 1  # Yanvarning 1-dushi dushanba bo'lsa
#     natija_kuni = (boshlanish_kuni + k - 1) % 7
#     return haftaning_kunlari[natija_kuni]
# k = int(input("1 va 365 oralig'ida bo'lgan biror sonni kiriting: "))
# kun = haftaning_kuni(k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")


# 1-son payshanba kuniga togri keladi
# def haftaning_kuni(k):
#     haftaning_kuni = ["Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba", "Dushanba", "Seshanba"]
#     boshlanish_kuni = 1
#     natija_kuni = (boshlanish_kuni + k - 1) % 7
#     return haftaning_kuni[natija_kuni]
# k = int(input("1 va 365 oralig'ida bo'lgann biror sonni kiriting="))
# kun = haftaning_kuni(k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")

# 1-son dushanbaga to'g'ri keladi va seshanba kuni deb chiqishi kerak
# def haftaning_kuni (k):
#     haftaning_kuni = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
#     boshlanish_kuni = 1
#     natija_kuni = (boshlanish_kuni + k - 1) % 7
#     return haftaning_kuni[natija_kuni]
# k = int(input("1 va 365 oralig'idagi sonlarni kiriting="))
# if k>365:
#     print("Iltimos 365 gacha sonni kiriting!")
# kun = haftaning_kuni(k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")

# 1-yanvar Yakshanba ga to'g'ri keladi
# def haftaning_kuni (k):
#     haftaning_kuni = ["Shanba", "Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma"]
#     boshlanish_kuni = 1
#     natija_kuni = (boshlanish_kuni + k - 1) % 7
#     return haftaning_kuni[natija_kuni]
# k = int(input("1 va 365 gacha bo'lgan sonni kiriting="))
# kun = haftaning_kuni(k)
# print(f"{k} - soni {kun} kuniga to'g'ri keladi.")

# if 1 error
# a = int(input("Butun sonni kiriting="))
# if a == -1 -2 -3:
#     print("Musbat sonni kiriting!")
# elif a == +1+1:
#     print("Ajoyib!")
# else:
#     print("Xato!")

# for operatoridan 4-misol successful
# print("1 kg konfet narxi= 34500 so'm")
# for a in range(1,11):
#     print(a*34500, "so'm")

# qo'shimcha
# print("1 kg mol go'sht=72990 so'm")
# a = int(input("Nechchi kilogram mol go'sht olasiz?"))
# print(a*72990, "so'm narxda to'laysizmi yoki plastikmi?")
# a = input("1 yoki 2 ")
# print("Tushunarli")
# print("Xaridingiz uchun rahmat!")
# print("Sizni yana kutib qolamiz!")

# ko'rib chiqish zarur
# if a == rint("Assalomu alaykum Korzinkaga xush kelibsiz!")
# a = print("1 kg Turkiya apelsini=37990")
# b = print("1 kg Qizil olma narxi=65990")
# c = print("1 kg Qulupnay narxi=14990")
# d = print("1 kg Tarvuz narxi=15990")
# e = print("1 dona Apelsin narxi=45990")
# f= input("Qanaqa


# successful
# print("1 kg konfet narxi=77990so'm")
# a = int(input("Necha kilogram konfet konfet olasiz?"))
# print(a*77990, "so'm")

# successful
# print("Assalomu alaykum Korzinkaga xush kelibsiz!")
# print("1 kg konfet narxi=36990 so'm")
# a = float(input("Nechchi kilogram konfet olasiz?"))
# print(a*36990, "so'm")

# successful
# a = int(input("A kesmani kiriting="))
# b = int(input("B kesmani kiriting="))
# joylashtirish_marta = 0
# while a >= b:
#     a -= b
#     joylashtirish_marta += 1
# print("Joylashtirish mumkinligi:", joylashtirish_marta)

# successful
# a = int(input("Ikki xonali son kiriting="))
# birinchi_son = a//10
# ikkinchi_son = a%10
# yigindi = birinchi_son+ikkinchi_son
# print("Raqamlar yig'indisi=",yigindi)

# successful
# a = int(input("Ikki xonali son kiriting="))
# birinchi_son = a//10
# ikkinchi_son = a%10
# almashtirish = ikkinchi_son*10+birinchi_son
# print("Almashtirilgan son=",almashtirish)

# IELTS sertificate
# successful
# a = float(input("Enter your listening"))
# b = float(input("Enter your speaking"))
# c = float(input("Enter your writing"))
# d = float(input("Enter your reading"))
# print("Overschool=",(a+b+c+d)//4)
# if a<5.5:
#     print("Siz A2 sertifikatini qo'lga kiritdingiz!")
# if a>7.5:
#     print("Siz C2 sertifikatikini qo'lga kiritdingiz!")
# if a<7.5:
#     print("Siz C1 sertifikatini qo'lga kiritdingiz!")
# else:
#     print("Tabriklaymiz!")

# successful
# a = int(input("Uch xonali son kiriting="))
# birinchi_raqam = a//100
# ikkinchi_raqam = (a//10)%10
# uchinchi_raqam = a%10
# new_number = ikkinchi_raqam*100+uchinchi_raqam*10+birinchi_raqam
# print("Yangi son=",new_number)

# integer14
# successful
# a = int(input("Uch xonali sonni kiriting="))
# birinchi_raqam = a//100
# ikkinchi_raqam = (a//10)%10
# uchinchi_raqam = a%10
# new_number = uchinchi_raqam*100+birinchi_raqam*10+ikkinchi_raqam
# print("New number=",new_number)

# successful
# integer15
# a = int(input("Uch xonali son kiriting, men o'nlikdagi sonni yuzlikka, yuzlikdagi raqamni esa o'nlikka o'tkazib beraman"))
# yuzlik = a//100
# onlik = (a//10)%10
# birlik = a%10
# new_number = onlik*100+yuzlik*10+birlik
# print("Xosil bolgan raqam",new_number)

# successful
# integer16
# a = int(input("Uch xonali son kiriting, o'nlikdagi sonni birlikka, birlikdagi sonni o'nlikka o'tkazaman"))
# yuzlik = a//100
# onlik = (a//10)%10
# birlik = a%10
# new_number = yuzlik*100+birlik*10+onlik
# print("Xosil bo'lgan raqam",new_number)

# successful
# while1
# a = int(input("A kesmani uzunligiini kiriting faqat B sondan katta bo'lsin="))
# b = int(input("B kesmani uzunligini kiriting="))
# print("B kesmani A kesmaga shuncha joylashtira olasiz=",a/b)

# 
# successful
# yil = int(input("Yilni kiriting asrga o'tkazib beraman = "))
# if 2099 >= yil >= 2000:
#     print("XXI asr")
# elif 1999 >= yil >= 1900:
#     print("XX asr")
# elif 1899 >= yil >=1800:
#     print("IXX asr")
# elif 1799 >= yil >=1700:
#     print("XVIII asr")
# elif 1699 >= yil >=1600:
#     print("XVII")
# elif 1599 >= yil >=1500:
#     print("XVI")
# elif 1499 >= yil >=1400:
#     print("XV asr")
# elif 1399 >= yil >= 1300:
#     print("XIV asr")
# elif 1299 >= yil >=1200:
#     print("XIII asr")
# elif 1199 >= yil >=1100:
#     print("XII asr")
# elif 1099 >= yil >=1000:
#     print("XI asr")
# elif 999 >= yil >=900:
#     print("X asr")
# elif 899 >= yil >=800:
#     print("IX asr")
# elif 799 >= yil >=700:
#     print("IIX asr")
# elif 699 >= yil >=600:
#     print("VII asr")
# elif 599 >= yil >=500:
#     print("VI asr")
# elif 499 >= yil >=400:
#     print("V asr")
# elif 399 >= yil >=300:
#     print("IV asr")
# elif 299 >= yil >=200:
#     print("III asr")
# elif 199 >= yil >=100:
#     print("II asr")
# elif 99 >= yil >= 00:
#     print("I asr")
# else:
#     print("Iltimos 1 dan 2023 gacha bo;lgan sonni kiriting!")

# masala 1
# successful
# a = float(input("Son kiriting = "))
# if a>0:
#     print(a+1, "musbat")
# else:
#     print("Manfiy")

# successful
# masala 2
# a = int(input("Son kiriting="))
# if a>0:
#     print(a+1, "musbat")
# elif a<0:
#     print(a-2, "manfiy")

# masala 3
# successful
# a = int(input("Son kiriting="))
# if a==0:
#     print(a+10)
# elif a<0:
#     print(a-2, "manfiy")
# elif a>0:
#     print(a+1, "musbat")
# else:
#     print("Xato")

# error
# masala 4
# tushunmadim 

# successful
# masala 6
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a>b:
#     print("Muvaffaqiyatli!, A son B sondan katta")
# elif a<b:
#     print("Muvaffaqiyatli!, B son A sondan katta")

# successful
# masala 8
# a = int(input("A sonni kiriting="))
# b = int(input("B sonnni kiriting="))
# if a>b:
#     print("A son B sondan katta,", "kichkina son esa=",b)
# elif a<b:
#     print("B son A sondan katta,", "kichkina son esa=",a)

# successful
# masala 9
# a = int(input("A sonni kiriting="))
# b = int(input("B sonni kiriting="))
# if a>b:
#     print("B son A sondan katta = ", b+a)
# elif a<b:
#     print("A son B sondan katta = ", a+b)

# error
# tushunmadim
# masala 10

# error
# tushunmadim
# masala 11



# def kichigini_aniqlovchi(son1, son2, son3):
#     kichik = son1 
#     if son2 < kichik: 
#         kichik = son2
#     if son3 < kichik: 
#         kichik = son3
#     return kichik

# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# son3 = int(input("Uchinchi sonni kiriting: "))

# kichik_son = kichigini_aniqlovchi(son1, son2, son3)

# print("Kichik son: ", kichik_son)

# narh= 15000 
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy: 
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat: 
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:   
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: 
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")

# xizmat_narxi = 10000
# Pepsi_1_litr = True 
# Non_2ta = True
# Osh = True
# Salat = True
# if Pepsi_1_litr:
#     print("10-stol 1.5 litrlik Pepsi oldi")
#     xizmat_narxi = xizmat_narxi + 5000
# if Non_2ta:
#     print("10-stol 2 ta non oldi")
#     xizmat_narxi = xizmat_narxi - 2000
# if Osh:
#     print("10-stol 1 porsiya osh oldi")
#     xizmat_narxi = xizmat_narxi + 10000
# if Salat:
#     print("10-stol salat oldi")
#     xizmat_narxi = xizmat_narxi - 5000

# print(f"Sizdan {xizmat_narxi} so'm")