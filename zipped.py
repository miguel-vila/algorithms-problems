def average(nums):
    return sum(nums) / len(nums)

splitted = raw_input().split()
cols = int(splitted[0])
rows = int(splitted[1])
lines = [ raw_input() for _ in xrange(rows) ]
nums = [ [ float(w) for w in words ] for words in [line.split() for line in lines]]
zipped = zip(*nums)
result = [ average(notes) for notes in zipped ]
for r in result:
    print("%.1f" % r)
        
