import testCaseGeneration as TG
import dis
import os

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

def func5(a:int, b:int):
    if a != b:
        return 233
    else:
        return 333

def analyse(func):
    (g,bc,models,results) = TG.generateTestCases(func)

    print("ByteCode")
    dis.dis(bc.codeobj)

    # print("Models")
    # print(models)

    print("Test Cases")
    for res in results:
        print(res)

    print("Display dependency graph")
    g.format = 'pdf'
    g.filename = func.__name__
    g.render().replace('\\', '/')

    # Mac specific
    # Uncomment this to open the generated PDF automatically
    # os.system(f'open -a Preview.app {func.__name__}.pdf')

analyse(func1)
analyse(func2)
analyse(func3)
analyse(func4)
analyse(func5)
