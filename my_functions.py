# if the input is a vertical list of items, one per line
# this will return a list of integers
def getintlist(filename):
    my_list = []
    f = open(filename)

    for line in f:
        my_list.append(int(line.strip()))
    f.close()

    return my_list


def getstring(filename):
    f = open(filename, "r")
    ans = f.read()
    f.close()
    return ans


