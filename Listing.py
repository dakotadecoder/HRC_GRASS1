#import the os module so that you can call the listdir and path.join functionality
import grass.script as gscript
import os



#set this variable equal to the path to the directory that the ascii files are in, depends on the user

directory = 'E:\HRC_Water\Task7\ASCII_DEM_2'

list1 = []
for filename in os.listdir(directory):

        if filename.endswith(".asc"):

                def funb():

                    b =  os.path.join(directory, filename) 

                    list1.append(b)

                funb()



        else:

            continue




#for loop that iterates over every file in the directory variable



for filename in os.listdir(directory):



#operates on only .asc files



        if filename.endswith(".asc"):



#define the variable which will be used for the r.n.ascii input 



                c = ("'" + os.path.join(directory, filename) + "'")



                for c in list1:



#create the function which runs r.in.ascii so that the output can recieve a new name for each iteration



                        def func():



#specify the variable that will be used for the output, truncates the c variable from character 40-48



#this range needs to be defined depending on the specific path name that is specific in list1



                            u = c[69:77]    



#calling grass functionality to run r.n.ascii



                            gscript.run_command('r.in.ascii', input = c , output = u)



#running the function



                        func()



        else:



            continue







