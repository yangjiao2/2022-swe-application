
# 1722. Minimize Hamming Distance After Swap Operations
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = [i for i in range(len(source))]

        def find(x):
            while uf[x]!=x:
                x = uf[x]
            return x

        for swap in allowedSwaps:
            x1 = find(swap[0])
            x2 = find(swap[1])
            uf[x1] = x2

        group_dict = defaultdict(list)
        for x in range(len(uf)):
            group_dict[find(x)].append(x)
        print (group_dict)

        val = 0
        for group_key in group_dict:
            cur_source = Counter([source[i] for i in group_dict[group_key]])
            print (cur_source)
            cur_target = Counter([target[i] for i in group_dict[group_key]])
            print (cur_target)
            cur_target.subtract(cur_source)
            print ('=')
            print (cur_target)
            diff_val = [v for k,v in cur_target.items() if v>=0]
            val += sum(diff_val)
        return val

# Input:
# [1,2,3,4]
# [2,1,4,5]
# [[0,1],[2,3]]

# Output:

# defaultdict(<class 'list'>, {1: [0, 1], 3: [2, 3]})
# Counter({1: 1, 2: 1})
# Counter({2: 1, 1: 1})
# =
# Counter({2: 0, 1: 0})
# Counter({3: 1, 4: 1})
# Counter({4: 1, 5: 1})
# =
# Counter({5: 1, 4: 0, 3: -1})

# thinking process:
- Connected component (Union find): use array to record swaps by index, construct dict for avaailble swaps
- subtract from each appearance of 
