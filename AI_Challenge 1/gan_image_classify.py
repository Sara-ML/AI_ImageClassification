import tensorflow as tf
import sys
import os
import tkinter as tk
from tkinter import filedialog

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

files_dir = './Test_M1' #Directory Location
files = os.listdir(files_dir)
# Loading the graph file
with tf.gfile.FastGFile("./models/output_graph.pb", 'rb') as f: #Graph location
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
# Create and write the output in a file
with open('output_AI1.txt', 'w') as outfile:
    for f in files:
        print(os.path.splitext(f))
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = files_dir + '/' + f
            # Read the image_data
            image_data = tf.gfile.GFile(image_path, 'rb').read()
   

            #Loading labels
            label_lines = [line.rstrip() for line in tf.gfile.GFile("./models/output_labels.txt")] # Labels Location

    
            with tf.Session() as sess:
                # Feed the image_data as input to the graph and get first prediction
                softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
                predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        
                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
       
                #for node_id in top_k:
                human_string = label_lines[0]
                score = predictions[0][0]
                #print('%s (score = %.5f)' % (human_string, score), file=outfile)
                filename = os.path.splitext(f)
                print('%s,%.5f' %(filename[0], score), file=outfile)