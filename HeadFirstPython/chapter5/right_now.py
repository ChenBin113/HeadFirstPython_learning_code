def sanitize(time_string):
    # 传入中间以“-”“:”符号分隔的成绩，最终清洗数据得到统一以“.”分隔的数据的函数
    # :param time_string:传入的待处理的数据
    # :return: 处理后以下标“.”的数据
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as err:
        print('File error:' + str(err))
        return None


print('————read from the file————')

#  常规读取数据1.0
# with open('julie.txt') as julie_scores:
#     data = julie_scores.readline()
#     julie = data.strip().split(',')
# with open('mikey.txt') as mikey_scores:
#     data = mikey_scores.readline()
#     mikey = data.strip().split(',')
# with open('sarah.txt') as sarah_scores:
#     data = sarah_scores.readline()
#     sarah = data.strip().split(',')

# 定义函数读取数据2.0
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# 测试读取功能是否正常
print(james)
print(julie)
print(mikey)
print(sarah)

print('————clean the data————')
clean_james = []
for i in james:
    clean_james.append(sanitize(i))
print(clean_james)
clean_julie = []
for i in julie:
    clean_julie.append(sanitize(i))
print(clean_julie)
clean_mikey = []
for i in mikey:
    clean_mikey.append(sanitize(i))
print(clean_mikey)
clean_sarah = []
for i in sarah:
    clean_sarah.append(sanitize(i))
print(clean_sarah)

print('————sort————')
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))


# print('————reverse————')
# print(sorted(clean_james, reverse=True))

print('————list comprehension(function test)————')
sort_clean_james = sorted([sanitize(i) for i in james])
print(sort_clean_james)
unique_james = []
for each_james in sort_clean_james:
    if each_james not in unique_james:
        unique_james.append(each_james)
print(unique_james[0:3])

# set工厂函数去除重复项，排序，选取前三项
print('————sort, clean, chooese————')
print(sorted(set(clean_james))[0:3])
print(sorted(set(clean_julie))[0:3])
print(sorted(set(clean_mikey))[0:3])
print(sorted(set(clean_sarah))[0:3])