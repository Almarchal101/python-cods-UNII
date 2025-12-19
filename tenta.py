"""def find_least_close(seq1: list[int], seq2: list[int]): 
    result = []
    
    for x in  seq1:
        maxdist = -1
        choosen = None
        
        for y in seq2:
            dist = abs(x - y)
            if dist > maxdist:
                maxdist = dist
                choosen = y 
            elif dist == maxdist and y > choosen:
                choosen = y
        result.append(choosen)
            
    return result
    
print(find_least_close([11], [5, 8, 12, 15]))
print(find_least_close([10], [5, 8, 12, 15]))
print(find_least_close([12, 10], [-1000, 5, 8, 12, 15]))"""



def reverse_pairs(seq: list):
    result = seq.copy()
    
    for nummer in range(0, len(result) -1,2):
            result[nummer], result[nummer + 1] = result[nummer + 1], result[nummer]
    
    return result
    

print(reverse_pairs([1,2,"x", 4, 5]))


def recreverce_pairs(seq: list):
    result = seq.copy()
    
    if len(result) < 2:
        print("Done")
        return result
        
    else: 
        first, secound = result[1], result[0]
        
        return [first, secound] + recreverce_pairs(result[2:])
    
print(recreverce_pairs([1,2,"x", 4, 5]))