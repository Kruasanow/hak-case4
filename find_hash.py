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


# def calculate_string_hash(file):
#     hash_obj = hashlib.sha256()
#     file_contents = file.read()  # read the contents of the file from the BytesIO object
#     hash_obj.update(file_contents)  # update the hash object with the file contents
#     return hash_obj.hexdigest()
def calculate_string_hash(input_string):
    hash_function = hashlib.sha256
    hash_obj = hash_function()
    hash_obj.update(input_string.encode('utf-8'))
    return hash_obj.hexdigest()


# def calculate_all_hash(all_data_dict):
#     input_string = ''.join([str(element) for pair in all_data_dict.items() for element in pair])
#     hash_function = hashlib.sha256
#     hash_obj = hash_function()
#     hash_obj.update(input_string.encode('utf-8'))
#     return hash_obj.hexdigest()




# name = 'data4.xlsx'
# print('Хеш-сумма столбца J:', calculate_hash(name))
# print('хеш функция имени пользователя:',calculate_string_hash(name))