import numpy as np
import pandas as pd

Initial = np.loadtxt(".\Matrix.txt", delimiter=' ', dtype=np.float)
df2 = pd.DataFrame(data = Initial, index = [1,2,3,4,5,6,7], columns=[1,2,3,4,5,6,7])
df = pd.DataFrame(data = Initial, index = [1,2,3,4,5,6,7], columns=[1,2,3,4,5,6,7])
print df
#while the length of the data frame is larger than one
while len(df) >1 :
    #find the minimum value
    minval = min(df[df>0].min())
    dic = []
    list1 = []
    list2 = []
    flag = 0
    
    #merge
    for i in df:
        for j in df[i].index:
            if df[i][j] == minval:
                list1.append(i)
                list2.append(j)  
                dic.append(list1)
                dic.append(list2)
                flag = 1
        if flag == 1:
            break
    df3 = df
    #drop the columns and rows
    lable = []
    for i in dic:
        for j in i:
            lable.append(j)
            if j in df:
                df = df.drop(j, axis=0)           
                df = df.drop(j, axis=1)
    #calculate the new distance for each point to the new node
    row = []
    for i in df:
        su = 0
        ind = 0
        for j in dic:
            for p in j:
                if type(i) == str:
                    su += df3[i][p]
                else:            
                    su += df2[i][p]
        row.append(su/(len(list1)*len(list2)))
    
    #create a string for the name of the index and column
    st = ''
    for i in lable:
        st += str(i)
        
    #add column to dataframe
    df[st] = row
    #add row to dataframe
    row.append(0)
    s = pd.Series(row, index = df.columns)
    df.loc[st] = s
    print df
    print dic

