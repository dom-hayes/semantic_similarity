import spacy
nlp = spacy.load("en_core_web_md")

# This dict variable will later contain the movies in the txt file
dict_of_movies = {}

def hulk_comparison():
    # This string was provided in the requirements to use to gage the similarity of other movies
    hulk_movie_description = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk in to a shuttle and launch him in to space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold in to slavery and trained as a gladiator.")

    # These variables will be replaced with the score and name of the highest similarity movie during the loop
    highest_similarity_score = 0
    highest_similarity_movie = None

    # Movies are imported from the movies.txt file
    with open("movies.txt", "r") as f:
        movie_file = f.readlines()

        # Loop through the list of movies in the file, remove new line characters and add to dict
        for movie in movie_file:
            movie_description = movie[9:].strip("\n")
            dict_of_movies.update({movie[:7]: movie_description})

    # Loop through each movie and check the similarity score when the description of the movie wis compared with the description of the Hulk movie
    for movie in dict_of_movies.keys():
        movie_description = dict_of_movies[movie]
        movie_similarity_score = nlp(movie_description).similarity(hulk_movie_description)

        # If the similarity score of the new movie is higher than the existing score overwrite the variables with the new highest similarity movie
        if movie_similarity_score > highest_similarity_score:
            highest_similarity_score = movie_similarity_score
            highest_similarity_movie = movie

    return highest_similarity_movie

print("The movie with the highest similarity to Hulk is:")
print(hulk_comparison())