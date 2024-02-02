# Inputando dados de preço e desconto
nome_produto = input('Digite o nome do produto: ')
preco_produto = int(input('Digite o preço do produto: '))
desconto_produto = int(input('Digite quanto porcento de desconto terá o produto: '))
valor_abatido = (preco_produto * desconto_produto) / 100
preco_final = preco_produto - valor_abatido
print('>' * 30)
print('>' * 30)
print(f'    Produto: {nome_produto}')
print(f'    Preço: {preco_produto}')
print(f'    Desconto: {desconto_produto}')
print('>' * 30)
print(f'    Preço final: {preco_final}')
print('>' * 30)
print('>' * 30)