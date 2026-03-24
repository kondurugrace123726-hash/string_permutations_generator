
def generate_permutations(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]   # swap
            generate_permutations(s, l + 1, r)
            s[l], s[i] = s[i], s[l]   # backtrack


# input
s = list(input().strip())
generate_permutations(s, 0, len(s) - 1)