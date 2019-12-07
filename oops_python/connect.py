"""For Sql connection."""
import psycopg2


# connection = psycopg2.connect(user='postgres', password='download@123',
#  host='localhost', port=5432, database="banking")

# cursor = connection.cursor()
# print(connection.get_dsn_parameters())
# cursor.execute("SELECT version();")
# record = cursor.fetchone()
# print("You are connected to - ", record, "\n")
# cursor.close()
# connection.close()


def create_connection():
    """Creating Connection with Database."""
    try:
        connection = psycopg2.connect(user='postgres', password='download@123',
                                      host='localhost', port=5432,
                                      database="banking")
        print("Database Connectivity has been made")
        return connection
    except psycopg2.errors:
        print("Connnection hasn't been made.")


def create_table(cursor, connection, table_name, *table_params):
    """Create Table."""
    print(table_params)
    try:
        create_table_query = ('''CREATE TABLE {}{};'''.format(
                              table_name, table_params)
                              ).replace("'", "")
        cursor.execute(create_table_query)
        connection.commit()
        print("Table has been created")
    except:
        print("Table has already been created")
    # connection.close()


def insert_data(cursor, connection, table_name, *record):
    """Insert data into table."""
    # import pdb;pdb.set_trace()
    print(record)
    try:
        postgres_insert_query = (" INSERT INTO {}{} VALUES {};".format(
            table_name.replace("'", ""),
            str(record[0]).replace("'", ""), record[1])).replace('"', '')
        cursor.execute(postgres_insert_query)
        connection.commit()
        print("values inserted successfully")
    except:
        print("Cannot insert values")


def update_table(cursor, connection, table_name, **update_params):
    """Update Table."""
    try:
        sql_update_query = "Update {} set {} = '{}' where id = {};".format(
            table_name, list(update_params)[1],
            update_params[list(update_params)[1]], update_params['id'])
        cursor.execute(sql_update_query)
        connection.commit()
        print("values updated successfully")
    except psycopg2.errors:
        print("Cannot update values")


def drop_table(cursor, connection, table_name):
    """Delete Table."""
    try:
        sql_update_query = "DROP table {};".format(table_name)
        cursor.execute(sql_update_query)
        connection.commit()
        print("Table deleted successfully")
    except psycopg2.errors:
        print("Cannot delete the table")
    # connection.close()
