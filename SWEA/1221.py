test = int(input())
for i in range(test):
    case_num, length = input().split()
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_rule = {num:idx for idx, num in enumerate(numbers)}
    n_list = input().split()
    idxs = sorted([num_rule[n] for n in n_list])
    sorted_n_list = [numbers[idx] for idx in idxs]
    print(case_num)
    print(' '.join(sorted_n_list))
    

test = int(input())
for i in range(test):
    case_num, length = input().split()
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_count = {num:0 for num in numbers}
    n_list = input().split()
    print(case_num)
    ordered = []
    for num in numbers:
        num_count[num] = n_list.count(num)
        ordered += [num]*num_count[num]
    print(' '.join(ordered))