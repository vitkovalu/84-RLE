class Komprese:
    def __init__(self, array):
        self.__text = array
        self.__compressed = None
    
    @property
    def compressed(self):
          return self.__compressed

    def encode(self):
        self.__compressed = []
        for item in self.__text:
            pole = item.split(',')  # rozdělí vstupní data na pole s prvky podle čárky
            encoded_vstup = ""       # pro zápis zakodovaného stupu
            i = 0                    # proměnná, číslo (kolikátý) prvku
        
            while (i <= len(pole)-1):   #cyklus dokud nejsou na predposlením prvku
                count = 1               #proměnná součtu opakování
                hodnota = pole[i]       #ukládá se hodnota čísla
                if not hodnota.isdecimal():
                    print("Hodnoty nejsou zadány jako čísla")
                if int(hodnota) < 0 or int(hodnota) > 255:      #kontroluje zda jsou hodnoty ve správném intervalu
                    print("Zadány hodnoty mimo interval 0 až 255")
                    exit()
                j = i              
                while (j < len(pole)-1):
                    if (pole[j] == pole[j+1]): #pokud se jsou čísla rovnají
                        count = count+1        #připočítá se jedna do proměnné pocet
                        j = j+1                #posouvá se na další prvek
                    else:
                        break
                encoded_vstup=encoded_vstup+ " "+ hodnota +" " +str(count)
                i = j+1    #pripočítá se 1 a kontroluje další prvek (číslo)
            self.__compressed.append(encoded_vstup + '\n')

try:
    with open ("vstup_rle.txt", "r" , encoding="utf-8") as input, \
        open("vystup_rle.txt", "w", encoding="utf-8") as out:
        file = input.readlines()
        objekt = Komprese(file)
        objekt.encode()
        out.writelines(objekt.compressed)

except FileNotFoundError:
    print("Vstupní soubor neexistuje")
    exit()
except PermissionError:
    print("Program nemá právo číst vstupní soubor")
    exit()
except ValueError:
    print("Vstupní soubor obsahuje jiné znaky než číslice nebo jsou ve špatném formátu")
    exit()
except IndexError:
    print("Vstupní data nejsou ve správném formátu")
    exit()
except UnboundLocalError:
    print("Vstupní soubor je prázdný")
    exit()
