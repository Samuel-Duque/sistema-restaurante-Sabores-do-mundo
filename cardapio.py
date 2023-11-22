import pandas as pd
import ast
estoque_df = pd.read_csv('estoque.csv')
estoque = estoque_df.set_index('Item')['Quantidade'].to_dict()

cardapio = {"Lasanha":{"Trigo":2,"Tomate":1},
            "Bolo":{"Trigo":3,"Ovo":2},
            "Pizza":{"Trigo":2,"Tomate":1,"Queijo":1},
            "Pudim":{"Leite":1,"Ovo":2},
            "Torta":{"Trigo":2,"Ovo":2,"Tomate":1},
            "Stronoff":{"Carne":1,"Creme de Leite":1,"Tomate":1},
            "Feijoada":{"Feijão":1,"Carne":1,"Arroz":1,"Farofa":1,"Laranja":1},
            "Sopa":{"Carne":1,"Tomate":1,"Cebola":1,"Batata":1},
            "Salada":{"Tomate":1,"Alface":1,"Pepino":1,"Cenoura":1,"Beterraba":1,"Ovo":1,"Queijo":1},
            "Macarronada":{"Macarrão":1,"Tomate":1,"Queijo":1},
            "Carbonara":{"Macarrão":1,"Ovo":1,"Queijo":1,"Creme de Leite":1},
            "Risoto":{"Arroz":1,"Tomate":1,"Queijo":1},
            "Purê":{"Batata":1,"Creme de Leite":1,"Queijo":1},
            "Fetuccine":{"Macarrão":1,"Creme de Leite":1,"Queijo":1},
            "Nhoque":{"Batata":1,"Trigo":1,"Queijo":1},
            "Bife":{"Carne":1,"Cebola":1,"Tomate":1},
            "Omelete":{"Ovo":2,"Queijo":1},
            "Filet ao Molho Madeira":{"Carne":1,"Creme de Leite":1,"Cebola":1,"Tomate":1},
            "Filet au Poivre":{"Carne":1,"Creme de Leite":1,"Cebola":1,"Tomate":1},
            "Peixe":{"Peixe":1,"Cebola":1,"Tomate":1},
            "Frango grelhado":{"Frango":1,"Cebola":1,"Tomate":1},
            "Frango ao Molho Branco":{"Frango":1,"Creme de Leite":1,"Cebola":1,"Tomate":1},
            "Suco de Laranja":{"Laranja":2},"Suco de Limão":{"Limão":2},"Suco de Abacaxi":{"Abacaxi":2},
            "Suco de Morango":{"Morango":2},"Suco de Uva":{"Uva":2},"Agua":{"Agua":2},"Coca-Cola":{"Coca-Cola":2},
            "Guaraná":{"Guaraná":2},"Fanta":{"Fanta":2},"Sprite":{"Sprite":2}}


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