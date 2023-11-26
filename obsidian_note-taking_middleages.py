# obsidian_note-taking_middleages.py

# Description: This script is used to create a template for the note-taking process in Obsidian.
# The template is used to create the markdown headings for current note selected in Obsidian.

# this is a very simple script but it has saved me a lot of time

# this can be expanded to create any template you want for your notes (I just stick to the same template for all my notes)

import pyautogui
import time

def create_note_template(num_headings):
    template = ""
    for num_headings in range(1, num_headings + 1):
        template += f"#### Learning Through Acting {num_headings}\n" # Change this line to the subsection you want to create
        template += "##### Level 1\n"
        template += "###### Level 2\n"
    
    return template

num_headings = int(input("How many 'heading' headings do you want to create? "))
if num_headings < 1:
    print("Please enter a valid number greater than or equal to 1.")
else:
    result = create_note_template(num_headings)
    time.sleep(5)  # Give you 5 seconds to focus on the input area
    pyautogui.write(result) # I should probably slow this process down a bit so it doesn't type so fast (because it rarely messes up, but when it does, it's annoying)