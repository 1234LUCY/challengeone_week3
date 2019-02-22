def list_sort(lista):
	

	    even = []
	    odd = []
	    chars = []
	    Dict = dict()
	    if not isinstance(lista, list):
	        return 'Invalid Input'
	

	    if not lista:
	        Dict['evens'] = even
	        Dict['odds'] = odd
	        Dict['chars'] = chars
	        return Dict
	    
	    for x in lista:
	

	        if isinstance(x, int):
	            if x % 2 == 0:
	                even.append(x)
	

	            else:
	                odd.append(x)
	

	        elif isinstance(x, str):
	            chars.append(x)
	

	    Dict['evens'] = sorted(even)
	    Dict['odds'] = sorted(odd)
	    Dict['chars'] = sorted(chars)
	    return Dict
	

	

print(list_sort([2,0,6,5,1,7, 'z', 'a']))



