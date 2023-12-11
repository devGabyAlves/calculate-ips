import ipaddress

def salvar_ips_em_arquivo(lista_ips, nome_arquivo):
    total_ips_adicionados = 0
    
    with open(nome_arquivo, 'w') as arquivo:
        for ip_com_mascara in lista_ips:
            ip, mascara = ip_com_mascara.split('/')
            try:
                if mascara == '255.255.255.255':
                    arquivo.write(f"{ip}\n")
                    total_ips_adicionados += 1
                    print(f"Ip único: {ip}")
                else:
                    endereco_ip = ipaddress.IPv4Network(ip_com_mascara, strict=False)
                    lista_ips = list(endereco_ip)
                    ips_a_imprimir = lista_ips[1:-1]
                    arquivo.write(','.join(str(ip) for ip in ips_a_imprimir))
                    arquivo.write('\n')  # Adiciona uma linha em branco entre os IPs
                    total_ips_adicionados += len(ips_a_imprimir)
                    print(f"Ips para a faixa {ip_com_mascara}:")
                    print(', '.join(str(ip) for ip in ips_a_imprimir))
                print()  # Adiciona uma linha em branco entre as faixas na tela
            except ValueError:
                arquivo.write(f"{ip_com_mascara}\n")  # Se houver erro, escreve o IP diretamente
                print(f"Faixa inválida: {ip_com_mascara}")
    
    print(f"Total de IPs adicionados ao arquivo: {total_ips_adicionados}")

# Lista de IPs
ips = [
    'Passe a lista de IPs aqui. separados por vírgula'
]

nome_do_arquivo = 'ips.txt'
salvar_ips_em_arquivo(ips, nome_do_arquivo)
print(f"Total de IPs na lista novos_ips: {len(ips)}")
