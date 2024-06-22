# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(
        "/Users/aaravbansal/Developer/100 Days of Code (Python) /100 Days/Intermediate/Day 24/Mail Merge/Input/Names/"
        "invited_names.txt"
) as file:
    names = file.readlines()

with open(
        "/Users/aaravbansal/Developer/100 Days of Code (Python) /100 Days/Intermediate/Day 24/Mail "
        "Merge/Input/Letters/starting_letter.txt"
) as file:
    template = file.read()

    for name in names:
        final1 = template.replace("[name]", name.strip())

        with open(
                f"/Users/aaravbansal/Developer/100 Days of Code (Python) /100 Days/Intermediate/Day 24/Mail Merge/"
                f"Output/ReadyToSend/{name} letter.txt",
            mode="w"
        ) as outputFile:
            outputFile.write(final1)
