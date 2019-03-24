# 版本2.0：将字典加入函数中
def sanitize(time_string):
    '''
    传入中间以“-”“:”符号分隔的成绩，最终清洗数据得到统一以“.”分隔的数据的函数
    :param time_string:传入的待处理的数据
    :return: 处理后以下标“.”的数据
    '''
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
            temp = data.strip().split(',')
            return({'Name': temp.pop(0),
                    'dob': temp.pop(0),
                    'grade': str(sorted(set([sanitize(t) for t in temp]))[0:3])})
    except IOError as err:
        print('File error:' + str(err))
        return None


sarah = get_coach_data('sarah2.txt')
# sarah_name, sarah_dob = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
print(sarah)
print(sarah['Name'] + "'s fastest times are: " + sarah['grade'])
