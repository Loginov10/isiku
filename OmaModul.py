def Sugu(isik_list:list):->str:
    """Esimise tahe j�rgi m��reme sugu
    :param list isik_list:J�rjend isikukoodi numbridest
    :rtype: str
    """
    if int(isik_list[0])%2==0:
         sugu="naine"
    else:
         sugu="mees"
    return sugu

def Sunnikoht(a:int)->str:
    """Esimise tahe j�rgi m��reme Sunnikoht
    :param list isik_list:
    :rtype: str
    """
    hhh=int(isik_list[8]+isik_list[9]+isik_list[10])
               if 1<=a<=10:
                    h="kuresaare haigla"
               elif 11<=a<=19:
                    h="Tartu �likooli Naistekliinik, Tartumaa, Tartu"
               elif 21<=a<=220:
                    h=" Ida-Tallinna Keskhaigla, Pelgulinna s�nnitusmaja, Hiiumaa, Keila, "
               elif 221<=a<=270:
                    h="Ida-Viru Keskhaigla (Kohtla-J�rve, endine J�hvi"
               elif 271<=a<=370:
                    h=" Maarjam�isa Kliinikum (Tartu), J�geva Haigla"
               elif 371<=a<=420:
                    h="Narva Haigla"
               elif 421<=a<=470:
                    h="P�rnu Haigla"
               elif 471<=a<=490:
                    h="Pelgulinna S�nnitusmaja (Tallinn), Haapsalu haigla"
               elif 491<=a<=520:
                    h="J�rvamaa Haigla (Paide)"
               elif 521<=a<=570:
                    h="Rakvere, Tapa haigla"
               elif 571<=a<=600:
                    h="Valga Haigla "
               elif 601<=a<=650:
                    h="Viljandi Haigla"
               elif 651<=a<=700:
                    h="L�una-Eesti Haigla (V�ru), P�lva Haigla "
               else:
                   h="____"
               return h

def Sunnipaev(ik_list:list):->str:
    """
    :param:
    :rtype: str
    """
            s1=int(ik_list[0])
            i2=isik_list[2]+isik_list[1]        #aasta     #????????? ????????
            i3=int(isik_list[3]+isik_list[4])   #kuu
            i4=int(isik_list[5]+isik_list[6])   #p�ev
            if (int(i3)<1 or int(i3)>13) and (int(i4)<1 or int(i4)>31):
                spaev="Viga"
                #arvud.append(isik)
            else:
               if i==1 or i==2:
                    yy="18"
               elif i==3 or i==4:
                    yy="19"
               elif i==5 or i==6:
                   yy="20"
               spaev=str(i4)+"."+str(i3)+"."+yy+str(i2)
               print(f"s�nnip�ev on",spaev)
               print(f"Viimane number:{isik_list[-1]}")
               if i in [2,4,6]:
                   print("naine")
               if i in [1,3,5]:
                   print("mees")
            return spaev

def naised_mehed(isikukoodid:list):
    """
    :rtype: list
    """

    naised=[]
    mehed=[]
    for kood in ikoodid:
        isik_list=list(kood)
        sugu=Sugu(isik_list)
        if sugu=="naine"
            naised.append(kood)
        else:
            mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(mehed)