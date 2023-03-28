import zipfile
import os

def create_hidden_file(hidden_string):
    hidden_filename = ".hidden_file.txt"
    with open(hidden_filename, "w") as f:
        f.write(hidden_string)
    return hidden_filename
 
def add_hidden_file_to_zip(zip_filename, hidden_filename):
    with zipfile.ZipFile(zip_filename, "a") as zipf:
        zipf.write(hidden_filename)
 
    # Удаляем временный скрытый файл после добавления в архив
    os.remove(hidden_filename)
 
# Скрытая строка
hidden_string = "Секретная информация"
 
# Создайте скрытый файл с секретной строкой
hidden_filename = create_hidden_file(hidden_string)
 
# Добавьте скрытый файл в архив
zip_filename = "data4.zip"
add_hidden_file_to_zip(zip_filename, hidden_filename)