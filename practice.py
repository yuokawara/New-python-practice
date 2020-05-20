# ## 練習
# def hello():
#     print('ドーモ、ニンジャです')

# hello()

# ## 練習2
# def add(a,b,c):
#     return a + b + c

# result = add(1,2,3)
# print(result)

## まとめてタプルに入れてくれる *args

def ninja(*args):
    for arg in args:
        print(arg)
ninja('ダークニンジャサン', 'フジキドサン','ラオモトサン')

## **kwargs キーワードargs

def jitsu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# jitsu(jitsu1='カトンジツ', jitsu2='スリケン')

d = {
    'jitsu1': 'カトンジツ',
    'jitsu2': 'スリケン',
    'jitsu3': 'チャドー呼吸法'
}
jitsu(**d)