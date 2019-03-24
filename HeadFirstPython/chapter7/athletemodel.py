import pickle
from HeadFirstPython.chapter6.athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
            # temp.pop返回了一个name,dob 而且运算后temp只剩下成绩
            return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('File error:' + str(err))
        return None

# def sanitize(time_string):
#     '''
#     传入中间以“-”“:”符号分隔的成绩，最终清洗数据得到统一以“.”分隔的数据的函数
#     :param time_string:传入的待处理的数据
#     :return: 处理后以下标“.”的数据
#     '''
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#         return (time_string)
#     (mins, secs) = time_string.split(splitter)
#     return (mins + '.' + secs)


def put_to_store(files_list):
    # 创建空运动员字典
    all_athletes = {}
    # 读取文件列表中每一个文件的名称
    for each_file in files_list:
        # 这时候，ath这个变量承载着两个属性
        # 分别是ath.name ath.dob
        # 因为之前删除了数据，ath只表示成绩
        ath = get_coach_data(each_file)
        # 字典的k,v对应关系由ath赋值
        # k--name v--times
        all_athletes[ath.name] = ath
        # 以下两行为检验字典的内容
        # for k, v in all_athletes.items():
        #     print(k, "----", v)
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as  ioerr:
        print('File error(put_and_store):' + str(ioerr))
    # 返回一个字典，其中键为运动员名称，值为成绩
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as  ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return all_athletes


the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)

# 检测用
print(data)
for each_athlete in data:
    print(data[each_athlete].name + '  ' + data[each_athlete].dob)

print('————————————')
data_copy = get_from_store()
# 检测用
# print(data_copy)
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + '  ' + data_copy[each_athlete].dob)
