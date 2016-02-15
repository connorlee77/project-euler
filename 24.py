arr = '0123456789'

def permute(s, arr):
    if len(s) == 10:
        print s
        return
	    
    for i in arr:
    	if i not in s:
    		permute(s + i, arr)

    return

permute('', arr)

#python 24.py | head -1000000