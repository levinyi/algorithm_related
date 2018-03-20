#生成某区间内不重复的N个随机数的方法  
import random;  
  
#1、利用递归生成  
resultList=[];#用于存放结果的List  
A=1; #最小随机数  
B=10 #最大随机数  
COUNT=10  
  
#生成随机数的递归数学，参数counter表示当前准备要生成的第几个有效随机数  
def generateRand(counter):   
    tempInt=random.randint(A,B); # 生成一个范围内的临时随机数，  
    if(counter<=COUNT): # 先看随机数的总个数是不是够了，如果不够  
        if(tempInt not in resultList): # 再检查当前已经生成的临时随机数是不是已经存在，如果不存在  
            resultList.append(tempInt); #则将其追加到结果List中  
            counter+=1;# 然后将表示有效结果的个数加1. 请注意这里，如果临时随机数已经存在，则此if不成立，那么将直接执行16行，counter不用再加1  
        generateRand(counter); # 不管上面的if是否成立，都要递归。如果上面的临时随机数有效，则这里的conter会加1，如果上面的临时随机数已经存在了，则需要重新再生成一次随机数,counter不能变化  
generateRand(1);#调用递归函数，并给当前要生成的有效随机数的个序号置为1，因为要从第一个开始嘛  
print(resultList)# 打印结果  
  
#2、利用Python中的randomw.sample()函数实现  
resultList=random.sample(range(A,B+1),COUNT); # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。上面的方法写了那么多，其实Python一句话就完成了。  
print(resultList)# 打印结果  
#3 一行代码搞定
resultList = [random.randrange(10000) for i in range(999)]  #生成999个随机数，随机数的范围为0-10000之间。