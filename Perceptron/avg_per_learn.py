import os
import os.path
import sys
import re
import random

fpath = "F:\\Try\\train"
#fpath = "F:\\USC\\Sem 3\\CSCI - 544\\Try\\train"
x = os.getcwd()

def num_there():
    global fpath
    global x
    global unique_word_weight_dict
    global file_dict
    global main_file_dict
    global file_key_count
    global weight
    global bias
    global avg_weight_dict
    global avg_bias
    global counter

    for root,dirs,files in os.walk(fpath):
        temp = os.path.normpath(root)
        path = os.path.basename(temp)
        #print(path)
        os.chdir(root)

        if path == 'spam': # or path =='spam':
           for file in files:
                if file.endswith(".txt"):
                    f = open( file, 'r', encoding="latin1")
                    predicate = f.read().strip().split() 
                    f.close()
                    #print(predicate)
                    #file_key_count = 0
                    
                    for line in predicate:
                        
                        #file_word_dict[ham_label] = -1
                        
                        'weight dictionary'
                        if line not in unique_word_weight_dict:
                            unique_word_weight_dict[line] = 0
                        if line not in avg_weight_dict:
                            avg_weight_dict[line] = 0
                        'File dictionary and calculation of value_xd'
                        if line in file_dict:
                            file_dict[line] += 1
                        else:
                            file_dict[line] = 1


                    temp1 = []
                    temp1.append(1)
                    temp1.append(file_dict)

                    main_file_dict[file_key_count] = temp1
                    file_key_count += 1

        if path == 'ham': # or path =='spam':
           for file in files:
                if file.endswith(".txt"):
                    f = open( file, 'r', encoding="latin1")
                    predicate = f.read().strip().split() 
                    f.close()
                    #print(predicate)
                    file_key_count = 0
                    

                    for line in predicate:
                        
                        'weight dictionary'
                        if line not in unique_word_weight_dict:
                            unique_word_weight_dict[line] = 0
                        if line not in avg_weight_dict:
                            avg_weight_dict[line] = 0
                        
                        'File dictionary and calculation of value_xd'
                        if line in file_dict:
                            file_dict[line] += 1
                        else:
                            file_dict[line] = 1


                    temp1 = []
                    temp1.append(-1)
                    temp1.append(file_dict)

                    main_file_dict[file_key_count] = temp1
                    file_key_count += 1    

    'calculate the value of alpha(activation)'
    
    y_activation = 0
    for i in range(30):
        for j in range(len(main_file_dict)):
            #random.shuffle(main_file_dict)
            
            activation = 0

            file_type = main_file_dict[j][0]
            dummy = main_file_dict[j][1]
            #print(file_type)
            for key,value in dummy.items():
                activation = unique_word_weight_dict[key] * value
            activation += bias
            y_activation = file_type * activation
            
            if(y_activation <= 0):
                for key,value in dummy.items():
                    unique_word_weight_dict[key] += (file_type * value)
                bias += file_type
                for key,value in dummy.items():
                    avg_weight_dict[key] += (file_type * counter * value)
                avg_bias += (file_type * counter)
            counter += 1

    for key,value in dummy.items():
        avg_weight_dict[key] = unique_word_weight_dict[key] - ((1/counter) * avg_weight_dict[key])
    avg_bias = bias - ((1/counter)*avg_bias)
    
    
    os.chdir(x)
    print(avg_bias)
    #print("----------")
    #print(avg_weight_dict)
    #print("------")
    #print(unique_word_weight_dict)
    #print(counter)
    
    
    #print(dummy)
    print("----------------------")
    #print(main_file_dict)
    #print(unique_word_weight_dict)

    

    rw = open('avg_per_model.txt', 'w', encoding='latin1')
    rw.write(str(avg_bias) + "\n")
    for i in unique_word_weight_dict:
        rw.write(i + "\t" + str(avg_weight_dict.get(i)) + "\n")
    rw.close()

if __name__ == '__main__':
    unique_word_weight_dict = {}
    file_dict = {}
    main_file_dict = {}
    avg_weight_dict = {}
    file_key_count = 0
    weight = 0
    bias = 0.0
    avg_bias = 0.0
    activation = 0.0
    counter = 1
    num_there()
