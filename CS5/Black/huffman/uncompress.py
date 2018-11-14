import binary
from collections import Counter

from huffman import HuffmanTree

class HuffmanDecoder(object):
    def decode(self, filename):
        self.filename = filename
        self.read_key_file()
        self.read_message_file()
        self.write_to_file()
        
    def read_key_file(self): 
        print("Not implemented yet")

    def read_message_file(self):
        print("Not implemented yet")
        
    def write_to_file(self):
        print("Not implemented yet")
        
if __name__ == "__main__": 
    decoder = HuffmanDecoder()
    decoder.decode("test.txt.HUFFMAN")
