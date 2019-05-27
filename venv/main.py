from collections.abc import Iterable


# Aufgabe 3.1
# this has not had enough testing yet. especially subset function
def flatten(list):
    for item in list:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item
        # return list


class Set:
    # using dictionaries to store elements
    # only allowing hashable types(i.e.: no lists)

    # args takes everything you throw in as a parameter and stores it in a tuple
    def __init__(self, *args):
        self.content = {}
        if len(args) == 0:
            pass
        else:
            # args = list(flatten(args))
            for i in args:
                temp_key = self.hashed(i)
                self.content[temp_key] = i

    def __len__(self):
        return len(self.content)

    def __str__(self, start=0, stop=None):
        if len(self) == 0:
            return "∅"
        if stop is None:
            stop = len(self)
        text = '{'
        for i in self:
            temp_key = self.hashed(i)
            text += str(self.content.get(temp_key)) + ', '
        text = text[0:len(text) - 2]
        text += '}'
        return text

    def __iter__(self):
        return iter(self.content)

    def __add__(self, other):
        return Set([self.content, other.content])

    def __sub__(self, other):
        # computes self / other
        temp = self.content.copy()
        for i in other:
            if temp.get(i) is not None:
                temp.pop(i)
        return Set(temp)

    def __contains__(self, item):
        temp_key = self.hashed(item)
        return self.content.get(temp_key) is not None

    def __getitem__(self, item):
        temp_key = self.hashed(item)
        return self.content.get(temp_key)

    def subset(self, selection):
        # selection is a function mapping the domain of the set to {True, False}
        temp = []
        for i in self:
            if selection(i):
                temp.append(i)
        return Set(temp)

    def hashed(self, object):
        return str(id(object))

class RandomObject:
    def __init__(self):
        self.value = "i'm useless."

    def __str__(self):
        return "<useless random object>"


if __name__ == "__main__":
    ro = RandomObject()
    a = Set(2, [5], {1, 2, 3}, 'c', "string", ro, [23, 2, [0], []], 3)
    print(a)
    # b = Set(1, 2, 99)
    # print(b)
    # c = a - b
    # print(c)
    # print(Set(a, b, c))
    # print(a.subset(lambda x: x < 4))
    # print(a.__contains__(5))
    # print(a.__getitem__(5))