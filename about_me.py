"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'fullname': 'Amnish Kaur'
        
        'studentid': 10297018
        
        'toppings':['onions', 'tomatoes', 'green pepper'],
        
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'Sanam Teri Kasam',
                'genre': 'romantic'
            },
            # TODO: Add one more movie
            {
                'title':'Golmaal'
                'genre':'comedy'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['soylent green', 'racht'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'the lord of the rings', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    print("My name is{my_info['fullname']},but most of the people do not know hoe to prounce {my_info['fullname'.split()[0]].}")
    print(f"My student ID is {my_info['studentid']}.")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print("My favorite pizza toppings are.")
    # Print bullet list of favourite pizza toppings
    print(f"-{'toppings'}")

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    my_info['toppings'].extend(toppings)
    my_info['toppings'] = [toppings.lower()as toppings in my_info['toppings']]
    my_info['toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    movie = {'title': "tiger", 'genre': "action.lower"()}
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    genres = [movie['action'] as movie in my_info['movies']]
    list_of_genres = ','.join(genres)
    print(f"I love to watch [list_of_genre] movies in my free time.")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    titles = [movie["title"] for movie in movie_list]
    title_list = ','.join(titles)
    print(f"Most of the favourite movies of min are in {title_list}.")

if __name__ == '__main__':
    main()