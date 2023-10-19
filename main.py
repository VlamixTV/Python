import re

io = open("123.txt", "w")
try:
    spreadsheet = open("new_84.csv", "r", errors="ignore")
    for value in spreadsheet:
        if re.fullmatch("\"\d\d-\d\d-\d\d\d\d\s\d\d:\d\d\t\d\d\t\d\d\d\"\n", value):
            io.write(value)
        else:
            fin = ''
            values = ['\"', '\d', '\d', '-','\d', '\d', '-', '\d', '\d','\d', '\d', '\s', '\d', '\d', ':', '\d', '\d',
                      r'\t', '\d',
                      '\d',  r'\t', '\d', '\d', '\d', '\"', '\n']
            for index in range(len(value)):
                if re.match(values[index],value):
                    fin += values[0]
                else:
                    values.insert(index, '')
                    value = value.removeprefix(value[0])
            io.write(fin)
    spreadsheet.close()
except Exception as ex:
    print(ex)
