from read_witch_excel import load_data_from_excel
from save_data_from_excel import save_data_from_excel
import os
from supabase import create_client, Client
from dotenv import load_dotenv
def add_value(_data, name_tabel):
  load_dotenv()
  url: str = 'https://nyyvpojadixruopwdksr.supabase.co'
  key: str = os.environ.get("KEY")
  supabase: Client = create_client(url, key)
  data, count = supabase.table(name_tabel).insert(_data).execute()
  print(data, count, end="\n")
  response = supabase.table(name_tabel).select("*").execute()
  print(response)

def main(file_path, sheet_name, name_tabel):
    data = load_data_from_excel(file_path, sheet_name)
    # save_data_from_excel("../db.sqlite3", name_tabel, data=data)
    for item in data:
        add_value(item, name_tabel)


if __name__ == '__main__':
    file_path = "dane.xlsx"
    # sheet_name = "Dane"
    # name= "api_place"
    # main(file_path, sheet_name, name)
    name= "api_rating"
    sheet_name = "ocena"
    main(file_path, sheet_name, name)

