
while True:
    isik=input("Anna isikukood: ")  #str
    if len(isik)!=11:            #!-не равно 11
        print("Liiga oalju või vähe sümboleid. Sisesta veel kord")
    else:
        print("Isikukoodi kontroll")
        isik_list=list(isik)      #обращение к 1 символу
        i=int(isik_list[0])       #sugu
    if i not in [1,2,3,4,5,6]:
       print("Esimene sümbol ei ole õige")          
    else:
        print("Esimene sümbol on õige")
        i2=isik_list[2]+isik_list[1]   #aasta         #склеиваем значения
        i3=int(isik_list[3]+isik_list[4])   #kuu
        i4=int(isik_list[5]+isik_list[6])   #päev
    if (int(i3)<1 or int(i3)>13) and (int(i4)<1 or int(i4)>31):
        print("Vale sümbolid")
    else:
       if i==1 or i==2:
            yy="18"
       elif i==3 or i==4:
            yy="19"
       elif i==5 or i==6:
           yy="20"
       spaev=str(i4)+"."+str(i3)+"."+yy+str(i2)
       print(f"sünnipäev on",spaev)
       print(f"Viimane number:{isik_list[-1]}")
       a=["1","2","3","4","5","6","7","8","9","1"]
       a2=["3","4","5","6","7","8","9","1","2","3"]
