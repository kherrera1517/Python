import binary
from collections import Counter

from huffman import HuffmanTree
from binary import BinaryToNum

class HuffmanEncoder(object): 
    def encode(self, filename):
        self.filename = filename
        self.read_text(self.filename)
        self.write_to_files()
        self.print_stats()

    def read_text(self, filename):
        self.filename = filename
        f1 = open(filename, "r")  # Open text file for reading
        self.text = f1.read()  # Read the entire contents of the file into a string
        f1.close() # Always close files after opening them!

        counter = Counter(self.text)

        self.make_tree(counter)


    def make_tree(self, counter):
        lot = [HuffmanTree(symbol=key, freq=counter[key]) for key in counter]
        while len(lot)>1:
            lot.sort()
            newt = lot[0] + lot[1]
            lot = lot[2:] + [newt]
        
        self.tree = lot[0]
        self.dict = dict(self.tree.get_codes())

            
    def write_to_files(self): 
        huff_key = open(self.filename+".HUFFMAN.KEY", "w")
        huff_key.write(str(len(self.dict)) + "\n")
        huff_key.write(str(len(self.text)) + "\n")
        for symbol, code in self.dict.items(): 
            huff_key.write(symbol + code + "\n")
        huff_key.close()

        binary_string = "".join(self.dict[key] for key in self.text)
        total_bytes = len(binary_string)//8
        if len(binary_string)%8 != 0:
            total_bytes += 1

        huff_message = []
        for i in range(total_bytes):
            huff_message.append(BinaryToNum(binary_string[i*8:(i+1)*8]))
        self.huffmess_length = len(huff_message)

        huff = open(self.filename+".HUFFMAN", "wb")
        huff.write(bytes(huff_message))
        huff.close()

    def print_stats(self):
        print("Number of characters in file:", len(self.dict) )
        print("Number of bytes in the input file:", len(self.text))
        print("Number of bytes in the compressed file:", self.huffmess_length)
        print("Asymptotic compression ratio:", self.huffmess_length/len(self.text))
        
        
if __name__ == "__main__":
    encoder = HuffmanEncoder()
    encoder.encode("test.txt")
