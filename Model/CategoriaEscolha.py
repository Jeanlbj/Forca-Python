import random

import pyodbc


class CategoriaEscolha:

    def __int__(self):
        pass

    def escolha_aleatoria(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=BOOK-SEDCMSP2G4;'
                              'Database=PalavrasForca;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()

        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Palavras'")
        nomes_colunas = cursor.fetchall()
        colunas = []
        for nome_coluna in nomes_colunas:
            colunas.append(nome_coluna.COLUMN_NAME)
        coluna_escolhida = colunas[random.randint(0, len(colunas) - 1)]

        cursor.execute(f'SELECT {coluna_escolhida} FROM Palavras')
        palavras_coluna = cursor.fetchall()
        palavras = []
        for palavra in palavras_coluna:
            palavras.append(palavra)
        palavra_escolhida = "".join(palavras[random.randint(0, 19)])

        cursor.close()
        conn.close()

        return palavra_escolhida

    def escolha_categoria(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=BOOK-SEDCMSP2G4;'
                              'Database=PalavrasForca;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()

        self.exibir_categorias()

        while True:

            opcao = int(input("\nEscolha a categoria: "))
            if opcao != 1 and opcao != 2 and opcao != 3:
                print("Opção invalida, digite novamente.")

            if opcao == 1:
                categoria_escolhida = "Fruta"
                break
            else:
                if opcao == 2:
                    categoria_escolhida = "Carro"
                    break
                else:
                    if opcao == 3:
                        categoria_escolhida = "Animal"
                        break

        cursor.execute(f'SELECT {categoria_escolhida} FROM Palavras')
        palavras_coluna = cursor.fetchall()
        palavras = []
        for palavra in palavras_coluna:
            palavras.append(palavra)
        palavra_escolhida = "".join(palavras[random.randint(0, 19)])

        cursor.close()
        conn.close()

        return palavra_escolhida

    def exibir_categorias(self):
        print("\n=== Categorias ===")
        print("1 - Fruta")
        print("2 - Carro")
        print("3 - Animal")
        print("============")
