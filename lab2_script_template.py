def main():
    # TODO: Step 2 - Create a complex data structure

    student_info = {
        "full_name": "Rishikumar Vijaykumar Patel",
        "student_id": 10330771,
        "pizza_toppings": ["CHICKEN", "MUSHROOMS", "OLIVES"],
        "movies": [
            {
                "title": "Interstellar",
                "genre": "science fiction"
            },
            {
                "title": "3 Idiots",
                "genre": "Comedy"
            }
        ]
    }



    # TODO: Step 3 - Add another movie to the data structure
    student_info["movies"].append({
        "title": "Core",
        "genre": "Drama, Science Fiction"
    })

    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()