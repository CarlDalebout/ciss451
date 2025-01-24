import string
s = """
Edgar Allan Poe's C. Auguste Dupin is generally acknowledged as the first detective in fiction and served as the prototype for many later characters, including Holmes.[8] Conan Doyle once wrote, "Each [of Poe's detective stories] is a root from which a whole literature has developed ... Where was the detective story until Poe breathed the breath of life into it?"[9] Similarly, the stories of Émile Gaboriau's Monsieur Lecoq were extremely popular at the time Conan Doyle began writing Holmes, and Holmes's speech and behaviour sometimes follow those of Lecoq.[10][11] Doyle has his main characters discuss these literary antecedents near the beginning of A Study in Scarlet, which is set soon after Watson is first introduced to Holmes. Watson attempts to compliment Holmes by comparing him to Dupin, to which Holmes replies that he found Dupin to be "a very inferior fellow" and Lecoq to be "a miserable bungler"
"""
# print(s)

t = []
for c in s:
  if c in string.ascii_letters:
    print(c.lower())
    t.append(c.lower())
t = ''.join(t)
print(t)
freq = {}
for c in string.ascii_lowercase:
    freq[c] = t.count(c)/len(t)
for k,v in freq.items():
   print(f"{k}, {v}")

def shift(k, s):
   t = []
   for c in s:
      d = (ord(c) - ord('a') + k) % 26
      e = chr(d + ord('a'))
      t.append(e)
      return ''.join(t)

print(t[:20])
print(shift(0, t)[:20])
print(shift(1, t)[:20])

y = shift(7, "abcde")
print(y)