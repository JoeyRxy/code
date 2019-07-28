# %%
from myPack.information_theroy import entropy


def H(*arg):
    return entropy.H(arg)


# %%
H(0.625, 0.125, 0.25)-H(0.75, 1/8, 1/8)

# %%
H(0.8, 0.2)

# %%
