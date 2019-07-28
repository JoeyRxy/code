import myPack.information_theroy as info

X = [0.1, 0.3, 0.6]
P = [
    [0.6, 0.2, 0.2],
    [0.7, 0.1, 0.2],
    [0.4, 0.5, 0.1]
]

t = info.entropy(X, P)
print(t.Y)
print("HX : {}".format(t.HX))
print("HY : {}".format(t.HY))
print("H(X|Y) : {}".format(t.HXgivenY))
