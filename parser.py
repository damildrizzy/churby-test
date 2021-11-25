import re


def parse(text: str, vars: dict):
    result = 0
    
    texts = text.splitlines()  
    for text in texts:
        text.strip()
        val = analyze(text, vars)
        if not text.startswith("i"):
            operator = text[:text.find("i")]
            result = eval(f"{result}{operator}{val}")
        else:
            result += val
    
    print(result)
    return result



def analyze(expr: str, vars: dict):
    try:
        expr = int(expr.lstrip().replace(")", ""))
        return expr
    except ValueError:
        cond,truthy,falsy = expr.split(",", 2)
        # remove 'if ( '
        cond = cond[cond.find("(")+1:]
        var = cond.split()[0]
        cond = cond.replace(var, str(vars[var]))
        
        if eval(cond):
            return analyze(truthy, vars)
        return analyze(falsy, vars)

 

parse("""if (var_1 == 2, 0, if (var_2 == 4, 15, 0))
+ if (var_2 == 3, 5, 0)
// if (var_4 == 2, 0, 5)
+ if (var_3 == 3, 5, 0)""", 
{
  "var_1": 1,
  "var_2": 4,
  "var_3": 3,
  "var_4": 5
})