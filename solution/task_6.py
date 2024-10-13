def serialize(data: list[dict[str, int | str]], path: str):
    with open(path, 'a',encoding="UTF-8") as f:
        for i in data:
            s = ''
            for j in i:
                s += j + ": " + str(i[j])+", "
            f.write(s[:-2]+"\n")

def deserialize(path: str) -> list[dict[str, int | str]]:
    with open(path,'r',encoding="UTF-8") as f:
        f = f.read().split('\n')
        l = []
    for i in f:
        if i!='':
            scufs = {}
            items = i.split(', ')
            for j in items:
                ne_pridumal = j.split(': ')
                try:
                    ne_pridumal[1] = int(ne_pridumal[1])
                except:
                    pass
                scufs[ne_pridumal[0]] = ne_pridumal[1]
            l.append(scufs)
    return l
print(deserialize('data.txt'))