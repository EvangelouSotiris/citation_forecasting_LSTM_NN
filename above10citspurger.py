import cPickle
from progress.bar import Bar
from progress.counter import Counter
import citation_counter as cit
from parser import Items_struct
from threading import Thread

def purge(i, initial_list):
    if i != 25:
        end = i*10000 + 9999
    else:
        end = 246298
    start = i*10000
    newlist = []
    #bar = Bar('Thread '+str(i)+ ' in range ('+str(i*10000)+','+str(end)+')' , max = end - i*10000)
    for j in range(start,end):
        if cit.counter_by_list(initial_list[j].ret_index() , initial_list) > 10:
            newlist.append(item)
        if (j-start) % 100 == 0:
            print 'Thread '+str(i) + ': '+str(j)+'/'+ str(end-start)
        #bar.next()
    #bar.finish()
    return newlist

if __name__ == '__main__':
    with open('parsedtxt' , 'rb') as inp:
        initial_list = cPickle.load(inp)
    print 'Loaded list with %d' %len(initial_list)
    newlist = []
    print 'Proceeding to purge the items citated less than 10 times.'

    newlist = []
    threads = []
    for i in range(25):
        x = Thread( target=purge , args=(i, initial_list) )
        x.start()
        threads.append(x)

    bar = Bar('Purging' , max=25)
    for i in range(len(threads)):
        templist = threads[i].join()
        print 'Thread %d returned' %i
        bar.next()
        newlist.extend(templist)

    bar.finish()
    with open('purged' , 'wb') as purged:
        purged.dump(newlist)
