from collections import defaultdict

def get_new_ord(original_alpha, idx):
    # a ~ z -> 97 ~ 122
    new_ord = 97 + (ord(original_alpha)-97 + idx) % 26
    return new_ord
    
def solution(s, skip, index):
    skip_dict = defaultdict(bool)
    
    for skip_alpha in skip:
        skip_dict[ord(skip_alpha)] = True
    
    answer = ''
    for alpha in s:
        idx = index
        i = 1
        while i <= idx:
            if skip_dict[get_new_ord(alpha, i)]:
                idx += 1
            i += 1
        answer += chr(get_new_ord(alpha, idx))

    return answer