"""User Info page."""
import random
from common.validation import int_validation, confirmation
from connect import create_connection, create_table, insert_data, update_table, drop_table


class User:
    """Class to get the user Info."""

    def __init__(self):
        """Init method."""
        self.connection = create_connection()
        self.cursor = self.connection.cursor()
        self.table_name = input("Enter table name: ")
        self.table_tuple = self.table_columns()
        create_table(self.cursor, self.connection, self.table_name,
                     *self.table_tuple)
        self.user_info = self.user_info(*self.table_tuple)
        insert_data(self.cursor, self.connection, self.table_name,
                    *self.user_info)
        permission = input("Do you want to update a table(y/n): ")
        if permission == 'y':
            self.update_params = self.update_params()
            update_table(self.cursor, self.connection, self.table_name,
                         **self.update_params)
        else:
            pass
        permission = input("Do you want to drop a table(y/n): ")
        while permission == 'y':
            if permission == 'y':
                table_name = input("Enter the table name")
                drop_table(self.cursor, self.connection, table_name)
                permission = input("Do you want to drop a table(y/n): ")
            else:
                break
        self.connection.close()


    # def crud_operations(self):
    #     """For personel info."""
    #     ctx = (self.first_name, self.last_name, self.account_number,
    #            self.phone_number, self.balance)
    #     # ctx['FIRST_NAME'] = self.first_name
    #     # ctx['LAST_NAME'] = self.last_name
    #     # ctx['ACCOUNT_NO'] = self.account_number
    #     # ctx['PHONE_NO'] = self.phone_number
    #     # ctx['BALANCE'] = self.balance
    #     insert_data(self.cursor, self.connection, self.table_name, *ctx)

    def user_info(self, *input_params):
        """For user info."""
        input_list = []
        column_list = []
        input_params = list(input_params)
        input_params.remove(input_params[0])
        for value in input_params:
            self.value = input('Enter the ' + value.split(" ")[0].upper() + ':'
                               )
            column_list.append(value.split(" ")[0].upper())
            if value.split(" ")[1] == 'INT':
                self.value = int(self.value)
            input_list.append(self.value)
        return tuple(column_list), tuple(input_list)

    def table_columns(self):
        """For dynamic table columns."""
        table_dict = {}
        total_columns = int(input("Enter number of columns: "))
        for i in range(0, total_columns):
            column_name = input("Enter column name: ")
            table_dict[column_name] = []
            count = 0
            while count < 2:
                column_params = input("Enter colmun attrs(eg:type, notnull)")
                table_dict[column_name].append(column_params)
                count += 1
        table_column = ['id SERIAL PRIMARY KEY']
        for column_name, column_params in table_dict.items():
            column = column_name.replace(" ", "_") + ' ' + column_params[0].upper() + ' ' + column_params[1].upper()
            table_column.append(column)
        return (tuple(table_column))

    def update_params(self):
        """For getting update parameters."""
        update_value_dict = {}
        update_id = int(input("Enter the ID for updation: "))
        update_value_dict['id'] = update_id
        column_name = input("Enter the column name").upper()
        update_value_dict[column_name] = input(
            "Enter the value that is to be inserted: ")
        print(update_value_dict)
        return update_value_dict
