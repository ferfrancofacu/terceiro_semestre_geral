import sqlite3
from contextlib import closing

connection = sqlite3.connect( "db.db")

# sqlalchemy -> framework sqlite3

# Criando estrutura do BD
create_sql = """
CREATE TABLE IF NOT EXISTS Pessoa (
      id integer primary key autoincrement(),
      nome TEXT NOT NULL,
      email TEXT NOT NULL
    )
"""
cursor = connection.cursor()
cursor.execute(create_sql)
connection.commit()

cursor.execute('DELETE FROM Pessoa')

insert_sql = """
INSERT INTO Pessoa(nome, email)
VALUES 
('Nome Completo', 'nome.completo@email.com')
"""

insert_sql_2 = """
INSERT INTO Pessoa(nome, email)
VALUES 
('Nome Completo', 'nome2.completo@email.com')
"""

updade_sql = """
UPDATE Pessoa 
SET nome = 'Fernando', email='fernando.franco@aluno.faculdadeimpacta.com.br'
WHERE id = '1'
"""

delete_sql = """
DELETE FROM Pessoa WHERE id = '2'
"""

def selectAllrows(cursor):
    select_sql = """
        SELECT * FROM PESSOA
    """
    cursor.execute(select_sql)
    rows = cursor.fetchall()

    print('fetchall - todas as linhas na memoria')
    for row in rows:
        print("valores:", row[0], row[1], row[2])
    print('---------')
    print(' ')
    print('fetchall - todas as linhas na memoria')
    cursor.execute(select_sql)
    rows = cursor.fetchmany(3)

    for row in rows:
        print("valores:", row[0], row[1], row[2])
    print('---------')


cursor.execute(insert_sql)

select_sql = """
        SELECT * FROM PESSOA
    """

print(' ')
print('fetchone - uma linha')
cursor.execute(select_sql)
rows = cursor.fetchone()
print("valores:", rows[0], rows[1], rows[2])

cursor.execute(insert_sql_2)
selectAllrows(cursor)

cursor.execute(updade_sql)
selectAllrows(cursor)

cursor.execute(delete_sql)
selectAllrows(cursor)

connection.commit()

cursor.close()
connection.close()
