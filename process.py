print 'var _entities = {'

f = open('entities')
for entity in f:
	s = entity.split('\t')
	print '\t"%s": "%s",' % (s[0], s[1])
f.close()

print '};'
