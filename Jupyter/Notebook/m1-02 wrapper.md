
<https://realpython.com/primer-on-python-decorators/>
----------------------
# Case 1: wrapped function taking no input 

## 1. original function  


```python
def sayhi():
    print("HI")
```


```python
sayhi()
```

    HI


## 2. 想法： 加工包成一個函數


```python
def double(func):
    func()
    func()
```


```python
double(sayhi)
```

    HI
    HI


## 3. 實踐：使用wrapper 
來 retun “double” 這個加工的 函式


```python
def wrapper(func):
    def double():
        func();
        func();
    return double 
```

## 4. 使用wrapper 函數


```python
sayhi = wrapper(sayhi)
sayhi()
```

    HI
    HI


## 5. code sugar 


```python
@wrapper
def sayhi():
    print('hi')

sayhi()
```

    hi
    hi



```python
@wrapper 
def saygod():
    print("Oh Godsh! ")
    
saygod()
```

    Oh Godsh! 
    Oh Godsh! 


------

# Case 2: a function which takes input

## 1. 一個original function:  that takes input 


```python
def sayhito(name):
    print(f'Hi, {name}!')
    
sayhito('tom')
```

    Hi, tom!


## 2. 想法：加工包裝成function


```python
def double(sayhito,name):
    sayhito(name)
    sayhito(name)

double(sayhito, 'Tome')
```

    Hi, Tome!
    Hi, Tome!


## 3. 實踐： 使用wrapper 
來retun “double” 這個加工函式


```python
def wrapper(func): 
    def double(*arg):
        func(*arg)
        func(*arg)
    return double 

```

## 4. 方法一：使用wrapper 函數


```python
sayhito = wrapper(sayhito)             # return inner function 

sayhito('Tom')                      # 執行 
```

    Hi, Tom!
    Hi, Tom!



## 5. 方法二：使用code sugar 


```python
@wrapper
def sayhito(*arg):
    print(f'hi {arg}')
```


```python
sayhito('Tom',"peter")
```

    hi ('Tom', 'peter')
    hi ('Tom', 'peter')


# Case 3 Wrapped funtion returns a value 

## 1. 一個 original function


```python
def sayhito(name):
    print(f'Hi, {name}!')
    return f'return of variable: {name}'
```

## 2. 想法：包裝成function 


```python
def double(sayhito, name):
    sayhito(name)
    sayhito(name)
    return sayhito(name)

return_variable = double(sayhito, 'Mary')
print(return_variable)
    
```

    Hi, Mary!
    Hi, Mary!
    Hi, Mary!
    return of variable: Mary


## 3. 實踐：用Use Wrapper 來包裝成function 


```python
def wrapper(func):
    def double(*arg):
        func(f'Hi, {arg}!')
        return func(f'Hi, {arg}!')
    return double
    
```

## 4. 方法一：使用wrapper 


```python
sayhito = wrapper(sayhito)

return_variable = sayhito('Mary')
print(return_variable)
```

    Hi, Hi, ('Mary',)!!
    Hi, Hi, ('Mary',)!!
    return of variable: Hi, ('Mary',)!


## 5. 方法二：使用code sugar 


```python
@wrapper
def saytito(*arg):
    print(f'Hi, {arg}!')
    return sayhito(*arg)

return_variable = sayhito("Mary")
print(return_variable)
```

    Hi, Hi, ('Mary',)!!
    Hi, Hi, ('Mary',)!!
    return of variable: Hi, ('Mary',)!


# Case 4: functools.wrap()

##### 背景： sayhito 被decoratored後， 是一個指向 wrapper_fuction 裡面的double_innerFunction 的一個variable。



```python
sayhito
sayhito.__name__
```




    <function __main__.wrapper.<locals>.double>






    'double'



## 主題： 讓sayhito 經過decorated 後，成為一個 新的function，而不是一個指向 wrapper_function 裡的inner_function 的 指標。  
#### functools.wraps()
#### ------  @functools.wraps(func)


```python
import functools

def wrapper(func):
    @functools.wraps(func)
    def double(*arg):
        func(f'Hi, {arg}!')
        return func(f'Hi, {arg}!')
    return double
```


```python
@wrapper
def sayhito(*arg):
    print(f'Hi, {arg}!')
    return f'return_variable = {arg}'

sayhito
sayhito.__name__
```




    <function __main__.sayhito>






    'sayhito'



--------

# Summary 


```python
def wrapper(*arg):
    def process_function(*arg):
        func(*arg)
        return fun(*arg)
    return process_function 

```
