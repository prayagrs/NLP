import glob,os
import re, math
import sys

fpath = sys.argv[-1]
#fpath = "F:\\Try\\train"
dict_spam = {}

with open('nbmodel.txt','r',encoding="latin1") as f:
	probability_spam = f.readline().strip().split()[0]
	probability_ham = f.readline()#.strip().split()[1]
	#print(probability_spam)
	#print(probability_ham)

	for line in f:
		temp = line.split(' \t ')
		dict_spam[temp[0]] = [float(temp[1]), float(temp[2])] 
#print(len(dict_spam))
	
text_file = open('nboutput.txt', "w")
correctly_classified_spam = 0
predicated_classified_spam = 0
classified_spam = 0
correctly_classified_ham = 0
predicated_classified_ham = 0
classified_ham = 0
spam_file_Count = 0
ham_file_Count = 0
total = 0

for root, dirs, files in os.walk(fpath):  
	os.chdir(root)
	#print(root)
	for file in glob.glob("*.txt"):
		with open(file, "r", encoding="latin1") as f1:

			if os.path.basename(os.path.normpath(root)) == "spam":
				spam_file_Count += 1
			else:
				ham_file_Count += 1

			given_spam_probability = 0
			given_ham_probability = 0

			for line in f1:
				#line=''.join(line.splitlines())
				#print(line)
				for word in line.split():
					if word in dict_spam:
						#print(word)
						#print(dict.get(word)[0]) #probability of the word
						given_spam_probability += math.log(dict_spam.get(word)[0])
						given_ham_probability += math.log(dict_spam.get(word)[1])
						#print(given_spam_probability)

			spam_probability = given_spam_probability + math.log(float(probability_spam))
			ham_probability = given_ham_probability + math.log(float(probability_ham))

			total += 1

			if(spam_probability > ham_probability):
				text_file.write("Spam "+ os.path.join(root,file) + "\n")
				classified_spam += 1
				if(os.path.basename(os.path.normpath(root)) == "spam"):
					correctly_classified_spam += 1
				#else:
				#	predicated_classified_spam += 1
			else:
				text_file.write("Ham " + os.path.join(root,file) + "\n")
				classified_ham += 1
				if(os.path.basename(os.path.normpath(root)) == "ham"):
					correctly_classified_ham += 1
				#else:
				#	predicated_classified_ham += 1
			


spam_precision = correctly_classified_spam / classified_spam
ham_precision = correctly_classified_ham / classified_ham

spam_recall = correctly_classified_spam / spam_file_Count
ham_recall = correctly_classified_ham / ham_file_Count

spam_f1 = (2*spam_precision*spam_recall)/(spam_precision + spam_recall)
ham_f1 = (2*ham_precision*ham_recall) / (ham_precision + ham_recall)

#print(spam_precision)
#print(spam_recall)
#print(spam_f1)

#print(ham_precision)
#print(ham_recall)
#print(ham_f1)


   
text_file.close()