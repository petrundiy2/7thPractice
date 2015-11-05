def f(accumulator, options):
    if len(options) == 0:
        print(*accumulator,sep=' ')
        return
    for element in options:
        newOptions = list(options)
        newOptions.remove(element)
        f(accumulator + element, newOptions)
a=''
n=int(input())
for x in range(1,n+1):
    a+=str(x)

f('',a)
