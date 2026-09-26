
movie_list = {
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

    status = input("Enter Status:")
    print(f"Status: {status}")    
     
    pass 
    


def view_movies(movie_list):
    
    
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    search = input("Find movie Title ").lower()

    found = False

    for movie in movie_list.values():
        if movie_list["title"].lower() == search:
            print("\n")
            print(f"Title:{movie['title']}")
            print(f"Author:{movie['author']}")
            print(f"Status:{movie['status']}")
            found = True
    
    if not found:
        print("Book was not found.")
    pass


def main():
   while True:
    print("CHOOSE OPTION")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs Unwatched")
    print("4. Find a Movie")
    print("5. Exit")

    choice = int(input("Enter number of your choice:"))
    if choice == 1:
         return add_movie(movie_list)
    elif choice == 2:
         return view_movies(movie_list)
    elif choice == 3:
         return count_watched_unwatched(movie_list)
    elif choice == 4:
         return find_movie(movie_list)
    elif choice == 5:
         break
    else: print("Invalid")

    pass 


main()
