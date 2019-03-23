# {'lines': 172, 'words': 2145, 'characters': 11227}
def statistics(file):
    with open(file) as f :
        stats = f.read()

    lines = stats.split("\n")
    lines = len(lines)

    words= stats.split()
    words = len(words)

    char_text = len(stats)

    return {"lines" : lines,"words" : words, "characters" : char_text}

print(statistics("story.txt"))
