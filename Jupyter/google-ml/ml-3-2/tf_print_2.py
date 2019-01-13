import tensorflow as tf 

def graph(input):
    node = []
    for i in range(tf.shape(input)[0].eval()):
        x=input[i]
        x1= tf.Print(x,[x],message="tf_Print is: ",name="julien_node")
        print('x= ',x)
        print('x1= ',x1)
        node.append(x1)
    return node
    

with tf.Session() as sess:
    input = tf.constant([1,2,3,4,5])
    sess.run(graph(input))

# equivalent to sess.run([julien_node, juilen_node_2,juien_node_3,...])