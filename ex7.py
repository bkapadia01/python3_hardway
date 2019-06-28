formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("ome", "tow", "there", "for"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "pown text here",
    "mayybe a poem",
    "or a song"
))