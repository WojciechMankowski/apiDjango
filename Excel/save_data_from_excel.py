from django.db import transaction
import  sqlite3

from read_witch_excel import load_data_from_excel


def save_data_from_excel(name_db: str, name_table: str, data):
    connect = sqlite3.connect(name_db)
    cursor = connect.cursor()

    for record in data:
        columns = ", ".join(record.keys())
        _values = ", ".join(['?']* len(record))
        value = tuple(record.values())

        query = f'INSERT INTO {name_table} ({columns}) VALUES ({_values})'
        cursor.execute(query, value)
    connect.commit()
    connect.close()


if __name__ == '__main__':
    file_path = "dane.xlsx"
    sheet_name = "Dane"
    data = load_data_from_excel(file_path, sheet_name)
    save_data_from_excel("", "", data=data)