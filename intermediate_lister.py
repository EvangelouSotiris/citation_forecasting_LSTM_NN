import parser
import cPickle
from progress.bar import IncrementalBar

def find_by_index(index,wholelist):
    for i in wholelist:
        if index == i.ret_index():
            return i

itemlist, wholelist = parser.main()

newlist = []
bar = IncrementalBar('Checking refs' , max=len(itemlist))
for i in itemlist:
    refs = i.ret_id_refs()
    for ref in refs:
        if int(ref) not in itemlist:
            itemlist.append(find_by_index(int(ref),wholelist))
            #print 'appended.'
    bar.next()
bar.finish()
with open('newlist','wb') as f:
    cPickle.dump(newlist,f)

