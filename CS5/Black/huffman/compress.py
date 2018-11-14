import binary
from collections import Counter

from huffman import HuffmanTree

class HuffmanEncoder(object): 
    def encode(self, filename):
        self.filename = filename
        self.read_text(self.filename)
        self.write_to_files()
        self.print_stats()

    def read_text(self, filename):
        print("Not implemented yet")
                
    def make_tree(self, counter): 
        print("Not implemented yet")
        
            
    def write_to_files(self): 
        print("Not implemented yet")

    def print_stats(self):
        print("Number of characters in file:", 0 )
        print("Number of bytes in the input file:", 0)
        print("Number of bytes in the compressed file:", 0)
        print("Asymptotic compression ratio:", 0)
        
        
if __name__ == "__main__":
    encoder = HuffmanEncoder()
    HuffmanEncoder.encode("test.txt")
