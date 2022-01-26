# -*- coding: utf-8 -*-

word = input("")

m = {word.count(k):k for k in set(word)}

print(m[max(m)])
