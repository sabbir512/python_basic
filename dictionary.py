words = set()  # Use set instead of dict

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    try:
        file = open(dictionary, "r")
    except FileNotFoundError:
        return False

    for line in file:
        word = line.rstrip()
        words.add(word)
    
    file.close()  # Close the file after the loop
    return True

def size():
    return len(words)

def unload():
    return True
