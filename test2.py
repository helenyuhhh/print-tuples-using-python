# my version of counting words from a file input by a user
fname = input('Enter file:')
timedic = dict()
timelist = list()


try:
    ofile = open(fname, 'r')
except:
    print("File doesn't exist!")
    quit()
for lines in ofile:
    if lines.startswith('From '):
        lines.rstrip()
        line = lines.split()
        times = line[5]
        timesplit = times.split(':')
        timelist.append(timesplit[0])
for hours in timelist:
    timedic[hours] = timedic.get(hours, 0) + 1
for k,v in sorted(timedic.items()):
    print(k,v)
