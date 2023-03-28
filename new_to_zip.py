import zipfile
import openpyxl

def create_archive_with_hidden_string(excel_file_path, archive_path, hidden_string, name):
    # Создание архива
    with zipfile.ZipFile(archive_path, 'w') as archive:
        # Добавление готового Excel файла в архив
        archive.write(excel_file_path)
        # Создание скрытого текстового файла и добавление его в архив
        with open('hidden_file.txt', 'w') as hidden_file:
            hidden_file.write(hidden_string)
        archive.write('hidden_file.txt', arcname='.hidden_file.txt')
        archive.comment = name
        # Установка пароля на архив
        archive.setpassword(b'my_password')

        # Закрытие архива
        archive.close()


def extract_hidden_string(archive_path, password):
    # Извлечение скрытого текстового файла из архива
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.setpassword(password.encode())
        archive.extract('.hidden_file.txt')
        # Чтение содержимого скрытого файла
        with open('.hidden_file.txt', 'r') as hidden_file:
            hidden_string = hidden_file.read()
        # Удаление временного скрытого файла
        archive.close()
        return hidden_string

# Путь к Excel файлу
excel_file_path = 'data4.xlsx'
# Путь к архиву
archive_path = 'my_archive.zip'
# Скрытая строка
hidden_string = 'This is a hidden string.'
name = b'agent007'
# Создание архива с Excel файлом и скрытой строкой
create_archive_with_hidden_string(excel_file_path, archive_path, hidden_string, name)

# Извлечение скрытой строки из архива
hidden_string_extracted = extract_hidden_string(archive_path, 'my_password')
print(hidden_string_extracted)