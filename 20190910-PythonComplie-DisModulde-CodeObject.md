# PythonComplie-DisModulde-CodeObject

### Stack-PythonComplie-DisModulde

    

    example 1
    >>> import dis    
    
    >>> def add(a,b):
    ...     return a+b        
    >>> dis.dis(add)
     3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
    
    
    
    example 2
    >>> def heron(a, b, c):
    ...     s = (a + b + c) / 2
    ...     return sqrt(s * (s - a) * (s - b) * (s - c))
     3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 LOAD_FAST                2 (c)
              8 BINARY_ADD
             10 LOAD_CONST               1 (2)
             12 BINARY_TRUE_DIVIDE
             14 STORE_FAST               3 (s)
  4          16 LOAD_GLOBAL              0 (sqrt)
             18 LOAD_FAST                3 (s)
             20 LOAD_FAST                3 (s)
             22 LOAD_FAST                0 (a)
             24 BINARY_SUBTRACT
             26 BINARY_MULTIPLY
             28 LOAD_FAST                3 (s)
             30 LOAD_FAST                1 (b)
             32 BINARY_SUBTRACT
             34 BINARY_MULTIPLY
             36 LOAD_FAST                3 (s)
             38 LOAD_FAST                2 (c)
             40 BINARY_SUBTRACT
             42 BINARY_MULTIPLY
             44 CALL_FUNCTION            1
             46 RETURN_VALUE
      
    



### CodeObject
  
  

