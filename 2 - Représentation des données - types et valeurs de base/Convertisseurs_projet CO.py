# projet de conversions

loop=True
while loop: # boucle tant que loop est True
    enter_base = int(input("Base d'entrée: ")) # demande la base du nombre
    exit_base = int(input("Base de sortie: ")) # demande la base dans laquel le nombre va être converti
    if (enter_base != 2 and enter_base != 10 and enter_base != 16) or (exit_base != 2 and exit_base != 10 and exit_base != 16): # verifie si la base est 2, 10 ou 16
        print("Une des bases n'est pas conforme.") # si non, afficher la phrase
    else: # sinon
        loop=False # fin de la boucle

nb_conv=input('Nombre à convertir: ')

def base_2_10(nb_bin):
    #code base 2 -> base 10
    nb_dec=0
    for i in range(len(nb_bin)):
        poids=2**(len(nb_bin)-1-i) #pow(2,len(nb_bin-1-i))
        nb_dec=nb_dec+int(nb_bin[i])*poids
    return nb_dec

def base_10_2(nb_dec):
    #code base 10 -> base 2
    quotient=int(nb_dec)
    nb_bin=""
    while (quotient!=0):
        reste=quotient%2   #reste de la division euclidienne
        nb_bin=str(reste)+nb_bin
        quotient=quotient//2  #quotient de la division euclidienne
    return nb_bin

def base_16_2(nb_hex):
    #code base 16 -> base 2
    nb_dec=0
    for i in range(len(nb_hex)):
        if (nb_hex[i]=='A') or (nb_hex[i]=='a'):
            nb=10
        elif (nb_hex[i]=='B') or (nb_hex[i]=='b'):
            nb=11
        elif (nb_hex[i]=='C') or (nb_hex[i]=='c'):
            nb=12
        elif (nb_hex[i]=='D') or (nb_hex[i]=='d'):
            nb=13
        elif (nb_hex[i]=='E') or (nb_hex[i]=='e'):
            nb=14
        elif (nb_hex[i]=='F') or (nb_hex[i]=='f'):
            nb=15
        else:
            nb=int(nb_hex[i])
        poids=nb*(16**(len(nb_hex)-1-i))
        nb_dec=nb_dec+poids
        quotient=nb_dec
        nb_bin=""
        while (quotient!=0):
            reste=quotient%2
            nb_bin=str(reste)+nb_bin
            quotient=quotient//2
    return nb_bin

def base_10_16(nb_dec):
    #code base 10 -> base 16
    quotient=int(nb_dec)
    nb_hex=""
    while (quotient>0):
        reste=quotient%16   #reste de la division euclidienne
        if reste==10:
            reste='A'
        elif reste==11:
            reste='B'
        elif reste==12:
            reste=='C'
        elif reste==13:
            reste='D'
        elif reste==14:
            reste='E'
        elif reste==15:
            reste='F'
        else:
            reste=str(reste)
        nb_hex=reste+nb_hex
        quotient=quotient//16  #quotient de la division euclidienne
    return nb_hex

def base_2_16(nb_bin):
    #code base 2 -> base 16
    nb_dec=0
    for i in range(len(nb_bin)):
        poids=2**(len(nb_bin)-1-i) #pow(2,len(nb_bin-1-i))
        nb_dec=nb_dec+int(nb_bin[i])*poids
    quotient=nb_dec
    nb_hex=""
    while (quotient!=0):
        reste=quotient%16   #reste de la division euclidienne
        if 10<=reste<=15:   #if reste>=10 and reste<=15:
            reste=chr(reste+55)
        elif 0<=reste<=9:
            reste=chr(reste+48)
        nb_hex=reste+nb_hex
        quotient=quotient//16  #quotient de la division euclidienne
    return nb_hex

def base_16_10(nb_hex):
    #code base 16 -> base 10
    nb_dec=0
    for i in range(len(nb_hex)):
        if 65<=ord(nb_hex[i])<=70:      # A à F
            nb=ord(nb_hex[i])-55
        elif 97<=ord(nb_hex[i])<=102:   # a à f
            nb=ord(nb_hex[i])-87
        elif 48<=ord(nb_hex[i])<=57:    # 0 à 9
            nb=ord(nb_hex[i])-48

        poids=16**(len(nb_hex)-1-i)
        nb_dec=nb_dec+nb*poids
    return nb_dec

if enter_base == 2 and exit_base == 10:
    result = base_2_10(nb_conv)
elif enter_base == 10 and exit_base == 2:
    result = base_10_2(nb_conv)
elif enter_base == 16 and exit_base == 2:
    result = base_16_2(nb_conv)
elif enter_base == 10 and exit_base == 16:
    result = base_10_16(nb_conv)
elif enter_base == 2 and exit_base == 16:
    result = base_2_16(nb_conv)
elif enter_base == 16 and exit_base == 10:
    result = base_16_10(nb_conv)

print(f"Votre nombre en base {exit_base}:", result)
