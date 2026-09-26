
Movie = {
    "Movie1": {
        "title": "Inception",
        "author": "Christopher Nolan",
        "status": "Watched"
    },

     "Movie2": {
        "title": "Dunkirk",
        "author": "Christopher Nolan",
        "status": "unwatched"
    },

     "Movie2": {
        "title": "",
        "author": "Christopher Nolan",
        "status": "Watched"
    },
    
    
}


  def display_menu():
    print("CHOOSE OPTION")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs Unwatched")
    print("4. Find a Movie")
    print("5. Exit")


    pass


def add_movie(movie_list):
    title = input("Enter Title:")
    print(f"Title: {title}")

    author = input("Enter Author:")
    print(f"Author: {author}")
  
    pass


def view_movies(movie_list):
    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()

display_menu()
 if 