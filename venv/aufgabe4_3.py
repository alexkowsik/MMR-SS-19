class Parser:
    def __init__(self):
        self.operators = []     # TODO: operatorenliste

    def parse(self, string):
        tokens = string.split()
        for element in tokens:
            try:
                float(element)
            except ValueError:
                for pair in self.operators:
                    if element == pair[0]:
                        valid_operator = True
                if valid_operator:
                    continue
                else:
                    print("invalid operator: '" + element + "'")
                    return -1
        self.rec_parser(tokens)


    def rec_parser(self, list):
        if not list:
            print("empty string cannot be parsed")
            return -1
        elif len(list) == 1:
            if isinstance(list[0], float):
                return list[0]
            else:
                print("invalid operand: '" + list[0] + "'")
        else:
            head = list.pop(0)
            if isinstance(head, float):
                second_operand = self.rec_parser(list)
                return tuple([head, second_operand])
            else:
                for pair in self.operators:
                    if head == pair[0]:
                        return pair[1](self.rec_parser(list))


if __name__ == '__main__':
    pars = Parser
    string = input()
    pars.parse(string)
