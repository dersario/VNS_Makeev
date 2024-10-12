def pull(n: int) -> tuple[int, int]:
    legendary = n//90
    if n>=90:
        n-=1
    epic = n//10
    return epic, legendary
i = int(input("Введите количество круток: "))
while i!=-1:
    print(pull(i))
    i = int(input("Введите количество круток: "))