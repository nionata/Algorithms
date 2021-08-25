from table import ScioTable

s = ScioTable(['a', 'b'])
s.insert_row([1, 2])
s.insert_row([3, 4])

s.read(['a', 'b'])
print()
s.read(['a'])
print()
s.read(['b'])
print()
s.read([])
print()

s.slice(['a']).read([])
print()

ns = s.add_column('c')
ns.read([])
print()
ns.add_column('d').read([])
print()

nns = ns.delete_column('b')
nns.read([])
print()

j = ScioTable(['b', 'c'])
j.insert_row([4, 5])
j.insert_row([6, 7])
j.read([])
print()

s.inner_join(j, 'b').read([])