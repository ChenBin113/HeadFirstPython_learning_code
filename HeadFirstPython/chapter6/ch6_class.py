class Athlete(object):
    def __init__(self, a_name, a_dob=None, a_time=[]):
        self.name = a_name
        self.dob = a_dob
        self.time = a_time

    def top3(self):
        # 计算前三的成绩
        return sorted(set([sanitize(t) for t in self.time]))[0:3]

    def add_time(self, extra_number=None):
        # 增加一个成绩
        # 用None标识是否调用
        # return(self.time.append(extra_number))
        self.time.append(extra_number)

    def add_times(self, extra_list):
        # 以列表的形式增加一些成绩
        # return self.time.append(extra_list)
        self.time.extend(extra_list)


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
            return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('File error:' + str(err))
        return(None)


sarah = get_coach_data('sarah2.txt')
# print(sarah)
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

vera = Athlete('vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['1.21', '1-22', '1:23'])

print(vera.time)
print(vera.top3())
