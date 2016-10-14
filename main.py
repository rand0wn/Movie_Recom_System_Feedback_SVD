import numpy as ny
import pandas as pn
import recsys.algorithm
recsys.algorithm.VERBOSE = True
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data


#Operation on Dataset

#Import
#Users
df_users = pn.read_csv('./ds/users.dat', sep="::", names=['user_id', 'gender', 'movie_id', 'rated', 'timestamp'], engine='python')
#Ratings
df_ratings = pn.read_csv('./ds/ratings.dat', sep='::', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')
#Movies
df_movies = pn.read_csv('./ds/movies.dat', sep='::', names=['movie_id', 'movie_name', 'tags'], engine='python')

#Deleting irrelevant col's
df_movies = df_movies.drop('tags', 1)
df_users = df_users.drop('timestamp', 1)
df_users = df_users.drop('gender', 1)
df_ratings = df_ratings.drop('timestamp', 1)

#Add new User for prediction2
def addNewUser(ratings, user_id=df_ratings.tail(1).iloc[0]['user_id'] + 1):
	for i in range(0, len(ratings)):
		row = [user_id, ratings[i][0], ratings[i][1]] #Add new user(user_id, movie_id, ratings)
		df_ratings.loc[len(df_ratings)] = row
		df_ratings.to_csv('ratings.dat', sep=':', index=False, mode = 'w', header=False)
	return user_id		 

#recompute after adding new user or updating feedback(explicit) from user(train data and predict results)
def reCompute(user_id):
	data = Data()
	fname = 'ratings.dat'
	dataset = Data()
	format = {'col':0, 'row':1, 'value':2, 'ids': 'int'}
	dataset.load(fname, sep=':', format=format)
	
	svd = SVD()
	svd.set_data(dataset)

	k = 100
	svd.compute(k=k, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True)

    #New ID of Added User
	USERID = user_id

	a = svd.recommend(USERID, is_row=False)
	for j in range(1, len(a)):
		global a
		k = a[j][0]
		print df_movies.query('movie_id==@k')

		
#Take feedback and input from user(new user)
arr = []
first = 0
def reInput():
	global arr
	global first
	for i in range(0, 20):
		x, y = raw_input("Enter Movie followed by Ratings(-1, -1 to quit(min 10 first time)) : ").split()
		x, y = [int(x), int(y)]
		if first == 0:	
			if x == -1 or y == -1 and i >= 10:
				first = 1
				break
			else:
				arr.append([x,y])
		else:
			if x == -1 or y == -1:
				break
			else:
				arr.append([x,y])
	reCompute(addNewUser(arr))				

		
#New user Movies, Ratings
#user_id = df_ratings.tail(1).iloc[0]['user_id'] + 1
#addNewUser([[318, 5],[858,5],[1221,5], [1, 4], [44, 3], [1203, 3], [1207, 4], [1219, 3], [2643, 4], [2379, 3], [2381, 3]], user_id)

#Input new user and feedback from user and predict movies he likes
while(1):
	reInput()