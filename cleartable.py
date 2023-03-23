from openpyxl import load_workbook
from openpyxl.styles import Font

def outdd(fileway):
    # загружаем существующий файл Excel
    workbook = load_workbook(filename=fileway)

    # получаем активный лист
    worksheet = workbook.active

    # устанавливаем высоту строки
    worksheet.row_dimensions[1].height = 0

    # записываем значение в ячейку
    worksheet['J1'] = 'Скрытая строка'

    # применяем форматирование шрифта, чтобы скрыть содержимое ячейки
    worksheet['J1'].font = Font(color='ffffff')
    
    # сохраняем файл Excel
    workbook.save(filename='output/file2.xlsx')