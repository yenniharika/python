def count_calls(func):
    count=0
    def wrapper():
        nonlocal count
        count+=1
        print(f"call{count}:function exicuted")
        return func()
        ret
