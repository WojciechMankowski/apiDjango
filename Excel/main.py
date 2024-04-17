from read_witch_excel import load_data_from_excel
from save_data_from_excel import save_data_from_excel



def main(file_path, sheet_name, name_tabel):
    data = load_data_from_excel(file_path, sheet_name)
    save_data_from_excel("../db.sqlite3", name_tabel, data=data)


if __name__ == '__main__':
    file_path = "dane.xlsx"
    sheet_name = "Dane"
    name= "api_place"
    main(file_path, sheet_name, name)
    name= "api_rating"
    sheet_name = "ocena"
    main(file_path, sheet_name, name)

