# modify this function, and create other functions below as you wish
def question04(v, c, mc):
    # modify and then return the variable below
    sort_v = sorted(v, reverse = False)
    sort_c = sorted(c, reverse = False)
    
    sum_v = []
    sum_c = []
    for i in range(1,len(sort_v)+1):
        comb_v = (list(itertools.combinations(sort_v, i)))
        comb_c = (list(itertools.combinations(sort_c, i)))
        for j in range(len(comb_v)):
            answer = sum(comb_v[j])
            sum_c = sum(comb_c[j])
            #sum_v.append(sum(comb_v[j]))
            #sum_c.append(sum(comb_c[j]))
            if sum_c == mc:
                return answer

