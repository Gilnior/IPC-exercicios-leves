# -*- coding: utf-8 -*-

word = input("")

m = {word.count(k):k for k in set(word) if k.lower() in ('a', 'e', 'i', 'o', 'u')}

print(m[max(m)])
