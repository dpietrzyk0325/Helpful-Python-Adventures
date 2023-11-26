# obsidian_note-taking_school_slides.py

# Description: This script is used to create a template for the note-taking process in Obsidian.
# The template is used to create the markdown headings for current note selected in Obsidian.

# this is a very simple script but it has saved me a lot of time

# this can be expanded to create any template you want for your notes (I just stick to the same template for all my notes)

import pyautogui
import time

def create_note_template(num_slides):
    template = ""
    for slide_num in range(1, num_slides + 1):
        template += f"#### Slide {slide_num}\n"
        template += "##### Level 1\n"
        template += "###### Level 2\n"
    
    return template

num_slides = int(input("How many 'Slide' headings do you want to create? "))
if num_slides < 1:
    print("Please enter a valid number greater than or equal to 1.")
else:
    result = create_note_template(num_slides)
    time.sleep(5)  # Give you 5 seconds to focus on the input area
    pyautogui.write(result) # I should probably slow this process down a bit so it doesn't type so fast (because it rarely messes up, but when it does, it's annoying)