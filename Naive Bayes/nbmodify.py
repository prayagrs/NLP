import os
import os.path
import sys
import re
import glob


fpath = sys.argv[-1]
x = os.getcwd()

punc = [',', '.', '{', '}', '(', ')', '!', '"', '@', '#', '$', '%', '^', '&', '*', ':', ';', '/', '?', '<', '>', '=', '+','1','2','3','4','5','6','7','8','9','0']
stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
            'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
            'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't",
            'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each',
            'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't",
            'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
            'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is',
            "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself',
            'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves',
            'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than',
            'that', "that's", 'the', 'their','theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this',
            'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've",
            'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why',
            "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves',
            'one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']


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
                        line = ''.join(ch for ch in line if ch not in punc) # for every character in line
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
                        line = ''.join(ch for ch in line if ch not in punc) # for every character in line
                    
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
