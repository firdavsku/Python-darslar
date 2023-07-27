# pythonda for operatori
# for operatori bu bir nechta obyektlarga bir xil buyruq beradigan operatorlarga aytiladi
# masalan:
# mchs dan keladigan favqulodda xabar(hammaga xabar bir xil yuborilishi)
# for operatorining belgilanishi for kalit suzi bn ishlatiladi
# forni turli raqamlar bn matnlar va ozgaruvchilar bn ishlatiladi


# ismlar - bu o'zgaruvchi
# Ichidagi qiymatlar list ro'yxat ko'rinishda
# for i in ismlar - ismlar o'zgaruvchisini ichidagi hamma qiymatni olib, i degan o'zgaruvchiga aylantiradi


# mehmonlar = ['Aizbek aka','Abror aka','Rustam aka', 'Farrux aka','Olim aka']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 22 Iyun kuni nahorga oshga taklif qilamiz!")
#     print("Hurmat bilan, Elmurodovlar oilasi")


# ismlar = ['Azizbek', 'Olim', 'Ilhom']
# for i in ismlar:
#     print("Salom", i)


# range buyrug'i oraliq degan ma;noni anglatadi
# uning vazifasi berilgan sonnni oraliq qiymatlarini chiqaradi masalan


# for i in range(1,100):
#     print(i)

# for i in range (1,100):
#     print(i**3)


#successful
# mevalar = ['olma', 'anor', 'shaftoli', 'anjir']
# for i in mevalar:
#     print("Yozda pishadigan meva bu", i)


# successful
# for i in range(1,10):
#     print(i**2)


# successful
# for i in range(1,14):
#     print(1-i)

# successful
# ismlar = ['Samandar', 'Suxrob', 'Doston', 'Karim', 'Laziz']
# for dust in ismlar:
#     print(f"Salom do'stim {dust}")


# successful
# ismlar = ['Samandar Achilov', 'Suxrob Nematov', 'Karim Umidov', 'Laziz Baxtiyarov']
# for dust in ismlar:
#     print(f"Hurmatli {dust}, sizning oylik maoshingiz tashlab beriladi!")
# ismlar = ['Doston Umarov']
# for i in ismlar:
#     print(f"Hurmatli {i}, sizning maoshingizni yarmi ushlab qolindi")


# successful
# mehmonlar = ['Azizbek Gulomov', 'Azamat Gulomov', 'Farrux Xurramov', 'Shahzod Pulatov', 'Dilshod Pulatov', 'Sherzod Pulatov']
# for mehmon in mehmonlar:
#     print(f"Aziz va muhtaram {mehmon}  bugun sizni yoziladigan dasturxonimizga ya'ni Islomjonning sunnat to'yi munosabati bilan lutfan sizni va oilangizni taklif qilib qolamiz")
#     print("Hurmat bilan Murodullayevlar xonadoni, manzil:Qarshi shahar, Turon to'yxonasi")


# successful
# t = int(input("Tonnani kiriting, necha kg ekanini aniqlayman="))
# print(t*1000)


# sm = int(input("Sm qiymatni kiriting, mm ga aylantiraman="))
# print(sm*10)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


# ism = input("Ismingiz nima? ")
# print(f'Salom, {ism.title()}')



# for i in range(0,20,3):
#     print(i)

# 1-raqam rangening boshlanishi
# 2-raqam rangening tugashi
# 3-raqam rangening qadami ya'ni oraliq soni

# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")


# for i in range (1,5,10,15,20):
#     print(i-1)

for a in range(1,31):
    print(a)