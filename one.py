# Testing the sample string "google.com"
test_string = "google.com"

character_frequency = {}
for i in test_string:
    if i in character_frequency:
        character_frequency[i] += 1
    else:
        character_frequency[i] = 1

print("CHARACTERS IN THE GIVEN STRING:\n" + str(character_frequency))

