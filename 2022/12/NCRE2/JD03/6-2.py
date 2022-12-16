fi = open("论语-原文.txt", "r", encoding="utf-8")
fo = open("论语-提纯原文.txt", "w", encoding="utf-8")

import re
for line in fi:
    fo.write(re.sub(r'\(\d+\)', '', line))
fi.close()
fo.close()