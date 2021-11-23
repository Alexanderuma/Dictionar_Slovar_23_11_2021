from Module import *
rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)

sonad=""
for sona in rus_list:
    sonad=sonad+" "+sona
heli(sona,'ru') # rus

sonad=""
for sona in est_list:
    sonad=sonad+" "+sona
heli(sona,'fi') # est

while True:
    menu=input("Tõlgida-T: ,\nUus sõna-U: \n,Viga-V: ,\nKontroll-K: ;\nLõpp-L: ")
    if menu.upper()=="T":
        pass
    elif menu.upper()=="U":
        rus_list=uus_sona("rus.txt", input("Новое слово: "))
        est_list=uus_sona("est.txt", input("Uus sõna: "))
        pass
    elif menu.upper()=="V":
        v=input("Keel")
        if v=="rus":
             rus_list=correction(input('Vvedi slovo:'),rus_list)
             print(rus_list)
             failisse(rus_list,"rus.txt")
        else:
             est_list=correction(input('Sisesta sõna:'),est_list)
             print(est_list)
             failisse(est_list,"est.txt")
    elif menu.upper()=="K":
        pass
    else:
        break
   