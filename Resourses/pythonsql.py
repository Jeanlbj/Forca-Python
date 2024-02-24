import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=BOOK-SEDCMSP2G4;"
    "Database=PalavrasForca"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem Sucedida!")

cursor = conexao.cursor()

palavras_fruta = ["MAÇA", "BANANA", "LARANJA", "UVA", "MORANGO", "ABACAXI", "MELANCIA", "PERA", "KIWI", "LIMAO",
                  "MANGA", "PESSEGO", "MELAO", "CEREJA", "AMEIXA", "GOIABA", "ABACATE", "FIGO", "PITAYA", "FRAMBOESA"]

palavras_carro = ["FUSCA", "GOL", "PALIO", "COROLLA", "CIVIC", "FOCUS", "UNO", "FIESTA", "ONIX", "HB20", "CELTA", "KA",
                  "SANDERO", "POLO", "FOX", "UP", "ETIOS", "LANCER", "CRUZE", "HRV"]

palavras_animal = ["CACHORRO", "GATO", "PASSARO", "TIGRE", "LEAO", "ELEFANTE", "GIRAFA", "CAVALO", "VACA", "PORCO",
                   "SAGUI", "HOMEM", "CAMELO", "COBRA", "MACACO", "RATO", "ABELHA", "BORBOLETA", "GALINHA", "PATO"]

for palavras in range(len(palavras_animal)):
    comando = f"""INSERT INTO Palavras (Fruta, Carro, Animal)
VALUES ('{palavras_fruta[palavras]}','{palavras_carro[palavras]}', '{palavras_animal[palavras]}');
"""

    cursor.execute(comando)
    cursor.commit()

print("Informações adicionadas")
