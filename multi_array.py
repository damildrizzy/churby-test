def generate(arrs: list):
    result = [[]]
    for arr in arrs:   
        result = [x+[y] for x in result for y in arr]
    
    return [" ".join(str(x) for x in r) for r in result]


print(generate([[1, 2, 3],
  [4, 5, 6], [7,8,9]]))