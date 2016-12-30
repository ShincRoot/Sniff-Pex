#!/usr/bin/python3

from scapy.all import *
import os, sys
import platform

so = platform.system()

def limpar():  
    if  so == 'Windows':
	    os.system("cls")
    else:
	    os.system("clear")

limpar()


print ('''
..__________ __________, , ) 
/ `---___________---- _____|] ¦¦¦¦D 
/_==o;;;;;;;;__ _____.:/ 
..), ---.(_(__) /             
..// (..) ), ----"                SNIFF PEX 1.0
..//___//          
.//___// 
.//___//                          
                                                         <by Shinc>
''')
nome = input("\n\n\n nome do arquivo pcap (com extensão .pcap): ")
print('''
	#############################
	#                           #
        #Para parar aperte ctrl + c #
	#                           #
	#############################
	''')


pacote = sniff()
wrpcap(nome, pacote)


resp = input("\n\nO Arquivo Fica Salvo No Diretorio Do Script \n\n\nPara Ler os Arquivos Digite Ler.\n\n\nPara Fechar o Script digite Fechar: " )

if resp == "Fechar":
	print ("obrigado por usar <by Shinc>")
if resp == "Ler":
	limpar()
	os.system('')
	pacoteLer = rdpcap(nome)
	op = int(input("Para Ver os Arquivos que Foram Recebidos Digite 1\n\nPara Ver Todos Arquivos em Hex Digite 2\n\nPara Ver Todos os Arquivos em Raw digite 3\n\nSua Resp: "))
	if op == 1:
		pacote.show()
	if op == 2:
		pacote.hexdump()
	if op == 3:
		pacote.hexraw()