import xlsxwriter

def haha(class_name, week, lession, location):
    if week == "一":
        row = "B"
    elif week == "二":
        row = "C"
    elif week == "三":
        row = "D"
    elif week == "四":
        row = "E"
    elif week == "五":
        row = "F"
    else:
        row = "G"
    for i in range(len(lession)):
        worksheet1.write(f'{row}{int(lession[i])+1}', f"{class_name} {location}")


# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('./my_courses.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet1 = workbook.add_worksheet("Jodie")
 
# Use the worksheet object to write
# data via the write() method.
worksheet1.write('B1', "一")
worksheet1.write('C1', "二")
worksheet1.write('D1', "三")
worksheet1.write('E1', "四")
worksheet1.write('F1', "五")
worksheet1.write('G1', "六")

worksheet1.write('A2', 1)
worksheet1.write('A3', 2)
worksheet1.write('A4', 3)
worksheet1.write('A5', 4)
worksheet1.write('A6', 5)
worksheet1.write('A7', 6)
worksheet1.write('A8', 7)
worksheet1.write('A9', 8)
worksheet1.write('A10', 9)
worksheet1.write('A11', 10)
worksheet1.write('A12', 11)
worksheet1.write('A13', 12)
worksheet1.write('A14', 13)
worksheet1.write('A15', 14)

file1 = open('./my_courses.txt', 'r')
ls = []
for line in file1:
    line = line.replace('\n', '')
    line = line.split('.')
    ls.append(line)
    # print(line)
    class_name = line[0]
    for i in range(1, len(line)):
        temp = line[i].split(" /")
        week = temp[0]
        lession = temp[1]
        lession = lession.split(",")
        location = temp[2]
        haha(class_name, week, lession, location)

file1.close()

worksheet2 = workbook.add_worksheet("Jodie2")

worksheet2.write('A1', "開課序號")
worksheet2.write('B1', "課目名稱")
worksheet2.write('C1', "授課老師")
worksheet2.write('D1', "年級")
worksheet2.write('E1', "必選修")
worksheet2.write('F1', "學分")
worksheet2.write('G1', "上課時間/地點")



workbook.close()