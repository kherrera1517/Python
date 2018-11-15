import binary
from collections import Counter

from huffman import HuffmanTree
from binary import EightBitNumToBinary

class HuffmanDecoder(object):
    def decode(self, filename):
        self.filename = filename
        self.read_key_file()
        self.read_message_file()
        self.write_to_file()
        
    def read_key_file(self):
        huff_key = open(self.filename+".KEY", "r")
        num_char = int(huff_key.readline())
        self.orig_mess_len = int(huff_key.readline())
        
        self.dict = {}
        for i in range(num_char):
            symbol = huff_key.read(1)
            code = huff_key.readline().strip()
            self.dict[code]= symbol
        
        huff_key.close()
        self.tree = HuffmanTree()
        self.tree.read_dict(self.dict)

    def read_message_file(self):
        with open(self.filename, 'rb') as huff:
            all_bytes = huff.read()
            lob = list(all_bytes)
            codes = "".join(map(EightBitNumToBinary, lob))

        self.orig_text = ""
        for i in range(self.orig_mess_len):
            (symbol, bits_used) = self.tree.find_char(codes)
            self.orig_text += str(symbol)
            codes = codes[bits_used:]
        

    def write_to_file(self):
        with open(self.filename + ".DECODED", "w") as decoded:
            decoded.write(self.orig_text)

if __name__ == "__main__": 
    decoder = HuffmanDecoder()
    decoder.decode("test.txt.HUFFMAN")
