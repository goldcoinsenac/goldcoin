from conexao import *
#Read
comando_read = """SELECT * FROM bdgoldcoin.cadastros;"""
cursor.execute = comando_read
resultado = cursor.fetchall() #ler o banco de dados
    print("Total rows are:  ", len(resultado))
    print("Printing each row")
    for row in resultado:
        print("Nome: ", row[1])
        print("Telefone: ", row[2])
        print("Email: ", row[3])
        print("\n")

cursor.close()
conexao.close()