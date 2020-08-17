def _parse(path):
	file = open(path,'r')
	str = file.readlines()
	str = ' '.join(str)
	print(_sort(_deduplicate(str)))
	
def _deduplicate(str):
	unique = []
	arr = str.split()
	for j in arr:
		if j not in unique:
			unique.append(j)
	return unique

def _sort(u):
   y = []
   count=65
   while len(y)<len(u):
   	for i in u:
   		if ord(i[0])==count:
   			y.append(i)
   	count+=1
   return y
path = input("Enter File Path Here : ")
_parse(path)
