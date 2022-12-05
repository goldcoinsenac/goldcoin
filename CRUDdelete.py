from conexao import *

#input de dados

delete_telefone = input(str('Digite o número para cancelar o cadastro: '))

#Delete
comando_delete = f"DELETE FROM `bdgoldcoin`.`cadastros` WHERE (`telefone` = '{delete_telefone}');"
cursor.execute (comando_delete)
conexao.commit() #quando edita o banco de dados

cursor.close()
conexao.close()