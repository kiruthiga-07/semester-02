#1
word1=input("Enter the first string: ")#abc
word2=input("Enter the first string: ")#def
def merged_string(word1,word2):
    merged=[]
    length1,length2=len(word1),len(word2)
    max_length=max(length1,length2)
    for i in range(max_length):
        if i<length1:
            merged.append(word1[i])
        if i<length2:
            merged.append(word2[i])
    return ''.join(merged)
print("Merged String:",merged_string(word1,word2))


#2
flowerbed=[1,0,0,0,1]
num=int(input())
count=0
length=len(flowerbed)
i=0
while i<length:
    if flowerbed[i]==0:
        pre_emp=(i==0)or(flowerbed[i-1]==0)
        nxt_emp=(i==length-1)or(flowerbed[i+1]==0)
        if pre_emp and nxt_emp:
            flowerbed[i]=1
            count+=1
        if count>=num:
            print(True)
            break
    i+=1
if count<num:
    print(False)
            
