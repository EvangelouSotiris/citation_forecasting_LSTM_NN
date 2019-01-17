from parser import Items_struct
import parser
import cPickle
import period_lister as pr
import citation_counter as cit
from progress.bar import Bar

print 'Parsing input text file...\n'
itemlist = parser.main()

index = 280127

print cit.counter_by_list(index,itemlist)
