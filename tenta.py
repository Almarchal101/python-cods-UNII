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



"""def reverse_pairs(seq: list):
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
"""



"""def expand(mem: list[str], msg: list):
    list1 = mem.copy()
    result = []
    
    word_posision = msg[0]
    word = mem[word_posision]
    
    if len(list1) <= 0:
        print("done")
        return result
    else: 
        result.append(word)
        return expand(mem[1:], msg[1:])
    
    

    
mem = [' ','att','lycka','tenta','till','på','är','kanske','tentan']
print(expand(mem, [2, 6, 1, 3]))  """

"""
def expand(mem: list[str], msg: list):
    result = []
    
    if not msg:
        return []
    
    elif isinstance(msg[0], int):
        word_pisision = msg[0]
        word = mem[word_pisision]
        result.append(word)
        return [word] + expand(mem,msg[1:])
    
    elif isinstance(msg[0],str):
        word = msg[0]
        result.append(word)
        return [word] + expand(mem,msg[1:])
    
    elif isinstance(msg[0], list):
        lista = msg[0]
        return [expand(mem,lista)] + expand(mem,msg[1:])
     
    
    else:
        return expand(mem,msg[1:])
 
        

    
    

mem = [' ','att','lycka','tenta','till','på','är','kanske','tentan']
print(expand(mem, [2, 6, 1, 3]))
print(expand(mem, [2, 4,'med', 8]))
print(expand(mem, [2, 6, [7,'att', []], 3]))


print(expand(mem, [2, 6, 1, 3]) == ['lycka', 'är','att','tenta'])
print(expand(mem, [2, 4,'med', 8]) == ['lycka','till','med','tentan'])
print(expand(mem, [2, 6, [7,'att', []], 3]) == ['lycka','är', ['kanske','att', []],'tenta'])
"""
"""
def expand_concat(mem: list[str], msg: list):
   
    result = []
    medelande = ""
    
    for element in msg:
        
        if isinstance(element, int):
            medelande += mem[element]
            
        elif isinstance(element, str):
            medelande += element
            
        elif isinstance(element, list):
            if medelande != "":
                result.append(medelande)
                medelande = ""
            result.append(expand_concat(mem, element))
        
        
    if medelande != "":
        result.append(medelande)
            
   
    
    return result
         
    
    

    
    
mem = [' ','att','lycka','tenta','till','på','är','kanske','tentan']
print( expand_concat(mem, [2, 6, 1, 3, 0, 'att']))
print(expand_concat(mem, [2, 0, 6, [7, 0,'att', []], 3, 0]))




print(expand_concat(mem, [2, 0, 6, 0, 1, 0, 3]))  
print(expand_concat(mem, [2, 0, 6, [7, 0,'att', []], 3, 0]))


print(expand_concat(mem, [2, 6, 1, 3]) == ['lyckaäratttenta'])
print(expand_concat(mem, [2, 0, 6, 0, 1, 0, 3]) == ['lycka är att tenta'])
print(expand_concat(mem, [2, 0, 6, [7, 0,'att', []], 3, 0]) ==
['lycka är', ['kanske att', []],'tenta '])
print(expand_concat(mem, [[[3, 3, [], [], 3]]]) ==
[[['tentatenta', [], [],'tenta']]])
"""


def pred_comp(p, t, f) :
    def argument(x):
        if p(x):
            return t(x)
        else:
            return f(x)
        
    return argument
    
    
print( pred_comp(lambda x: x > 0, lambda x: x, lambda x: -x)(-4))

add_world = pred_comp(lambda x: x == "", lambda x: x, lambda x: x + "World")
print(add_world("Hello") == "HelloWorld")
print(add_world("") == "")



def is_zero(t):
    x, y = t
    return y == 0


def return_zero(t):
    return 0


def divide(t):
    x, y = t
    return x / y
safe_div = pred_comp(is_zero, return_zero, divide)


print(safe_div((10, 5)))
assert safe_div((10, 4)) == 2.5
assert safe_div((10, 0)) == 0