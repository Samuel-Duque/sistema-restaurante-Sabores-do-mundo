import pandas as pd
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
            "Nhoque":{"Batata":1,"Trigo":1,"Queijo":1}}




i = 0
while (i<2):
    comida = input("Qual comida você quer?: ")
    for item in estoque:
        if item in cardapio[comida] and estoque[item] >= cardapio[comida][item]:
            estoque[item] -= cardapio[comida][item]
    i=i+1

print(estoque)

cardapio_df = pd.DataFrame(list(cardapio.items()), columns=['Comida', 'Ingredientes'])
estoque_df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])

cardapio_df.to_csv('cardapio.csv', index=False)
estoque_df.to_csv('estoque.csv', index=False)