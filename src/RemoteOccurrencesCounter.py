import sys
from os import walk

path = sys.argv[1]
filesList = []
for (dirpath, dirnames, filenames) in walk(path):
    filesList.extend(filenames)
    break

names = list()

for filename in filesList:
    idxStart = filename.find('_') + 1
    idxEnd = len(filename) - filename[::-1].index('_') - 1
    name = filename[idxStart:idxEnd]
    names.append(name.lower())

occurrencesDict = dict()

for name in names:
    if(occurrencesDict.__contains__(name)):
        occurrencesDict[name] +=1
    else:
        occurrencesDict[name] = 1

#
#
#
# for curr_name in names:
#     occurrencesDict[curr_name] = 1
#
#
#
#
# for i in range(0, len(names) - 1):
#     for j in range(i + 1, len(names)):
#         if names[i] == names[j]:
#             ocCount = occurrencesDict[names[i]]
#             occurrencesDict[names[i]] = ocCount + 1
#
# for key, value in occurrencesDict.items():
#     print (key, value)
#

text_file = open("Remotes Occurrences.txt", "w")
for key, value in sorted(occurrencesDict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    text_file.write( "%s: %s" % (str(key), str(value))+"\n")

text_file.close()
