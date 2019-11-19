class PeekIter:
    def __init__(self, data):
        self.iter = iter(data)
        self.peeked_list = []

    def __next__(self):
        if len(self.peeked_list) > 0:
            value = self.peeked_list[0]
            self.peeked_list = self.peeked_list[1:]

            return value
        else:
            return next(self.iter)

    def peek(self, offset=0):
        while not len(self.peeked_list) > offset:  
            self.peeked_list.append(next(self.iter))
        
        return self.peeked_list[offset]

    def __iter__(self):
        return self

def check_integer(data):
    num_chars = [str(i) for i in range(10)]

    for c in data:
        if not c in num_chars:
            return False

    return True


def check_float(data):
    num_chars = [str(i) for i in range(10)]

    count = 0

    for c in data:
        if c == ".":
            if count == 0:
                count += 1
                continue
            else:
                return False
        if not c in num_chars:
            return False

    return True
