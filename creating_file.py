#running this on command line
Enter_the_sentence=input()
print(len(Enter_the_sentence))
Enter_the_file_name=input()
Enter_the_file_name= f'{Enter_the_file_name}.txt'

with open(Enter_the_file_name,"w") as f:
    f.write(Enter_the_sentence)
    f.close()
