import pickle
# 用dump保存，用load恢复
with open('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1, 2, 'three'], mysavedata)
with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)
print(a_list)