# Scanner de IPs

## Descrição
O objetivo deste projeto é receber uma lista de endereços IPs e realizar um scan para identificar e listar todos os IPs válidos contidos nessas faixas de endereço. O resultado é armazenado em um arquivo de texto.

## Autora
Gabrielly Alves

Contato: gabriellysthefany.alves@gmail.com

## Funcionalidades
- Salvar IPs em Arquivo: A função salvar_ips_em_arquivo(lista_ips, nome_arquivo) recebe uma lista de IPs para varredura e gera um arquivo de saída com os IPs válidos.
- Identificação de IPs Únicos: IPs que possuem máscara '255.255.255.255' são identificados como únicos e são listados individualmente no arquivo de saída.
- Identificação de Faixas de IPs: Para IPs que não são únicos, o programa identifica a faixa de IPs e lista todos os IPs dentro dessa faixa no arquivo de saída.

## Utilização
Para usar esta função, siga estes passos:

1. Input de IPs: Passe uma lista de IPs para a função salvar_ips_em_arquivo(lista_ips, nome_arquivo).
2. Estrutura da Lista: A lista deve conter IPs no formato 'X.X.X.X/Máscara' (por exemplo, '000.000.0.0/24').
3. Saída: Será gerado um arquivo de texto com a listagem dos IPs válidos identificados na varredura.

Exemplo de uso:
lista_ips = ['000.000.0.0/24', '11.1.1.1/8', '8.8.8.8/32']
nome_arquivo = 'ips_validos.txt'

salvar_ips_em_arquivo(lista_ips, nome_arquivo)


## Requisitos
Este projeto foi desenvolvido em Python e requer a versão 3.10 ou superior para funcionar corretamente.
