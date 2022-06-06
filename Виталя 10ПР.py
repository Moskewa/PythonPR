def main(table):
    result = []
    for row in table:
        if (row[0] == None):
            continue
        tempRow = []
        # Первая колонна
        firstColumn = row[0][:row[0].find("!")]
        xd=(str(row[0][firstColumn.find(".") + 1:]+" "+firstColumn[:1]+"."+firstColumn[firstColumn.find(".") - 1: firstColumn.find(".") + 1]))
        tempRow.append(xd)
        # Вторая колонна
        tempRow.append(row[0][row[0].find("[at]")])
        # Третья колонна
        tempRow.append(row[1][3:15].replace("(", ")"))
        # Четвёртая колонна
        if (row[4] == "Выполнено" and row[4] == row[3]):
            tempRow.append("да")
        else:
            tempRow.append("нет")
        # Вставка
        # Сортировка возможно здесь будет лучше. Не реализована, сами реализуйте :з
        result.append(tempRow)
    return result
print(main([['Виктор Г. Шичян!viktor53[at]yahoo.com', '(480) 709-86-87', None, None, '70%', '(480) 709-86-87'], ['Святослав З. Медорин!svatoslav86[at]yandex.ru', '(224) 596-14-98', None, None, '67%', '(224) 596-14-98'], ['Даниэль Б. Теговев!daniel_35[at]yahoo.com', '(501) 488-63-35', None, None, '85%', '(501) 488-63-35']]))