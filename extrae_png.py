import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(photo):
    print("Reading BLOB data from sys_empresa table")

    try:
        connection = mysql.connector.connect(host='srv_db_nacional',
            database='llopart, matias fact', user='root', password='root')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT logo from sys_empresa"""

        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            image = row[0]
            print("Storing image on disk \n")
            write_file(image, photo)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

readBLOB("logo.png")