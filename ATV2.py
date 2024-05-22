funcionarios = {}

def inicio(funcionarios):
    opcao = None
    while opcao !=7:
        print("\nMenu:")
        print("1 - Inserir Funcionários")
        print("2 - Remover Funcionários")
        print("3 - Determinar a folha de pagamento de um determinado funcionário")
        print("4 - Determinar um relatório com o salário bruto e líquido de todos os funcionários")
        print("5 - Imprimir as informações do funcionário com maior salário líquido")
        print("6 - Imprimir as informações do funcionário com o maior número de faltas no mês")
        print("7 - Sair")
        opcao = int(input("Selecione a opção desejada: "))

        if opcao==1:
            inserir(funcionarios)
        elif opcao==2:
            remover(funcionarios)
        elif opcao==3:
            folha_pagamento(funcionarios)
        elif opcao==4:
            relatorio_sal(funcionarios)
        elif opcao==5:
            funcionario_maior_liquido(funcionarios)
        elif opcao==6:
            funcionario_maior_falta(funcionarios)
        elif opcao==7:
            print("Saindo do programa...")
        else:
            print("Opção inválida!")
def inserir(funcionarios):
    matricula = int(input("Digite a matrícula: "))
    nome = input("Digite o nome: ")
    cod_funcao = int(input("Informe o código da função: "))
    num_falta = int(input("Informe as faltas no mês: "))

    if cod_funcao == 101:
        vol_vendas = float(input("Informe o volume no mês: "))
        sal_bruto = 1500 + (vol_vendas * 0.09)
    elif cod_funcao == 102:
        sal_bruto = float(input("Informe o salário: "))

    if sal_bruto <= 2259.20:
        imposto = 0
    elif sal_bruto >= 2259.21 and sal_bruto <= 2828.65:
        imposto = 7.5
    elif sal_bruto >= 2828.66 and sal_bruto <= 3751.05:
        imposto = 15
    elif sal_bruto >= 3751.06 and sal_bruto <= 4664.68:
        imposto = 22.5
    else:
        imposto = 27.5

    funcionario = {"matricula": matricula, "nome": nome, "cod_funcao": cod_funcao, "sal_bruto": sal_bruto, "faltas": num_falta, "imposto": imposto}
    funcionarios[matricula] = funcionario

def remover(funcionarios):
    matricula = int(input("Informe qual matrícula deseja remover: "))
    if matricula in funcionarios:
        del funcionarios[matricula] 
        print("Funcionário removido!")
    else: 
        print("Funcionário não encontrado!")

def folha_pagamento(funcionarios):
    matricula = int(input("Informe a matrícula do funcionário: "))
    if matricula in funcionarios:
        funcionario = funcionarios[matricula]
        sal_liquido = calc_sal_liquido(funcionario)
        print(f"Matrícula: {funcionario['matricula']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Código Funçaõ: {funcionario['cod_funcao']}")
        print(f"Salário Bruto: {funcionario['sal_bruto']}")
        print(f"Imposto: {funcionario['imposto']}")
        print(f"Salário Líquido: {funcionario['sal_liquido']}")
    else:
        print("Funcionário não encontrado!")
    
def relatorio_sal(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado!")
        return 
    print("Matricula | Nome | Código da Função | Salário Bruto | Salário Líquido ")
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        salario_liquido = calc_sal_liquido(funcionario)
        print(f"{funcionario['matricula']} | {funcionario['nome']} | {funcionario['cod_funcao']} | {funcionario['sal_bruto']} | {salario_liquido}")

def funcionario_maior_liquido(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado!")
        return
    funcionario_maior_liquido = None
    maior_sal_liquido = -1
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        salario_liquido = calc_sal_liquido(funcionario)
        if salario_liquido > maior_sal_liquido:
            funcionario_maior_liquido = funcionario
            maior_sal_liquido = salario_liquido
    
    if maior_sal_liquido:
        imprimir_info_funcionario(funcionario_maior_liquido, maior_sal_liquido)

def funcionario_maior_falta(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado!")
        return
    funcionario_maior_falta = None
    maior_num_falta= -1
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        if funcionario["faltas"] > maior_num_falta:
            funcionario_maior_falta = funcionario
            maior_num_falta = funcionario["faltas"]
    
    if funcionario_maior_falta:
        desconto = funcionario_maior_falta["faltas"] * (funcionario_maior_falta["sal_bruto"] / 30)
        print(f"Matrícula: {funcionario_maior_falta['matricula']}")
        print(f"Nome: {funcionario_maior_falta['nome']}")
        print(f"Código da Função: {funcionario_maior_falta['cod_funcao']}")
        print(f"Número de Faltas: {funcionario_maior_falta['faltas']}")
        print(f"Desconto no Salário: {desconto}")

def calc_sal_liquido(funcionario):
    desconto = (funcionario["sal_bruto"] / 30) * funcionario["faltas"]
    imposto = funcionario["sal_bruto"] * (funcionario["imposto"] / 100)
    return funcionario["sal_bruto"] - imposto - desconto

def imprimir_info_funcionario(funcionario, salario_liquido):
    print(f"Matrícula: {funcionario['matricula']}")
    print(f"Nome: {funcionario['nome']}")
    print(f"Código da Função: {funcionario['cod_funcao']}")
    print(f"Salário Bruto: {funcionario['sal_bruto']}")
    print(f"Percentual de Imposto: {funcionario['imposto']}%")
    print(f"Salário Líquido: {salario_liquido}")

inicio(funcionarios)