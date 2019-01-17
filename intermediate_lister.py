import parser
import cPickle
from progress.bar import IncrementalBar
import sys

if(len(sys.argv)== 1):
    print 'Starting the process'
    itemlist,wholelist = parser.main()
    counter = 0
    bar = IncrementalBar('Checking refs' , max=len(itemlist))
else:
    print 'continuing process from last time'
    palialist,wholelist = parser.main()
    with open('newlist','rb') as f:
        itemlist = cPickle.load(f)
    with open('stopped_at.txt','r') as stopped:
        counter = int(stopped.read())
        print 'starting counting from %d' %counter
    bar = IncrementalBar('Checking refs' , max=len(itemlist))
    for i in range(counter):
        bar.next()

for i in range(counter,len(itemlist)):
    if counter % 5000 == 0:
        with open('stopped_at.txt','w') as stopped:
            stopped.write(str(counter))
            with open('newlist','wb') as f:
                cPickle.dump(itemlist,f)
            print 'saved at %d items' %counter
    refs = itemlist[i].ret_id_refs()
    for ref in refs:
        if wholelist[int(ref)] not in itemlist:
            itemlist.append(wholelist[int(ref)])
    bar.next()
    counter += 1
bar.finish()
with open('newlist','wb') as f:
    cPickle.dump(itemlist,f)

