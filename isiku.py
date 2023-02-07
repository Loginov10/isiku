from OmaModul import *
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
            spaev=Sunnipaev(isik_list)
            if Sunnipaev=="Viga":
                arvud.apppend(isik)
            else:
                #
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

               h=Sunnikoht(hhh)

               sugu=Sugu(isik_list)
               print(f"See in {sugu}, sünnipäev {spaev}. ta on sündinud {h}")
               isikukoodid.append(isik)
               break
print(isikukoodid)
isikukoodid=naised_mehed(isikukoodid) #sort alguses naised ja pärast mehed
print(isikukoodid)
arvud=list(map(int,arvud))  #map - преобразует в новый формат
arvud.sort()
print(arvud)



