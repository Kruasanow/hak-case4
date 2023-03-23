import olefile

def outd(file):
    file = str(file)
    File_Ole=file
    # assert olefile.isOleFile(File_Ole) # Проверка корректности OLE файла
    ole = olefile.OleFileIO(File_Ole)
    meta = ole.get_metadata() # Извлечение метаданных
    print('Дата создания файла:  '+str(meta.create_time)) # Вывод даты создания файла
    print('Дата последнего сохранения:  '+str(meta.last_saved_time))# Вывод даты сохранения файла
    meta.dump() # Вывод всех метаданных на экран
    metadump = meta.dump()
    # print(str(metadump))
    mct = str(meta.create_time)
    mlst = str(meta.last_saved_time)
    ole.close() # Закрытие файла
    return [metadump, mct, mlst]

# outd('output/data4.xls')