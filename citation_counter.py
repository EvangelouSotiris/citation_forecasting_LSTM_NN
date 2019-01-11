# Given a list, either the forecasting or the validation period, and an index
#this program calculates the total citations of index in that period.

def counter_by_list(index, certlist):
    total_citations = 0
    for item in certlist:
        if item.ret_index() == index:
            continue
        else:
            refs = item.ret_id_refs()
            for refed_index in refs:
                if index == refed_index:
                    total_citations += 1

    return total_citations
