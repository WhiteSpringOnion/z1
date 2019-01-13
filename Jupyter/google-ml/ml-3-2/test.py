
import tensorflow as tf
# tf.enable_eager_execution()

def some_method(a, b):
    b = tf.cast(b,tf.float32)
    s = (a/b)
    print_ab = tf.Print(s,[a,b],summarize=10,message='a,b: ')
    s= tf.Print(print_ab, [print_ab],message='s ')
    isnan= tf.is_nan(s)
    isnan = tf.Print(isnan, [isnan], message='is_nan: ')
    s = tf.where(isnan,s,s)
    return tf.sqrt(tf.matmul(s,tf.transpose(s)))

def f():
    fake_a = tf.constant([[5.0, 3.0, 7.1 ], [2.3,4.1,4.8]])
    fake_b = tf.constant([[2,0,5], [2,8, 7]])
    some_method(fake_a,fake_b)
  

matrix_sqrt = f()
print(matrix_sqrt)
    
# <https://www.tensorflow.org/api_docs/python/tf/print>