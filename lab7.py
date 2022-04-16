#Rebecca Glatts
#Lab 7

#Q1
#original code
inf = open('mydata.txt', 'r')
for line in inf:
    print(line)
inf.close()

#revised code
inf = open('mydata.txt', 'r')
for line in inf:
    print(line, end='')
inf.close()

"""
We can't touch

But we still reach out

We hunker down

But we still rise up

Q2: There is an extra blank line because pythons print command has a default ending of a
newline that is not shown. When the line from the file is printed, python prints that (which ends
in a new line) and then adds an extra newline because of the nature of the print command.

But we still rise up
We can't touch
But we still reach out
We hunker down
But we still rise up

Q3 (1): When opening a file to read, if the file does not exist, a 
FileNotFoundError: [Errno 2] No such file or directory: 'filename'
is created
(2): When opening a file to write, if the file does not exist, a 
io.UnsupportedOperation: not readable 
is created.
If the file exists, 


"""

#Q4
cm = 0
rainfall = open('rainfall.txt', 'r')
newfile = open('newfile.txt', 'w')
for line in rainfall:
    values = line.split()
    inches = float(values[1])
    cm = inches*2.54
    newfile.write(f"{values[0]}  {cm}\n")

rainfall.close()
newfile.close()

"""
Allison  85.4456
Alton  69.6722
AmesW  86.5378
AmesSE  86.233
Anamosa  89.73819999999999
Ankeny  84.7852
Atlantic  88.31580000000001
Audubon  85.3694
Beaconsfield  89.5858
Bedford  92.32900000000001
BellePlaine  90.9574
Bellevue  87.24900000000001
Blcokton  92.1512
Bloomfield  96.5708
Boone  92.202
Brighton  85.3186
Britt  80.1116
Buckeye  85.4964
BurlingtonKBUR  96.3676
Burlington  93.82759999999999
Carroll  84.6582
Cascade  85.0392
Daly  97.0788
Delmar  71.628

"""


#Q5
#write strings one by one, i.e. write(str)
fp=open('data1.txt', 'w')
fp.write("hello\t")
fp.write("how are you")
fp.write("\n")
fp.write("thank you ")
fp.write("bye\n")
fp.close()
#writelines(): write a sequence, i.e. a list or a tuple into a file
fp=open('data2.txt', 'w')
fp.writelines(["hello\t", "how are you", "\n", "thank you ", "bye\n"])
fp.close()

"""
data1.txt:
hello	how are you
thank you bye

data2.txt:
hello	how are you
thank you bye

The text in the files are exactly the same despite the code being different.

"""
