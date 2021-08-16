import os

wf=open("current.txt","w")
#function to rename files
os.chdir(r"C:\Users\Rashmi\Desktop\Development\one-good-project\quesbank\current")
lst= os.listdir()
ollst=[]
count=0
for i in range(len(lst)):
    ollst.append(lst[i])
    no=lst[i][-5:]
    for j in range(len(lst)):
        newno=lst[j][-5:]
        if newno==no and lst[i]!=lst[j] and lst[i][2:-5]==lst[j][2:-5] and lst[j] not in ollst:
            if lst[i].endswith(".png"):
                count+=1
                qnewname="03"+str(count)+".png"
                anewname="13"+str(count)+".png"

                os.rename(lst[i],anewname)
                os.rename(lst[j],qnewname)
                print(lst[i],"-->",anewname)
                print(lst[j],"-->",qnewname)
                wf.write(qnewname+" "+anewname+"\n")
# for filename in range(len(lst)):
    # if lst[filename].endswith(".png"):
    #     newname=""
    #     if lst[filename].startswith("q_"):
    #         newname+="03"
    #     elif lst[filename].startswith("a_"):
    #         newname+="13"
    #     newname+=str(filename)
    #     newname+=".png"

    #     os.rename(lst[filename],newname)
    #     print(lst[filename],"-->",newname)