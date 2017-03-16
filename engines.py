import math
# Takes 3 parameters, data, names
def euclid(data,pone,ptwo):
	# Get what items are shared between two people
	shared = {}
	total = 0 
	#print shared
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			# Calculate using Euclid's formula
			total += (data[pone][movie]-data[ptwo][movie])**2

		#print shared

	# If nothing common return 0
	if len(shared) == 0:
		return 0;

	#print shared
	# Return
	return 1/(1+total)

#d = euclidDistance(critics,'Lisa Rose', 'Gene Seymour')
#print d
#-----------------------------------------------------------------------------------------------------------------------
''' Manhatten distance algorithm
	1) Identify the shared objects
	2) Calculate difference between the scores
	3) Sum the scores
	Minimum distance similar the people
	'''
def manhatten(data,pone,ptwo):
	shared = {}
	total = 0
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			total += abs(data[pone][movie] - data[ptwo][movie])

	if len(shared) == 0:
		return 0

	return 1/(1+total)
#-----------------------------------------------------------------------------------------------------------------------

def pearson(data,pone,ptwo):
	shared = {}
	p1sum = p1sq = 0
	p2sum = p2sq = 0
	prodsum = 0
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			p1sum += data[pone][movie]
			p1sq += data[pone][movie]**2
			p2sum += data[ptwo][movie]
			p2sq += data[ptwo][movie]**2
			prodsum += data[pone][movie]*data[ptwo][movie]

	length = len(shared)
	if length == 0:
		return 0

	temp = prodsum - ((p1sum*p2sum)/length)
	value = ((p1sq-(p1sum**2/length))*(p2sq-(p2sum**2/length)))**0.5
	if value == 0:
		return 0
	else:
		return temp/value

#p = pearson(critics,'Lisa Rose', 'Gene Seymour')
#print p
#-----------------------------------------------------------------------------------------------------------------------
# A function to assign ranks and sort
#	the rankings
def spearman_sort(l):
	l = [[k,v] for k,v in l.items()]
	l.sort(key=lambda l:l[1])
	index = 1
	for each in l:
		each[1] = index
		index += 1
	l.sort()
	return l

''' Spearman Correlation algorithm
		1) Find scores of each object
		2) Calculate ranks for each object
		3) Find the difference between ranks,
			to verify - sum of ranks should be 0
		4) Calculate sum of squares of ranks
		5) Calculate Spearman r = 1 - (6*summ(d**2)/n(n**2-1)) '''
def spearman(data,pone,ptwo):
	shared = {}

	# Find scores of each object
	x = {}
	y = {}
	index = 1
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			x[index] = data[pone][movie]
			y[index] = data[ptwo][movie]
			index += 1

	# If no common element return 0
	if len(shared) == 0:
		return 0

	# Calculate ranks for each object
	x = spearman_sort(x)
	y = spearman_sort(y)

	# Find the difference between ranks
	diff = []
	for index in range(0,len(x)):
		diff.append(x[index][1] - y[index][1])

	# Calculate sum of squares of ranks	
	diffs = 0
	for each in diff:
		diffs += each**2

	# Calculate Spearman r = 1 - (6*summ(d**2)/n(n**2-1))
	l = len(shared)
	temp = (6*diffs)/(1+l*((l**2)-1))
	r = 1 - temp
	return r
#-----------------------------------------------------------------------------------------------------------------------
''' Cosine Similarity
	1) Find scores of each object
	2) Calculate ||x|| = sqrt(summ(x))
	3) Calculate ||y|| = sqrt(summ(y))
	4) Dot product x.y = summ(x*y)
	5) Cosine Similarity =  (x.y)/(||x||X||y||)
	'''
def cosine(data,pone,ptwo):
	shared = {}
	dot = 0
	x = 0
	y = 0
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			x += data[pone][movie]**2
			y += data[ptwo][movie]**2
			dot += data[pone][movie]*data[ptwo][movie]

	if len(shared) == 0:
		return 0

	x = x**0.5
	y = y**0.5
	return dot/(x*y)
#-----------------------------------------------------------------------------------------------------------------------
def centered_cosine(lis,p1,p2):
    avg={p1: sum(lis[p1][i] for i in lis[p1])/len(lis[p1])}
    avg.update({p2: sum(lis[p2][i] for i in lis[p2]) / (1+len(lis[p2]))})
    value=dict([(x,dict([(item,lis[x][item]-avg[x]) for item in lis[x]])) for x in avg])
   	nu=0
    for i in value[p1]:
        if i in value[p2]:
            nu=nu+value[p1][i]*value[p2][i]
    x=sum(pow(value[p1][item],2) for item in [i for i in value[p1]])
    y=sum(pow(value[p2][item],2) for item in [i for i in value[p2]])
    return nu/(1+math.sqrt(x*y))