arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def permute(arr):
	if len(arr) == 1:
		return arr[0]

	r = []	
	for i, val in enumerate(arr):
		r = arr
		print r.pop(i)
		print arr
		break
		s = val + permute(arr.pop(i))
		arr.append(s)
	return arr

print permute(arr)