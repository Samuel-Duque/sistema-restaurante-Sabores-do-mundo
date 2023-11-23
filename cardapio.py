import pandas as pd
import ast
estoque_df = pd.read_csv('estoque.csv')
estoque = estoque_df.set_index('Item')['Quantidade'].to_dict()

cardapio_df = pd.read_csv('cardapio.csv')

# Converte a coluna'Ingredientes' de string p/ dicionario
cardapio_df['Ingredientes'] = cardapio_df['Ingredientes'].apply(ast.literal_eval)

# Cria um dicionario com o nome da comida como chave e os ingredientes como valor
cardapio = cardapio_df.set_index('Comida')['Ingredientes'].to_dict()

i = 0
while (i<2):
    comida = input("Qual comida você quer?: ")
    for item in estoque:
        if item in cardapio[comida] and estoque[item] >= cardapio[comida][item]:
            estoque[item] -= cardapio[comida][item]
    i=i+1


estoque_df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])
estoque_df.to_csv('estoque.csv', index=False)