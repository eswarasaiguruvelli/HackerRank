basic=int(input("enetr basic salary"))
DA=int(input("DA percentage"))
HRA=int(input("HRA percentage"))
hra=(basic*HRA)/100
da=(basic*DA)/100
gross=basic+hra+da
print(gross)