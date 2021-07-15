import openpyxl


def get_data_xls():
    book = openpyxl.open('out.xlsx', read_only=True)
    sheet = book.active


    data = []
    for row in range(3, sheet.max_row + 1):
        data.append({'name': sheet[row][3].value,
                    # Опубликовано за текущий
                    'inn': sheet[row][4].value,
                     'gz': sheet[row][13].value,
                     'pfhd':sheet[row][15].value,
                     'intmoney':sheet[row][16].value,
                     'bsmeta': sheet[row][18].value,
                     # Опубликовано за предыдущий
                     'gz2': sheet[row][19].value,
                     'pfhd2': sheet[row][21].value,
                     'intmoney2': sheet[row][22].value,
                     'bsmeta2': sheet[row][24].value,
                     'otchetd': sheet[row][25].value,
                     'bof0503121':sheet[row][26].value,
                     'bof0503127':sheet[row][27].value,
                     'bof0503130':sheet[row][28].value,
                     'bof0503721':sheet[row][29].value,
                     'bof0503730':sheet[row][30].value,
                     'bof0503737':sheet[row][31].value
                     })
    return data