if __name__ == "__main__":
   
   def main():
      # The input line below won't work correctly running from sublime
      #filename = input("Enter a txt file name such as huff.txt : ")
      # Might need to add 'b' below.
      d = {}
      tempWord = ""
      readFile = open("Sample.txt", "r")
      #huffman = open("huff.txt.HUFFMAN", 'wb')
      for line in readFile:
          for word in line.split():
              if tempWord == "":
                  tempWord = word
              else:
                  if tempWord in d:
                      d[tempWord] += [word]
                  else:
                      d[tempWord] = [word]

                  tempWord = word

              print(word)

      readFile.close()
      print(d['see'])
      #huffman.close()

   main()