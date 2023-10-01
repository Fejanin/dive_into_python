# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def foo(*, a, b, c):
    loc = locals()
    res = {}
    for i in loc:
        if is_hashable(loc[i]):
            res[loc[i]] = i
        else:
            res[str(loc[i])] = i
    return res

def is_hashable(value):
    try:
        hash(value)
        return True
    except:
        pass

print(foo(b=1, a=[2, 2], c=3))
print(foo(a=(2, 3), c=3, b='44'))
try:
    print(foo(1, 2, 3))
except TypeError:
    print('Принимаются только ключевые параметры.')
