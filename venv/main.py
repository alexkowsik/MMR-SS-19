# Aufgabe 3.1
# this has not had enough testing yet. especially subset function

# def flatten(list):
#     for item in list:
#         if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
#             yield from flatten(item)
#         else:
#             yield item
#         # return list


class Set:
    # using dictionaries to store elements
    # only allowing hashable types(i.e.: no lists)

    # args takes everything you throw in as a parameter and stores it in a tuple
    def __init__(self, *args):
        self.content = {}
        if not args:
            pass
        else:
            for i in args:
                temp_key = self.hashed(i)
                self.content[temp_key] = i

    # standard utility functions:
    def __len__(self):
        return len(self.content)

    def __iter__(self):
        self.keylist = list(self.content.keys())
        self.iterindex = -1
        return self

    def __next__(self):
        self.iterindex += 1
        if len(self.keylist) <= self.iterindex:
            raise StopIteration
        else:
            return self.content[self.keylist[self.iterindex]]

    def __contains__(self, item):
        temp_key = self.hashed(item)
        return self.content.get(temp_key) is not None

    def __getitem__(self, item):
        temp_key = self.hashed(item)
        return self.content.get(temp_key)

    def __str__(self, start=0, stop=None):
        if len(self) == 0:
            return "∅"
        if len(self) == 1 & isinstance(self.content.values(), Set):
            return '{' + str(self.content.values()) + '}'
        # if stop is None:
        #     stop = len(self)
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
        if len(self) == 0 and len(other) == 0:
            return Set()
        elif len(self) == 0:
            return other
        elif len(other) == 0:
            return self
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

    #Aufgabe3.1.2
    def powerset(self):
        result = Set()
        base_set = list(self.content.values())

        for i in range(1, (2**len(self))):
            subsets_to_include = bin(i)[2:]

            for i in range(len(self)-len(subsets_to_include)):
                subsets_to_include = "0" + subsets_to_include

            temp = Set()
            for j in range(len(subsets_to_include)):
                if subsets_to_include[j] == "1":
                    temp = temp + Set(base_set[j])
            result = result + Set(temp)

        return result + Set(Set())

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
        temp_dict = self.content.copy()
        new_set.content = temp_dict
        return new_set

    # helpers
    def hashed(self, obj):      # function that hashes any python object to its memory address(as string)
        return str(id(obj))


# Aufgabe 3.1.2
def neumann_numbers(n, the_set = Set()):
    if len(the_set) < n:
        the_set = the_set + Set(the_set)
        return neumann_numbers(n, the_set)
    else:
        return the_set


def binomialCoefficients(num):
    pass


class RandomObject:
    def __init__(self):
        self.value = "i'm useless."

    def __str__(self):
        return "<useless random object>"


if __name__ == "__main__":
    a = Set(1, 2, 3)
    b = Set(Set())
    print(a.powerset())
    print(b)
    nn = neumann_numbers(7)
    print(nn)
    print(len(nn))
    # print(list(a.content.values()))
    # print(list(iter(a)))
    # print(a.powerset())
