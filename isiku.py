
arvud=[]
isikukoodid=[]
while True:
    isik=input("Anna isikukood: ")  #str
    if len(isik)!=11:            #!-не равно 11
        print("Liiga oalju või vähe sümboleid. Sisesta veel kord")
        arvud.append(isik)
    else:
        print("Isikukoodi kontroll")
        isik_list=list(isik)      #обращение к 1 символу
        i=int(isik_list[0])       #sugu
        if i not in [1,2,3,4,5,6]:
           print("Esimene sümbol ei ole õige") 
           arvud.append(isik)
        else:
            print("Esimene sümbol on õige")
            i2=isik_list[2]+isik_list[1]        #aasta     #склеиваем значения
            i3=int(isik_list[3]+isik_list[4])   #kuu
            i4=int(isik_list[5]+isik_list[6])   #päev
            if (int(i3)<1 or int(i3)>13) and (int(i4)<1 or int(i4)>31):
                print("Vale sümbolid")
                arvud.append(isik)
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
               if i in [2,4,6]:
                   print("naine")
               if i in [1,3,5]:
                   print("mees")
               a=[1,2,3,4,5,6,7,8,9,1]
               a2=[3,4,5,6,7,8,9,1,2,3]
       
               b1=int(isik[0])*1
               b2=int(isik[1])*2
               b3=int(isik[2])*3
               b4=int(isik[3])*4
               b5=int(isik[4])*5
               b6=int(isik[5])*6
               b7=int(isik[6])*7
               b8=int(isik[7])*8
               b9=int(isik[8])*9
               b10=int(isik[9])*1

               b11=b1+b2+b4+b3+b5+b6+b7+b8+b9+b10
               b=b11//11
               p=b*11
               p1=b11-p
               print(p1)
       
               c1=int(isik[0])*3
               c2=int(isik[1])*4
               c3=int(isik[2])*5
               c4=int(isik[3])*6
               c5=int(isik[4])*7
               c6=int(isik[5])*8
               c7=int(isik[6])*9
               c8=int(isik[7])*1
               c9=int(isik[8])*2
               c10=int(isik[9])*3

               c11=c1+c2+c4+c3+c5+c6+c7+c8+c9+c10
               c=c11//11
               p2=c*11
               p3=c11-p2
               print(p3)

               hhh=int(isik_list[8]+isik_list[9]+isik_list[10])
               if 1<=hhh<=10:
                    h="kuresaare haigla"
               elif 11<=hhh<=19:
                    h="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
               elif 21<=hhh<=220:
                    h=" Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, "
               elif 221<=hhh<=270:
                    h="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi"
               elif 271<=hhh<=370:
                    h=" Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
               elif 371<=hhh<=420:
                    h="Narva Haigla"
               elif 421<=hhh<=470:
                    h="Pärnu Haigla"
               elif 471<=hhh<=490:
                    h="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
               elif 491<=hhh<=520:
                    h="Järvamaa Haigla (Paide)"
               elif 521<=hhh<=570:
                    h="Rakvere, Tapa haigla"
               elif 571<=hhh<=600:
                    h="Valga Haigla "
               elif 601<=hhh<=650:
                    h="Viljandi Haigla"
               elif 651<=hhh<=700:
                    h="Lõuna-Eesti Haigla (Võru), Põlva Haigla "
               if int(isik_list[0])%2==0:
                   sugu="naine"
               else:
                   sugu="mees"
               print(f"See in {sugu}, sünnipäev {spaev}. ta on sündinud {h}")
               isikukoodid.append(isik)
               break
print(isikukoodid)
arvud=list(map(int,arvud))  #map - преобразует в новый формат
arvud.sort()
print(arvud)


