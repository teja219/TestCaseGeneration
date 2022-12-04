### TestCaseGeneration

## Installation

- Clone the project locally
- Create a virtual environment in the root folder: python3.10 -m venv env
- Activate the virtual environment: source env/bin/activate
- ```brew install graphviz```
- ```pip install --global-option=build_ext --global-option="-I$(brew --prefix graphviz)/include/" --global-option="-L$(brew --prefix graphviz)/lib/" pygraphviz```
- Install all packages in requirements.txt file: python3.10 -m pip install -r requirements.txt
- To convert a jupyter notebook to README : ```jupyter nbconvert --execute --to markdown README.ipynb```
- To convert a jupyter notebook to python file: ```jupyter nbconvert --to script testCaseGeneration.ipynb```

## Scope

- Handles bools,int and floats
- Code shouldn't have functions
- Supports >,<,==,+,*,-,>=,<= operations
- Incase a variable can take any value
    - Floats will default to a random value between 0 to 2 in the example test case
    - Ints will default to random value between 1 to 9 in the example test case
- The arguments of the function type must be defined

## Examples


```python
import testCaseGeneration as TG


def func1(a:int,b:int):
    a = a * 1
    b = b + 4
    a = a + 4
    c = a * a
    return a

def func2(a:int,b:float):
    if a == 1 and b==2.3:
        b = 2
        return 233
    return 333

def func3(a:int,b:int):
    if a == 1 and b==2:
        b = 2
        return 233
    elif b==3:
        b = 4
        return
    else:
        a = 1
    return 333

def func4(a:int,b:int,c:bool):
    if a==3 or c:
        if b==4:
            return
        else:
            return
    elif a==2 and b==4:
        return
    else:
        return
```

    342           0 LOAD_FAST                0 (a)
                  2 LOAD_CONST               1 (1)
                  4 COMPARE_OP               2 (==)
                  6 POP_JUMP_IF_FALSE       12 (to 24)
                  8 LOAD_FAST                1 (b)
                 10 LOAD_CONST               2 (2.3)
                 12 COMPARE_OP               2 (==)
                 14 POP_JUMP_IF_FALSE       12 (to 24)
    
    343          16 LOAD_CONST               3 (2)
                 18 STORE_FAST               1 (b)
    
    344          20 LOAD_CONST               4 (233)
                 22 RETURN_VALUE
    
    345     >>   24 LOAD_CONST               5 (333)
                 26 RETURN_VALUE
    Bytecode(<function func2 at 0x107663eb0>)



```python
(g,_,models,results) = TG.generateTestCases(func1)
print("Test Cases")
for res in results:
    print(res)
print("Display dependency graph")
g
```

    Bytecode(<function func1 at 0x1073e45e0>)
    Test Cases
    [('a', '-4'), ('b', '-4')]
    Display dependency graph





    
![svg](README_files/README_2_1.svg)
    




```python
(g,_,models,results) = TG.generateTestCases(func2)
print("Test Cases")
for res in results:
    print(res)
print("Display dependency graph")
g
```

    Bytecode(<function func2 at 0x1073e4af0>)
    Test Cases
    [('a', '2'), ('b', '0.34')]
    [('a', '1'), ('b', '33/10')]
    [('a', '1'), ('b', '23/10')]
    Display dependency graph





    
![svg](README_files/README_3_1.svg)
    




```python
(g,_,models,results) = TG.generateTestCases(func3)
print("Test Cases")
for res in results:
    print(res)
print("Display dependency graph")
g
```

    Bytecode(<function func3 at 0x107688160>)
    Test Cases
    [('a', '2'), ('b', '3')]
    [('a', '2'), ('b', '4')]
    [('a', '1'), ('b', '3')]
    [('a', '1'), ('b', '0')]
    [('a', '1'), ('b', '2')]
    Display dependency graph





    
![svg](README_files/README_4_1.svg)
    




```python
(g,_,models,results) = TG.generateTestCases(func4)
print("Test Cases")
for res in results:
    print(res)
print("Display dependency graph")
g
```

    Bytecode(<function func4 at 0x1076881f0>)
    Test Cases
    [('a', '3'), ('b', '4'), ('c', 'False')]
    [('a', '3'), ('b', '5'), ('c', 'False')]
    [('a', '2'), ('b', '5'), ('c', 'False')]
    [('a', '2'), ('b', '4'), ('c', 'False')]
    [('a', '0'), ('b', '3'), ('c', 'False')]
    [('a', '4'), ('b', '4'), ('c', 'True')]
    [('a', '4'), ('b', '5'), ('c', 'True')]
    Display dependency graph





    
![svg](README_files/README_5_1.svg)
    




```python

```
