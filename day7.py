import re

import xlrd
import xlwt
import numpy as np

file = xlrd.open_workbook(filename=r"百度合作单位-人员管理-二期.xls", encoding_override=True)
table = file.sheet_by_index(0)
row = table.nrows
col = table.ncols
col_v1 = table.col_values(3, 1)
number = len(col_v1)
print("总人数：", number)

dx = 0
yd = 0
lt = 0
phone = table.col_values(5, 1)
for i in range(1, len(phone)):
    hq = phone[i]
    fz1 = re.compile("14")
    fz2 = re.compile("17")
    f1 = fz1.match(hq)
    f2 = fz2.match(hq)
    if f1 != None or f2 != None:
        dx += 1

    fz3 = re.compile("13")
    f3 = fz3.match(hq)
    if f3 != None:
        yd += 1

    fz4 = re.compile("15")
    f4 = fz4.match(hq)
    if f4 != None:
        lt += 1
print("电信用户：", dx, "\n移动的用户：", yd, "\n联通的用户：", lt)

nan = 0
nv = 0
gender = table.col_values(8, 1)
for o in gender:
    if o == "男":
        nan += 1
    else:
        nv += 1
print("公司男士有：", nan, "人")
print("公司女士有：", nv, "人")

veteran = 0
age = table.col_values(7, 1)
for p in age:
    if p > 45:
        veteran += 1
print("年龄超过45岁的老员工人数：", veteran)

three = 0
eight = 0
payroll = table.col_values(11, 1)
for u in payroll:
    if u < 3000:
        three += 1
    elif u > 8000:
        eight += 1
print("薪资低于3000元的人数：", three)
print("薪资高于8000元的人数：", eight)

ma = 0
mass = table.col_values(13, 1)
for y in mass:
    if "传媒" in y:
        ma += 1
print("去传媒公司工作的人员数量：", ma)

danger = 0
aim = table.col_values(9, 1)
for t in aim:
    if "黑龙江" in t or "北京" in t or "福建" in t or "四川" in t:
        danger += 1
print("疫情高危地区人数：", danger)

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("人员管理数据统计")
worksheet.write(0,0,label = "公司总人数")
worksheet.write(1,0,label = number)
worksheet.write(0,1,label = "电信的用户")
worksheet.write(1,1,label = dx)
worksheet.write(0,2,label = "移动的用户")
worksheet.write(1,2,label = yd)
worksheet.write(0,3,label = "联通的用户")
worksheet.write(1,3,label = lt)
worksheet.write(0,4,label = "公司的男士数量")
worksheet.write(1,4,label = nan)
worksheet.write(0,5,label = "公司的女士数量")
worksheet.write(1,5,label = nv)
worksheet.write(0,6,label = "超过45岁的老员工人数")
worksheet.write(1,6,label = veteran)
worksheet.write(0,7,label = "薪资低于3000元的人数")
worksheet.write(1,7,label = three)
worksheet.write(0,8,label = "薪资高于8000元的人数")
worksheet.write(1,8,label = eight)
worksheet.write(0,9,label = "去传媒公司工作的人数")
worksheet.write(1,9,label = ma)
worksheet.write(0,10,label = "高危地区的人数")
worksheet.write(1,10,label = danger)
workbook.save("人员管理数据统计.xls")
print("写入成功！")

