import tensorflow as tf

def graph(input):
    x=input[0]
    x1= tf.Print(x,[x],message="tf_Print is : ",name="julien_node")
    print('x= ',x)
    print('x1= ',x1)
    print('x1.name = ',x1.name)
    return x1
    

with tf.Session() as sess:
    input = tf.constant([1,2,3,4,5])
    sess.run(graph(input))
    
# equivalent to sess.run(x1)