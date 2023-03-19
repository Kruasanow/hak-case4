import olefile
File_Ole='data4.xls'
assert olefile.isOleFile(File_Ole) # Проверка корректности OLE файла
ole = olefile.OleFileIO(File_Ole)
meta = ole.get_metadata() # Извлечение метаданных
print('Дата создания файла:  '+str(meta.create_time)) # Вывод даты создания файла
print('Дата последнего сохранения:  '+str(meta.last_saved_time))# Вывод даты сохранения файла
meta.dump() # Вывод всех метаданных на экран
ole.close() # Закрытие файла