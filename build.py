import operator


def solution_asc(dic):
    return sorted(dic.items())

def solution_desc(dic):
    return sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
