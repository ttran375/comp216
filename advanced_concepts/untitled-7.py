text_list = [
    ["You've", "gotta", "ask", "yourself", "a", "question"],
    ["do", "I", "feel", "lucky?", "...well"],
    ["do", "ya", "punk?"],
]

text_flat = [word for sublist in text_list for word in sublist]
print(text_flat)

quest_mark_word = []

for pharse in text_flat:
    if "?" in pharse != -1:
        quest_mark_word.append(pharse)

print(quest_mark_word)


def quest_mark_finder(pharse):
    if pharse.find("?") != -1:
        return True
    else:
        return False


output = list(
    filter(quest_mark_finder, [word for sublist in text_list for word in sublist])
)
print(output)
