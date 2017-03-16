from engines import pearson, euclid, spearman, manhatten, cosine, centered_cosine


# n is how many results you want 
# sim is the similarity function you want to use
# person is the person or movie whose similar one we need to find
# function to find similar user or movie, user - user prediction
def similar(data,person,e,n=5):

	if e == 0:
		sim = euclid
	elif e == 1:
		sim = manhatten
	elif e == 2:
		sim = pearson
	elif e == 3:
		sim = spearman
	elif e == 4:
		sim = cosine

	s = []
	for people in data:
		if people != person:
			s.append((sim(data,person,people),people))
	s.sort()
	s.reverse()
	# Return the best n results
	return s[0:n]


# A function to recommend movies, user - item prediction
# Using weighted averages

def recommend(data,person,e):
	if e == 0:
		sim = euclid
	elif e == 1:
		sim = manhatten
	elif e == 2:
		sim = pearson
	elif e == 3:
		sim = spearman
	elif e == 4:
		sim = cosine
	elif e == 5:
		sim = centered_cosine
	rec_m = {}
	simsum = {}
	for people in data:
		if people != person:
			s = sim(data,person,people)
		if s > 0:
			for movie in data[people]:
				#if movie not in data[person]:
				rec_m.setdefault(movie,0)
				rec_m[movie] += data[people][movie]*s
				simsum.setdefault(movie,0)
				simsum[movie] += s
	ranking = []
		# After normalizing
	for movie in rec_m:
		ranking.append((rec_m[movie]/simsum[movie],movie))
	ranking.sort()
	ranking.reverse()
