#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/7 :    Below you'll find a list which contains the relevant data about a selection of movies. Each item in the list is a tuple containing a movie name and movie budget in that order:

movies = [
 ("Eternal Sunshine of the Spotless Mind", 20000000),
 ("Memento", 9000000),
 ("Requiem for a Dream", 4500000),
 ("Pirates of the Caribbean: On Stranger Tides", 379000000),
 ("Avengers: Age of Ultron", 365000000),
 ("Avengers: Endgame", 356000000),
 ("Incredibles 2", 200000000)]

# Calculate the average budget of all movies in the data set
def calculate_average_budget (movies):
    total_budget = 0
    for movie in movies:
        total_budget += movie[1]
    return total_budget / len(movies)

# Print out how many movies spent more than the average you calculated.
def movies_spent (movies):
    average_budget = calculate_average_budget(movies)
    count=0
    for movie in movies:
        if movie[1] > average_budget:
            count += 1   
    return f"Number of movies with budget above average: {count}"

# Create a function to print all movie names
def movie_names (movies):
    for movie in movies:
        print(movie[0])

# implementation
print("---> The movies names :")
movie_names (movies)
average_budget = calculate_average_budget(movies)
print()
print(f"---> Average budget: {average_budget}")
print()
print(f"---> The number of movies spent more than the average: {movies_spent(movies)}")


