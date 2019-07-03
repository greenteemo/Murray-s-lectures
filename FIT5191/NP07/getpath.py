net = { 
	'x':['u','v','w','y'],
	'y':['x','w','z'],
	'z':['y','w'],
	'u':['w','x','v'],
	'v':['u','w','x'],
	'w':['u','v','x','y','z']
}

def dfs(path, dest):
	if(path[-1] == dest):
		print(path)
		return
	for node in net[path[-1]]:
		if(node not in path):
			dfs(path+node, dest)

path = input("start node:")
dest = input("end node:")
dfs(path, dest)
