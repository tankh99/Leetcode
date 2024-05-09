import numpy as np

conditions = [
    [True, False, False],
    [True, False, False],
    [False, True, True]
]

categories = ["A", "B", "C"]

test = np.select(conditions, categories)
print(test)