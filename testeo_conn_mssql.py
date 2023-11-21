import pymssql

cnn = pymssql.connect(server='172.16.140.220',
                      user='sacx',
                      password='A71cx4321',
                      database='Operaciones')

print(cnn)
cursor = cnn.cursor()
cursor.execute("SELECT a.IdAeronave, a.Descripcion from Aeronaves a ")

row = cursor.fetchall()
print(row)

cursor.close()
cnn.close()