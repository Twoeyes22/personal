




'''li = [[1,3], [2,4],[3,3],[4,4],[5,5]]

li.sort(key = lambda x : (x[1], -x[0]))
print(li)
'''
'''
li = [1,-3,5,-10]


li.sort(key = lambda x : abs(x), reverse=True)
li.sort(key = lambda x : -abs(x))
'''