# Umwandlung Sexagesimalsystem in Dezimalsystem und andersherum

def menu():
    print("\nWählen Sie eine Option, indem Sie die Nummer unten eingeben")
    print("\n1. Sexagesimal in Dezimal")
    print("2. Dezimal in Sexagesimal")
    print("3. Exit")
    pick = int(input("Gib deine Wahl hier ein: "))
    return pick 
    
def inDezimal(s):
    e = int(s[3:5])
    f = e*60
    g = int(s[0:2])
    h = g*3600
    i = int(s[6:8]) + f + h
    ans = str(round(i/3600, 2))
    return ans+chr(186)
    
def inSexagesimal(d):
    x = float(d[:-1])
    y = x - int(x)
    z = y*60
    c = z - int(z)
    n = c*60
    return str(str(int(x)) + chr(186) + str(int(z)) + "'" + str(int(n)) + '"')
    
def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            #wandle S in D um
            s = (input("Gib Sexagesimal hier ein: "))
            print(inDezimal(s))
        elif choice == 2:
            #wandel D in S um
            d = (input("Gib die Dezimalzahl hier ein: "))
            print(inSexagesimal(d))
        else:
            print("Ungueltige Eingabe")
            
        choice = menu()
        
if __name__ == '__main__':
    main()

###evaluate###
    #52.12525° = 52°07'30"
    #48.177455556° = 48°10'38"
    #16°19'28.29" = 16.324525° 
