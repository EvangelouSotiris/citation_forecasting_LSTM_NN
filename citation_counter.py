# Given a list, either the forecasting or the validation period, and an index
#this program calculates the total citations of index in that period.

def counter_by_list(index, certlist):
    total_citations = 0
    for i in range(len(certlist)):
        id_refs = certlist[i].ret_id_refs()
        for ref in id_refs:
            if index == int(ref):
                total_citations = total_citations + 1

    return total_citations
