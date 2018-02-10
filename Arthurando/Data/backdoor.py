import Data.metasploit as msf


def done(payload):
    if payload[0] == 1 and payload[1] in msf.android:
        msf.gera_payloads(nome=payload[4], formato='apk', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 2 and payload[1] in msf.linux:
        msf.gera_payloads(nome=payload[4], formato='elf', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 3 and payload[1] in msf.windows:
        msf.gera_payloads(nome=payload[4], formato='exe', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 4 and payload[1] in msf.windows:
        msf.gera_payloads(nome=payload[4], formato='msi', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 5 and payload[1] in msf.mac:
        msf.gera_payloads(nome=payload[4], formato='macho', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 6 and payload[1] in msf.linux or msf.windows:
        msf.gera_payloads(nome=payload[4], formato='jsp', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 7 and payload[1] in msf.php:
        msf.gera_payloads(nome=payload[4], formato='php', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 8 and payload[1] in msf.python:
        msf.gera_payloads(nome=payload[4], formato='py', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 9 and payload[1] in msf.linux or msf.windows:
        msf.gera_payloads(nome=payload[4], formato='asp', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 10 and payload[1] in msf.windows:
        msf.gera_payloads(nome=payload[4], formato='dll', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 11 and payload[1] in msf.linux or msf.windows:
        msf.gera_payloads(nome=payload[4], formato='war', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])
    elif payload[0] == 12 and payload[1] in msf.windows:
        msf.gera_payloads(nome=payload[4], formato='vbs', tipo=payload[1],
                          ip=payload[2], port=payload[3], encoder=payload[5])

def done2(lista):
    msf.fusao(nome=lista[0], origem=lista[1], ip=lista[2], port=lista[3])
