def solution(sequence, k):
    s, e = 0, 0
    p_sum = sequence[0]
    min_len = len(sequence)+1
    answer = [s, e]
    
    while s <= e:
        if p_sum < k:
            if e == len(sequence)-1:
                return answer
            e += 1
            p_sum += sequence[e]
        elif p_sum > k:
            p_sum -= sequence[s]
            s += 1
        else:
            if min_len > e - s + 1:
                min_len = e-s+1
                answer = [s, e]
            p_sum -= sequence[s]
            s += 1
            
    
    return answer
