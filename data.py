# A function to load the 100k dataset.
def loadData(path = '/home/avinash/projects/ml-100k/'):
	fhandle = open(path+'u.item')
	movies = {}
	for line in fhandle:
		(i,t) = line.split('|')[0:2]
		movies[i] = t
	data = {}
	fhandle = open(path+'u.data')
	for line in fhandle:
		(user, i, rating, t) = line.split('\t')
		data.setdefault(user, {})
		data[user][movies[i]] = float(rating)
	return data


# A function to check if the value is in a valid data format
def isFloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False


# A function to load recent datasets. (Here, ml-latest-small and ml-latest )
def loadNewData(path = '/home/avinash/projects/ml-latest-small/'):
	fhandle = open(path+'movies.csv')
	movies = {}
	for line in fhandle:
		(i,t) = line.split(',')[0:2]
		movies[i] = t
	data = {}
	fhandle = open(path+'ratings.csv')
	for line in fhandle:
		(user,i,rating,t) = line.split(',')
		data.setdefault(user, {})
		if isFloat(rating):
			data[user][movies[i]] = float(rating)
		else:
			continue
	return data
