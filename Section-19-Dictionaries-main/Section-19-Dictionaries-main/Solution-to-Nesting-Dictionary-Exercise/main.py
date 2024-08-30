import pprint
programming_language = [
    {"user_name" : "Kayn",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10 
    },
    {"user_name":"Dhea",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]

def add_new_user(p_user_name, p_favorite_languages, p_experience):
    new_user = {}
    new_user["user_name"] = p_user_name
    new_user["favorite_languages"] = p_favorite_languages
    new_user["experience"] = p_experience
    programming_language.append(new_user)
    pprint.pprint(programming_language)

add_new_user("Chisee", ["Java", "Kotlin", "Swift"], 10)