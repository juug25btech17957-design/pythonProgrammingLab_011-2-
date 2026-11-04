def process_marks(marks):
    # Keep marks >= 40 in a NEW list (the original is never modified)
    valid = [mark for mark in marks if mark >= 40]
    # set() removes duplicates, sorted() gives ascending order
    unique_marks = sorted(set(valid))
    qualified = [mark for mark in unique_marks if mark >= 60]
    # Last three of an ascending list = three highest (or all if fewer)
    top_three = qualified[-3:]
    return unique_marks, qualified, top_three


datasets = [
    [35, 60, 45, 80, 35, 55, 60, 95, 40, 80],   # given data
    [40, 59, 60, 70, 39, 70],                   # fewer than three qualify
    [30, 30, 50, 55, 59],                       # none qualify
    [60, 65, 70, 75, 80, 80],                   # more than three qualify
]
for marks in datasets:
    unique_marks, qualified, top_three = process_marks(marks)
    print("Marks:", marks)
    print("Processed marks:", unique_marks)
    print("Qualified marks:", qualified)
    print("Top three:", top_three)
    print()
