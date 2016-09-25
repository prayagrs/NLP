The goal of this assignment is to get some experience implementing the simple but effective machine
learning technique, Naïve Bayes classification, and applying it to a binary text classification task (i.e.,
spam detection). This assignment will describe the details of a particular implementation of a Naïve
Bayes classifier with the categories spam and ham (i.e., not spam).


nblearn.py will learn a naive Bayes model from labeled data, and nbclassify.py will use the model to classify new data.

python3 nblearn.py /path/to/input

The argument is a data directory. The script should search through the directory recursively looking for
subdirectories containing the folders: "ham" and "spam". Note that there can be multiple "ham" and
"spam" folders in the data directory. Emails are stored in files with the extension ".txt" under these
directories.

"ham" and "spam" folders contain emails failing into the category of the folder name (i.e., a spam folder
will contain only spam emails and a ham folder will contain only ham emails). Each email is stored in a
separate text file. The emails have been preprocessed removing HTML tags, and leaving only the body
and the subject. The files have been tokenized such that white space always separates tokens. Note, in
the subject line, "Subject:" is considered as one token. Because of special characters in the corpus, you
should use the following command to read files:

open(filename, "r", encoding="latin1")

nblearn.py will learn a naive Bayes model from the training data, and write the model parameters to a
file called nbmodel.txt



you should search the directory for files with the extension ".txt". nbclassify.py
should read the parameters of a naive Bayes model from the file nbmodel.txt, and classify each ".txt" file
in the data directory as "ham" or "spam", and write the result to a text file called nboutput.txt
