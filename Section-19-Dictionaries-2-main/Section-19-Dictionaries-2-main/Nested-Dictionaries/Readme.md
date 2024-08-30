# Nesting list inside dictionary
programming_language = {
    "Kayn" : ["Python", "Java", "C#"],
    "Dhea" : "Scratch",
    "Chisee" : "Java",
}

# Nesting dictionary inside dictionary
programming_language = {
    "Kayn" : { "favorite_languages" : ["Python", "Java", "C#"],
                 "experience": 10 
              },
    "Dhea" : { "favorite_languages" : ["Scratch","Python"],
                "experience" : 2
              },
}

# Nesting dictionary inside list
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
