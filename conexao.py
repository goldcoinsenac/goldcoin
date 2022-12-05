#baixa a biblioteca mysql-connector-python
import mysql.connector #importar a biblioteca que conectará o python no BD no mysql

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root',
    database= 'bdgoldcoin',
)
cursor = conexao.cursor() #cursor é o elemento que vai criar a conexão com o BD


