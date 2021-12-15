cinema = {}

def alusta():
    with open("elokuvalista.txt", "w") as t:
        t.write("")
    with open("varaukset.txt", "w") as t:
        t.write("")

def varaa(elokuva: dict, nimi, sali, aika):
    for k,v in elokuva.items():
        if nimi in k and sali in v[0] and aika in v[1]:
            if int(v[2]) < 0:
                return("Näytössä ei ole paikkoja jäljellä")
            elokuva[k] = v[0],v[1],int(v[2])-1
            with open("varaukset.txt", "w") as t:               
                    t.write(f"Varaus: {k} {v}")
            return print("Nauti elokuvasta.")
    return print("Varaus ei onnistunut, tarkista kirjoititko nimet väärin")

def listaa_varaukset():
    lista = []
    with open("varaukset.txt") as t:
        for i in t:
            lista.append(i)
    return lista    

def lisaa_elokuva(cinema, elokuva, sali, aika):
    if sali == "nautiskelu":
        cinema[elokuva] = sali, aika, "60"
    if sali == "rex":
        cinema[elokuva] = sali, aika, "150"
    if sali == "giga":
        cinema[elokuva] = sali, aika, "200"

    with open("elokuvalista.txt") as t:
        lines = t.readlines()
    with open("elokuvalista.txt", "w") as t:
            for line in lines:
                t.write(line)            
            t.write(f"Elokuva: {elokuva}, sali: {sali}, aika: {aika}\n")
    return f"Lisättiin näytös: {elokuva, sali, aika}"

def poista_elokuva(cinema, elokuva, sali, aika):
    for k,v in cinema.items():
        if elokuva == k and sali == v[0] and aika == v[1]:
            cinema.pop(k)
            break
    with open("elokuvalista.txt") as t:
        lines = t.readlines()
    with open("elokuvalista.txt", "w") as tie: 
        for line in lines:
            if elokuva not in line and sali not in line and aika not in line:
                tie.write(line)
            else:
                return f"Poistettiin {line}"
      
def naytot(): 
    lista = [] 
    with open("elokuvalista.txt") as t:
        for i in t:
            u = i.strip()
            lista.append((u))
    return lista
   
alusta()
while True:
    kauttaja = int(input("Valitse käyttäjä \n 1. asiakas \n 2. ylläpitäjä \n 3. poistu: "))
    if kauttaja == 1:
        while True:
            print(naytot())
            elokuva = input("Minkä elokuvan haluaisit nähdä: ")
            sali = input("Minkä salin haulaisit valita: ")
            aika = input("Mihin aikaan: ") 
            if varaa(cinema, elokuva, sali, aika) ==  "Nauti elokuvasta.":
                break
            if elokuva == "":
                break


    if kauttaja == 2:
        while True:
            komento = int(input("Valitse komento \n 1. selaile varauksia \n 2. lisää näytös \n 3. poista näytös \n 4. Poistu: "))
            if komento == 1:
                print(listaa_varaukset())
                
            if komento == 2:
                elokuva = input("Minkä elokuvan haluaisit lisätä: ")
                sali = input("Minkä salin haulaisit valita: rex/nautiskelu/giga")
                aika = input("Mihin aikaan: 0:00-24:00")
                print(lisaa_elokuva(cinema, elokuva, sali, aika))

            if komento == 3:
                print(naytot())
                elokuva = input("Minkä elokuvan haluaisit poistaa: ")
                sali = input("Mistä salista: ")
                aika = input("Mihin aikaan pyörivä: ")
                print(poista_elokuva(cinema, elokuva, sali, aika))

            if komento == 4:
                break
        

    if kauttaja > 3:
        print ("Valitse 1 tai 2")
        
    if kauttaja == 3:
        break

