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
    return


    # TODO: Step 3 - Add another movie to the data structure
    student_info["movies"].append({
        "title": "Core",
        "genre": "Drama, Science Fiction"
    })

    print_student_name_and_id(student_info)

    print_pizza_toppings(student_info)
    

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    about_me["pizza_toppings"] = sorted([topping.lower() for topping in about_me["pizza_toppings"]])
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