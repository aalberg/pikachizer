import sys
import random
import re

kWords = {
  1: ["pi"],
  2: ["pi", "ka", "chu"],
  3: ["pii", "pi-i", "kaa", "chu"],
  4: ["pika", "piii", "pipi", "kachu", "kaaa", "chuu"],
  5: ["pikaa", "pikapi", "kachu", "piika", "chuuu"],
  6: ["piikaa", "pikachu", "chuuuu", "pika-pi"],
  7: ["pika-chu", "pika-pika", "piikachu", "pikachu"],
  8: ["pika-pika", "piikachu", "pi-kaaa-chu"],
}

kShortRetext = "[a-zA-Z]{1,8}"
kLongRetext = "[a-zA-Z]{9,}"
kAllRetext = "[a-zA-Z]+"

def pikachize(word):
  length = len(word)
  if length <= 8:
    arr = kWords[length]
    return arr[random.randrange(len(arr))]
  else:
    split = random.randrange(1, len(word))
    return pikachize(word[0:split]) + "-" + pikachize(word[split:])

def pikachizeAndExcite(word, base_excitement = 0):
  new_word = pikachize(word)
  if random.randrange(3) == 2:
    return new_word.capitalize()
  return new_word

def translate(file_contents):
  # This is slow but whatever.
  num_words = len(re.findall(kShortRetext, file_contents)) + \
              len(re.findall(kLongRetext, file_contents))
  advance_rng(2*num_words)
  index = 0
  words = []
  for match in re.finditer(kAllRetext, file_contents):
    span = match.span()
    words += [file_contents[index:(span[0])], \
              pikachizeAndExcite(match.group())]
    index = span[1]
  words += [file_contents[index:]]
  final = "".join(words)
  print(final)
  return final

def advance_rng(num):
  for i in range(num):
    random.randrange(2**32 - 1)
 
# Usage: python pikachizer.py <infile> <outfile>
if __name__ == "__main__":
  random.seed(123)
  if len(sys.argv) != 3:
    print("Wrong number of argv")
    exit(1)
  else:
    with open(sys.argv[1]) as f:
      final = translate(f.read())
      with open(sys.argv[2], "w+") as f2:
        f2.write(final)