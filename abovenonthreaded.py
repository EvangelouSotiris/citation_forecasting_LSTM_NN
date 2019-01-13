import cPickle
from progress.bar import IncrementalBar
from progress.counter import Counter
import citation_counter as cit
from parser import Items_struct
from threading import Thread

def purge(initial_list):
    bar = IncrementalBar('Purging' , max=len(initial_list))
    newlist = []
    for j in initial_list:
        if cit.counter_by_list(j.ret_index() , initial_list) > 10:
            newlist.append(j)
        bar.next()
    bar.finish()
    return newlist

if __name__ == '__main__':
    with open('parsedtxt' , 'rb') as inp:
        initial_list = cPickle.load(inp)
    print 'Loaded list with %d items' %len(initial_list)
    print 'Proceeding to purge the items citated less than 10 times.'
    newlist = purge(initial_list)
    print 'Output, list with %d items' %len(newlist)
    with open('purged' , 'wb') as purged:
        purged.dump(newlist)
