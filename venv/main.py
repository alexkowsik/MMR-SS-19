# Aufgabe 3.1
# this has not had enough testing yet. especially subset function

# def flatten(list):
#     for item in list:
#         if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
#             yield from flatten(item)
#         else:
#             yield item
#         # return list


class IteratorShell:    # use for Set class only!!! this is NOT a generic wrapper!!!
    def __init__(self, set):
        self.set = set
        self.shadowiterator = iter(set.content)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.currentindex = self.shadowiterator.__next__()
        except StopIteration:
            raise StopIteration
        self.currentitem = self.set.content[self.currentindex]
        return self.currentitem


class Set:
    # using dictionaries to store elements
    # args takes any python object as parameter and stores it in the dictionary
    def __init__(self, *args):
        self.content = {}
        if len(args) == 0:
            pass
        else:
            # args = list(flatten(args))
            for i in args:
                temp_key = self.hashed(i)
                self.content[temp_key] = i

    # standard utility functions:
    def __len__(self):
        return len(self.content)

    def __iter__(self):         # BEWARE: this function returns values, not keys! be careful with for x in set!!!
        iterator = IteratorShell(self)
        return iter(iterator)

    def __contains__(self, item):
        temp_key = self.hashed(item)
        return self.content.get(temp_key) is not None

    def __getitem__(self, item):
        temp_key = self.hashed(item)
        return self.content.get(temp_key)

    def __str__(self, start=0, stop=None):
        if len(self) == 0:
            return "∅"
        if stop is None:
            stop = len(self)
        text = '{'
        for i in self:
            text += str(i) + ', '
        text = text[0:len(text) - 2]
        text += '}'
        return text

    # set operations
    def intersect(self, other):
        temp_set = Set()
        for element in self:
            if other.__contains__(element):
                temp_set.additem(element)
        return temp_set

    def merge(self, other):
        temp_set1 = self.intersect(other)
        temp_set2 = self.copy()
        for element in other:
            if element in temp_set1:
                pass
            else:
                temp_set2.additem(element)
        return temp_set2

    def complementWithRespectTo(self, other):        # computes self / other
        new_set = self.copy()
        for i in other:
            if new_set.__contains__(i):
                new_set.removeitem(i)
        return new_set

    def __add__(self, other):
        return self.merge(other)

    def __sub__(self, other):
        return self.complementWithRespectTo(other)

    def subset(self, selection):
        # selection is a function mapping the domain of the set to {True, False} BEWARE: domain is every possible python object!
        new_set = Set()
        for i in self:
            if selection(i):
                new_set.additem(i)
        return new_set

    # internal set operations
    def additem(self, item):
        temp_key = self.hashed(item)
        self.content[temp_key] = item

    def removeitem(self, item):
        if not self.__contains__(item):
            pass
        else:
            temp_dict = self.content
            del temp_dict[self.hashed(item)]
            self.content = temp_dict

    def copy(self):
        new_set = Set()
        temp_dict = self.content
        new_set.content = temp_dict
        return new_set

    # helpers
    def hashed(self, obj):      # function that hashes any python object to its memory address(as string)
        return str(id(obj))


class RandomObject:         # dummy class to show that all python objects are accepted in Set(such pc, much wow)
    def __init__(self):
        self.value = "i'm useless."

    def __str__(self):
        return "<random object>"

    def do_something(self):
        print("<random object> sais: '" + self.value + "'")


if __name__ == "__main__":
    ro = RandomObject()
    a = Set(2, [5], {1, 2, 3}, 'c', "string", ro, [23, 2, [0], []], 3)
    for each in a:
        print(each)
    print(a)
    b = Set(1, 2, 99)
    print(b)
    c = a + b
    print(c)
    # print(a.subset(lambda x: x < 4))
    a.additem(5)
    print(a.__contains__(5))
    print(a.__getitem__(5))