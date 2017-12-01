

num_lines = sum(1 for line in open("dcs_words_sentence_wise.txt"))
t = int(num_lines * .8)
a = 0
f1 = open("train2.txt","w")
f2 = open("test2.txt","w")
with open("dcs_words_sentence_wise.txt") as f:
  for line in f:
    temp = ""
    for c in line:
      if c == ' ':
        temp += "_ "
      else:
       temp += c + " "
    line = line.strip('\n')
    line = line.lower()
    line = line.replace(" ", "_")
    if a < t:
      f1.write((line + " " + temp).strip(" "))
    else:
      f2.write((line + " " + temp).strip(" "))
    a = a+1

f.close()
f1.close()
f1.close()

