# Python 学习笔记

## 第一天

### <u>列表</u>

1. 列表操作--遍历列表、对列表的增删改查 以插入为例：

```pytho
if __name__ == "__main__":
    listvalue = list()
    for i in range(1,11):
        listvalue.append(i)
    # 上面表示对列表插入 1——10个整数
```



列表解析方式插入列表

```py
if __name__ == "__main__":
    listvalue = [value for value in range(1,11)]
```

下面测试下两种方式的程序运行时间上的差距:

第一种：

```pyth
import time
if __name__ == "__main__":
    start_time = time.time()
    listvalue = list()
    for i in range(1,100001):
        listvalue.append(i)
    end_time = time.time()

    run_time = end_time - start_time
    print(run_time)
#执行时间为：
0.007964372634887695
```

第二种方式:

```py
import time
if __name__ == "__main__":
    start_time = time.time()
    # listvalue = list()
    # for i in range(1,100001):
    #     listvalue.append(i)
    listvalue = [value for value in range(1,100001)]
    end_time = time.time()
    run_time = end_time - start_time
    print(run_time)
#执行时间：
0.003989458084106445
```

**可以看出 列表解析方式 可以简化代码并且可见减少程序执行时间**

------

### Python <u>名字空间</u>

不同于其他语言 python没有单独变量这一说

```py
x
# 这样的代码 会出错
Traceback (most recent call last):
  File "e:\pythontest\hello.py", line 3, in <module>
    x
NameError: name 'x' is not defined

x = 123 # 使用 globals()来获取名字空间

if __name__ == "__main__":
    x = 123
    print(globals())
返回{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000017D77D8BD70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'e:\\pythontest\\hello.py', '__cached__': None, 'x': 123}
# 可以看到 x :123 是一个 字典类型

```



