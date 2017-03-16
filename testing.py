from recommend import similar, recommend, transform_data
from data import loadData, loadNewData, critics	
from engines import euclid, spearman, manhatten, pearson, cosine
import itertools
import time

#dataset = critics
dataset = loadNewData() 

# A function to spilt the data to training and test sets
def splitDict(d):
    n = int(len(d) * 0.85)         
    i = d.iteritems()
    d1 = dict(itertools.islice(i, n))  
    d2 = dict(i)                        
    return d1, d2

training, test = splitDict(dataset)


# A function to calculate MAE
def mae(ordered, test):
	isum = 0
	tot_sum = 0
	num = 0
	tot_num = 0
	for each in ordered:
		tot_num += 1
		for movie in ordered[each]:
			if movie in test[each]:
				num += 1
				error = test[each][movie] - ordered[each][movie]
				if error < 0:
					error = 0 - error
				isum = isum + error
		tot_sum += isum/num
		num = 0
		isum = 0
	return tot_sum/tot_num

# A function to calculate RMSE
def rmse(ordered, test):
	isum = 0
	tot_sum = 0
	num = 0
	tot_num = 0
	for each in ordered:
		tot_num += 1
		for movie in ordered[each]:
			if movie in test[each]:
				num += 1
				error = (test[each][movie] - ordered[each][movie])**2
				isum = isum + error
		tot_sum += (isum)**0.5/num
		num = 0
		isum = 0
	return tot_sum/tot_num

# A driver function to calculate the time taken for each recommendation and also the 
# error in each calculation
def driver(n):
	predicted = {}

	start = time.clock()
	for each in test:
		predicted[each] = recommend(dataset, each, n)
	end = time.clock()

	print end - start
	ordered = {}
	for each in predicted:
		ordered.setdefault(each,{})
		for movie in predicted[each]:
			ordered[each][movie[1]] = movie[0]
	mae_error = mae(ordered, test)
	print mae_error
	rmse_error = rmse(ordered, test)
	print rmse_error

# A program to calculate individual prediction
def new_p(n):
	predicted = {}
	each = '479'
	predicted[each] = recommend(dataset, each, n)
	ordered = {}
	for each in predicted:
		ordered.setdefault(each,{})
		for movie in predicted[each]:
			ordered[each][movie[1]] = movie[0]
	print ordered[each]['Harry Potter and the Deathly Hallows: Part 2 (2011)']
	print test[each]['Harry Potter and the Deathly Hallows: Part 2 (2011)']
