#1. ['x','xx','xxx','xxxx','y','yy','yyy','yyyy','z','zz','zzz','zzzz']
inp = ['x','y','z']
res = [item*rep for item in inp for rep in range(1,5)]
print(res)
print('\n')

#2. ['x','y','z','xx','yy','zz','xxx','yyy','zzz','xxxx','yyyy','zzzz']
inp = ['x','y','z']
res = [item*rep for rep in range(1,5) for item in inp]
print(res)
print('\n')

#3. [[2],[3],[4],[3],[4],[5],[4],[5],[6]] 
inp = [2,3,4]
res = [[item+add] for item in inp for add in range(0,3)]
print(res)
print('\n')

#[[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
inp = [2,3,4,5]
res = [[item+add for add in range(0,4)] for item in inp]
print(res)
print('\n')

#[(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3)]
inp = [1,2,3]
res = [(a,b) for b in inp for a in inp]
print(res)

