def findAndReplace(oldText, text, newText):
    len_oldText = len(oldText)
    len_newText = len(newText)

    text_buffer = ""
    i = 0

    while i < len_oldText:
        if oldText[i : i + len_newText] == text:
            text_buffer += newText
            i += len_newText
        else:
            text_buffer += oldText[i]
            i += 1
    return text_buffer


print(findAndReplace("the dog", "dog", "fox"))

assert findAndReplace("The fox", "fox", "dog") == "The dog"

assert findAndReplace("fox", "fox", "dog") == "dog"

assert findAndReplace("Firefox", "fox", "dog") == "Firedog"

assert findAndReplace("foxfox", "fox", "dog") == "dogdog"

assert findAndReplace("The Fox and fox.", "fox", "dog") == "The Fox and dog."
