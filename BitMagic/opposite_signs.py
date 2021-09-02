def oppositeSigns(x, y):

    return (x^y) >> 31


x, y = 100, -11
if oppositeSigns(x, y):
    print("Signs are opposite")
else:
    print("Signs are not opposite")