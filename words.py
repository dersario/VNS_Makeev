def play(words: list[str]) -> list[int]:
    i = 0
    j = i+1
    errors = []
    while j < len(words):
        if words[i][-1] != words[j][0] or words[:j+1].count(words[j])>1:
            errors.append(j+1)
            j+=1
        else:
            i=j
            j+=1
    return errors
