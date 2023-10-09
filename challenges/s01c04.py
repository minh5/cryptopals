import os

from s01c03 import decipher

def decipher_text():
    """
    Brute force method - I care more about comprehension of the materials
    than the efficiency.

    We iterate through the lines of the text and test each for the single character
    keys and return the top 5. After that we flatten the top five into a main
    list containing the line number, single character key, plaintext, and their score
    and display the top five out of all permuatations
    """
    # retrieve the file
    file_path = os.path.join(
        os.path.expanduser("~"), "cryptopals", "assets", "s01c04.txt"
    )
    results = []
    with open(file_path, "r") as fd:
        full_texts = fd.read().split()

    # this can parallelize using concurrent
    for i, text in enumerate(full_texts):
        decoded = bytes.fromhex(text)
        top_five = decipher(decoded)
        for item in top_five:
            to_append = [i]
            to_append.extend(item)
            results.append(to_append)

    # sort the main list
    results.sort(key=lambda x: x[3], reverse=True)
    return results[:5]

