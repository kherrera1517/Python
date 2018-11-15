class HuffmanTree(object):
    def __init__(self, symbol=None, left=None, right=None, freq=None): 
        self.symbol = symbol
        self.left = left
        self.right = right
        self.freq = freq

    def read_dict(self, d):
        if d == {}:
            return
        left_dict, right_dict = {}, {}

        # for key in d:
        #     if key != '0' and key != '1':
        #         if key[0] == '0':
        #             left_dict[key[1:]] = d[key]
        #         else:
        #             right_dict[key[1:]] = d[key]

        if '0' in d:
            self.left = HuffmanTree(symbol = d['0'])
        else:
            self.left = HuffmanTree()
            list_of_0 = list(filter(lambda key: key[0] == '0', d.keys()))
            for key in list_of_0:
                left_dict[key[1:]] = d[key]
            self.left.read_dict(left_dict)

        if '1' in d:
            self.right = HuffmanTree(symbol = d['1'])
        else:
            self.right = HuffmanTree()
            list_of_1 = list(filter(lambda key: key[0] == '1', d.keys()))
            for key in list_of_1:
                right_dict[key[1:]] = d[key]
            self.right.read_dict(right_dict)

    def find_char(self, code):
        if self.left is None and self.right is None:
            return (self.symbol, 0)
        elif code[0] == '0':
            symbol, count = self.left.find_char(code[1:])
        else:
            symbol, count = self.right.find_char(code[1:])
        
        return (symbol, count + 1)

    def __add__(self, other): 
        return HuffmanTree(left = self, right = other, freq = self.freq + other.freq )

    def __lt__(self, other): 
        return self.freq < other.freq

    def __repr__(self):
        if self.symbol is None: 
            return "(" + self.left.__repr__() + ", " + self.right.__repr__() + ")"
        else: 
            return self.symbol
    
    def get_codes(self, prefix = ""):
        if self.left is None and self.right is None:
            return [(self.symbol, prefix)]
        else:
            left_sublist = self.left.get_codes(prefix=(prefix+'0'))
            right_sublist = self.right.get_codes(prefix=(prefix+'1'))
        return left_sublist + right_sublist