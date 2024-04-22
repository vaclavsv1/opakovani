cisla = [3,5,8,1,2,4,6,7]
serazeni_od_nejvetsiho = sorted(cisla, reverse=True)
serazeni_od_nejmensiho = sorted(cisla)
prumer = sum(cisla) /len(cisla)

print("Seřazení od největšího po nejmenší:", serazeni_od_nejvetsiho)
print("Seřazení od nejmenšího po nejvtší:", serazeni_od_nejmensiho)
print("Průměrná hodnota:", prumer)