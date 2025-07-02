# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", 
                         "maggie": "(Pacifier Suck)"
                         }
for key in simpson_catch_phrases:
    if ['lisa', 'bart', 'marge'] == key:
        print(simpson_catch_phrases[key])

print(simpson_catch_phrases['lisa']) 
print(simpson_catch_phrases['bart'])
print(simpson_catch_phrases['homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

