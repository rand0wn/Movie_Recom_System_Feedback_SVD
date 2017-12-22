## REALTIME RECOMMENDATION SYSTEM(Explicit Feedback)

This document contains information about implementaion, working and using this
system.  

### Dataset: I am using MovieLens 1M dataset, which contains data of movies rated by user.  
http://grouplens.org/datasets/movielens/1m/  

I am going to use item based collaborative filtering, in this similarities between  
items(here movies) is determined and then users with similar items are recommended to  
items found most similar to others.  

### Frameworks: python-recsys(for SVD algorithm), numpy, pandas  

### Working:  
Three datasets are imported movies, ratings and users. Since we are using item-item  
based collborative filtering, I am only interested in ratings dataset.  

Ratings(user_id, movie_id, ratings, timestamp)  
I am only interested in the first 3 columns as others are irrelevant.  

### Dataset: Ratings(user_id, movie_id, ratings)  

As this is only item-item based filtering item, user_id and rating is required to run matrix
factorisation(SVD).  

Create matrix where rows are user_id and cols are movie_id and values are ratings in
which we can predict missing values of unrated movies by users.  

Factorisation is done on the matrix and missing ratings are computed and user gets
suggestions on the movies.  

User supplies explicit feedback on some of the unrated movies previously not rated by  
the user, recomputation is called and new suggestions are shown and feedback to show  
more suggestions is appreciated for more recommendations.  
