import glob, os
import sys, random

fpath = "F:\\Try\\train"
#fpath = sys.argv[-1]

rw = open("per_model.txt", 'w',encoding="latin1")

class num_there:
    
    def __init__(self, dir):
        self.dir = dir

    def main_calculation(self,main_dict,temp,bias,temp_list):


        for key_count_value in temp_list:
            total = 0
            unique_word_weight = temp
            activation = 0
            spam_label = 1
            ham_label = -1
            y_activation = 0

            for word in main_dict[key_count_value][0]:
                total += main_dict[key_count_value][0].get(word) * unique_word_weight.get(word)

            activation = total + bias

            if(main_dict[key_count_value][1] == 'spam'):
                y_activation = spam_label * activation
            elif(main_dict[key_count_value][1] == 'ham'):
                y_activation = ham_label * activation

            if (y_activation <= 0):
                if (main_dict[key_count_value][1] == 'spam'):
                    for words in main_dict[key_count_value][0]:

                        unique_word_weight[words] = unique_word_weight.get(words) + (spam_label * int(main_dict[key_count_value][0].get(words)))
                    bias = bias + spam_label
                else:
                    for words in main_dict[key_count_value][0]:
                        unique_word_weight[words] = unique_word_weight.get(words) + (ham_label * int(main_dict[key_count_value][0].get(words)))
                    bias = bias + ham_label
        return unique_word_weight,bias

    def tokenization(self):

        main_dict = {}
        key_count_value = 0
        weight_dict = {}

        for root, subdirs, files in os.walk(self.dir):
            os.chdir(root)
            for file in glob.glob("*.txt"):
                key_count_value += 1
                file_dict = {}

                with open(file, "r", encoding="latin1") as f1:
                    for line in f1:
                        
                        for word in line.strip().split():
                            if word not in file_dict:
                                file_dict[word] = 1
                            else:
                                file_dict[word] = file_dict.get(word) + 1
                            if word not in weight_dict:
                                weight_dict[word] = 0

                if (os.path.basename(os.path.normpath(root)) == 'spam'):
                    main_dict[key_count_value] = file_dict, 'spam'
                elif(os.path.basename(os.path.normpath(root)) == 'ham'):
                    main_dict[key_count_value] = file_dict, 'ham'



        return main_dict,weight_dict,key_count_value

    


dummy = num_there(fpath + "/train")

my_words,unique_word_unique_word_weight,key_count_value= dummy.tokenization()
bias = 0
temp_list=list(range(1,key_count_value+1))

for i in range (0,20):
    random.shuffle(temp_list)
    unique_word_unique_word_weight,bias = dummy.main_calculation(my_words,unique_word_unique_word_weight,bias,temp_list)

rw.write(str(bias) + "\n")

for i in unique_word_unique_word_weight:
    rw.write(i + "\t" + str(unique_word_unique_word_weight.get(i)) + "\n")

rw.close()