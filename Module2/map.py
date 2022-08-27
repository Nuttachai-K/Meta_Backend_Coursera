menu = ["esso","moca","latte","capp","corta","ameri"]

def find_coff(coff):
    if coff[0] == 'c':
        return coff

#map
map_coff = map(find_coff,menu)
print(map_coff)
for i in map_coff:
    print(i)

#filter
filter_coff = filter(find_coff,menu)
print(filter_coff)
for i in filter_coff:
    print(i)