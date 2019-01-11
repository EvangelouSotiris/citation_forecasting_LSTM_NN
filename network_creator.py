from parser import Items_struct
import cPickle
import period_lister as pr
#import citation_counter as cit
from progress.bar import Bar

#print 'Parsing input text file...\n'
#itemlist = parser.main()

with open('parsedtxt' , 'rb') as f:
    itemlist = cPickle.load(f)

print len(itemlist)
