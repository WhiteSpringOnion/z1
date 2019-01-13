
import tensorflow as tf
import numpy as np

# function take away parameter: input
def make_graph():
    node = []
    
    # add place holder 
    input=tf.placeholder(dtype="int32", shape=[5])
    
    # 我想表達的是for i in range(len(input))，只不過因為input 是Tensor object, 所以寫起來就很麻煩。
    for i in range(tf.shape(input)[0].eval(session=sess)):

        x=input[i]
        x1= tf.Print(x,[x],message="tf_Print is: ",name="julien_node")
        print('x= ',x)
        print('x1= ',x1)
        node.append(x1)
    return node,input    

with tf.Session() as sess:
    input_array = np.array([1,2,3,4,5])
    node, placeholder = make_graph()
    sess.run(node,feed_dict={placeholder:input_array})

# equivalent to sess.run([julien_node, juilen_node_2,juien_node_3,...])