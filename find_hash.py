import hashlib
import openpyxl

def calculate_hash(name):
    column = 10
    file_path = name
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active
    hash_obj = hashlib.sha256()
    for row in worksheet.iter_rows(min_col=column, max_col=column, values_only=True):
        cell_value = row[0]
        if cell_value is not None:
            hash_obj.update(str(cell_value).encode())
    return hash_obj.hexdigest()


def calculate_string_hash(input_string):
    hash_function = hashlib.sha256
    hash_obj = hash_function()
    hash_obj.update(input_string.encode('utf-8'))
    return hash_obj.hexdigest()






name = 'data4.xlsx'
print('Хеш-сумма столбца J:', calculate_hash(name))
print('хеш функция имени пользователя:',calculate_string_hash(name))