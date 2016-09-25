import os
import os.path
import sys
import re
import glob


fpath = sys.argv[-1]
#fpath = "F:\\Try\\train"
x = os.getcwd()

def num_there():
    global spamCount
    global hamCount
    global fileCount_ham
    global fileCount_spam
    for root, dirs, files in os.walk(fpath):
        #path = root.split('\\')
        # print(path)
        temp = os.path.normpath(root)
        path = os.path.basename(temp)
        os.chdir(root)
        if path == 'spam':
            for file in files:
                if file.endswith(".txt"):
                    #print(file)
                    fileCount_spam += 1
                    f = open( file, 'r', encoding="latin1")
                    predicate = f.read().strip().split()
                    for line in predicate:
                        if line in dict_spam:
                            count = dict_spam[line]
                            count += 1
                            spamCount += 1
                            dict_spam[line] = count
                        else:
                            dict_ham[line] = 1
                            dict_spam[line] = 2
                            spamCount = spamCount + 2
                            hamCount = hamCount + 1
                    f.close()

        if path == 'ham':
            os.chdir(root)
            for file in files:
                if file.endswith(".txt"):
                    #print(file)
                    fileCount_ham += 1
                    f = open(file, 'r', encoding="latin1")
                    predicate = f.read().strip().split()
                    for line in predicate:
                        if line in dict_ham:
                            count = dict_ham[line]
                            count += 1
                            hamCount += 1
                            dict_ham[line] = count
                        else:
                            dict_spam[line] = 1
                            dict_ham[line] = 2
                            hamCount = hamCount + 2
                            spamCount = spamCount + 1
                    f.close()

    #print(len(dict_spam))  # dict is words
    #print(spamCount)
    #print(len(dict_ham))
    #print(hamCount)

    #print(fileCount_spam)
    #print(fileCount_ham)

    for i in dict_spam:
        count = dict_spam[i]
        count = float(count) / float(spamCount)
        dict_spam[i] = float(count)

    #print(dict_spam)

    for i in dict_ham:
        count = dict_ham[i]
        count = float(count) / float(hamCount)
        dict_ham[i] = float(count)

    #print(dict_ham)

    denominator = fileCount_spam + fileCount_ham
    spamCount = float(fileCount_spam) / float(denominator)
    hamCount = float(fileCount_ham) / float(denominator)

    
    os.chdir(x)
    rw = open('nbmodel.txt', 'w', encoding='latin1')
    rw.write(str(spamCount) + "\n")
    rw.write(str(hamCount) + "\n")
    
    for i in dict_spam:
        rw.write(i + " \t " + str(dict_spam.get(i)) + " \t " + str(dict_ham.get(i)) + "\n")
        #rw.write(i + " \t " + str(dict_ham.get(i)) + "\n")
    rw.close()


if __name__ == '__main__':
    dict_spam = {}
    dict_ham = {}
    hamCount = 0
    spamCount = 0
    fileCount_spam = 0
    fileCount_ham = 0
    num_there()
