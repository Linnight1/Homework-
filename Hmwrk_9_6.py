from itertools import combinations
def  all_variants(text):
    a = 1
    while a <= len(text):
        yield list(combinations(text, a))
        a += 1


a = all_variants("abc")
for i in a:
    print(i)
