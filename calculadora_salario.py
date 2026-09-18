print("\nGustavo Vicente")
print("André")
print("Beatriz")
print("Julia")
print('-----------------------------')
print("\nExercício 01")

#-------------------------------------------------------------------

def AliqINSS(salarioBruto):
    if salarioBruto > 8157.42:
        return 0
    if salarioBruto > 4190.84:
        return 0.14
    if salarioBruto > 2793.89:
        return 0.12
    if salarioBruto > 1518.01:
        return 0.09
    return 0.075


def DeducaoINSS(salarioBruto):
    if salarioBruto > 8157.42:
        return 951.62
    if salarioBruto > 4190.84:
        return 190.40
    if salarioBruto > 2793.89:
        return 106.59
    if salarioBruto > 1518.01:
        return 22.77
    return 0.00


def IR(salarioBruto, VALINSS):
    return salarioBruto - VALINSS


def AliqIR(baseIR):
    if baseIR > 4664.68:
        return 0.275
    if baseIR > 3751.05:
        return 0.225
    if baseIR > 2826.65:
        return 0.15
    if baseIR > 2259.20:
        return 0.075
    return 0.0


def DeducaoIR(baseIR):
    if baseIR > 4664.68:
        return 896.00
    if baseIR > 3751.05:
        return 662.77
    if baseIR > 2826.65:
        return 381.44
    if baseIR > 2259.20:
        return 169.44
    return 0.00


def saida(lstSalarios):
    nome_arquivo = "CALCULOS.txt"
    arquivo = open(nome_arquivo, "w")

    header = (
        f"{'Bruto':>10} {'AliqINSS':>10} {'Val.INSS':>12} "
        f"{'Base IR':>12} {'AliqIR':>10} {'Val.IR':>10} {'Líquido':>12}\n"
        + "-" * 82 + "\n"
    )

    print()
    print(header, end="")
    arquivo.write(header)

    for p in lstSalarios:
        linha = (
            f"{p['SalBruto']:10.2f} "
            f"{p['AliqINSS']*100:9.2f}% "
            f"{p['VALINSS']:12.2f} "
            f"{p['IR']:12.2f} "
            f"{p['AliqIR']*100:9.2f}% "
            f"{p['VALIR']:10.2f} "
            f"{p['SalLiquido']:12.2f}\n"
        )

        print(linha, end="")
        arquivo.write(linha)

    arquivo.close()
    print("\nArquivo 'CALCULOS.txt' gravado com sucesso!")


lstSalarios = []

SalBruto = float(input('\nDigite o salário: '))
while SalBruto != 0:
    VALINSS = abs(SalBruto * AliqINSS(SalBruto) - DeducaoINSS(SalBruto))
    calculoIR = IR(SalBruto, VALINSS)
    VALIR = calculoIR * AliqIR(calculoIR) - DeducaoIR(calculoIR)

    if VALIR < 10:
        VALIR = 0.0

    SalLiquido = SalBruto - VALINSS - VALIR

    lstSalarios.append(
        {
            "SalBruto": SalBruto,
            "AliqINSS": AliqINSS(SalBruto),
            "VALINSS": VALINSS,
            "IR": calculoIR,
            "AliqIR": AliqIR(calculoIR),
            "VALIR": VALIR,
            "SalLiquido": SalLiquido,
        }
    )

    SalBruto = float(input('Digite o salário: '))

lstSalarios_ordenada = sorted(lstSalarios, key=lambda item: item["SalBruto"])
saida(lstSalarios_ordenada)

print("\nFim do programa.")
