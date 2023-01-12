year = int(input("Année: "))
if (year%4==0 or year%400==0) and year%100!=0 and year>1582:
    print(year, "est une année bissextile")
else:
    print(year, "n'est pas une année bissextile")
