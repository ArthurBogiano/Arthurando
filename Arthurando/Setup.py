import os
from Data.Cores_lines import *

# iniciando instalação dos programas necessarios

up = os.system('apt-get update')
msf = os.system('apt-get install metasploit-framework')

if up == 1:
    print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
          f' do comando : apt-get update')
if msf == 1:
    print(f'     {branco}[{vermelho}ATENÇÃO !!!{branco}]{vermelho}  Algum erro ocorreu no processamento'
          f' do comando : apt-get install metasploit-framework')
