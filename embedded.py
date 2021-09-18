def use(x, y, size):
    # here some code to make a signal to mechanism and get an answer
    # we will just random answers because we have no embedded code here

    import random
    res = random.randint(1,100)

    if res <= 5:
        return -1
    elif res > 95:
        return 0
    return size

def read_tsv(name):
    file = open(name)
    import csv
    tsv_reader = csv.reader(file, delimiter = '\t')
    headers = next(tsv_reader)
    tsv_dict = [dict(zip(headers, row)) for row in tsv_reader if row and len(row) > 0]
    file.close()
    return tsv_dict

