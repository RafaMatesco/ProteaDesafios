
nome = input("")


TotalHoras = int(input(""))


GanhoHora = float(input(""))


dependentes = int(input(""))


SalarioBruto = TotalHoras * GanhoHora

entitled = False
if dependentes > 3:
    entitled = True
    AumentoSalario = SalarioBruto * 0.03 * (dependentes - 3)
    SalarioFinal = SalarioBruto + AumentoSalario

print(nome)

if entitled == True:
    print(SalarioFinal)
    print(AumentoSalario)
else:
    print(SalarioBruto)