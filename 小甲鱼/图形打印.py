'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''''
for i in range(5):
    for j in range(5):
        print("* ",end="")
    print()
        
print("^-^ "*7)

'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j ==4:
            print("* " ,end="")
        else:
            print("  ",end="")
    print()

print("^-^ "*7)


'''
* * * * *
* * * *
* * *
* *
* 
'''

for i in range(5):
    for j in range(5):
        if i+j < 5 :
            print("* ",end = "")
        
    print()
    
print("^-^ "*7)


'''
* * * * *
*     *
*   *
* *
*
'''
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or j==(4-i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("^-^ "*7)


'''
* 
* *
* * *
* * * * 
* * * * * 

'''
for i in range(5):
    for j in range(i+1):
        print("* ",end = "")
    print()

print("^-^ "*7)


'''
*
* *
*   *
*     *
* * * * * 
'''
for i in range(5):
    for j in range(5):
        if i == 4 or j == 0 or i == j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print("^-^ "*7)

'''
* * * * * 
  * * * * 
    * * * 
      * * 
        *  
'''
for i in range(5):
    for j in range(5):
        if j>=i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print("^-^ "*7)

'''
* * * * * 
  *     * 
    *   * 
      * * 
        *
'''
for i in range(5):
    for j in range(5):
        if i == 0 or j == 4 or i ==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print("^-^ "*7)


'''
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * * 
 '''
for i in range(6):
    for k in range(5-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
       
print("^-^ "*7)           
'''
     *
    * *
   *   *
  *     *
 *       *
* * * * * *
'''


for i in range(6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i+1):
        if i ==5 or k==0 or k==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
        
print("^-^ "*7)   
    
        


'''
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * *

'''
for i in range(10):
    for j in range(10):
        if i < 5:
            if  j < (10-i*2)/2 or j>= (10-(10-i*2)/2):
                print("* ",end="")
            else:
                print("  ",end="")
        else:
            if j < ((i*2 -10)/2+1) or j>= (10-((i*2 -10)/2+1)):
                print("* ",end = "")
            else:
                print("  ",end="")
        
    print()

    
print("^-^ "*7)

# 给参数就是10，不变的情况下

for i in range(10):
    for j in range(10):
        if i < 5:
            if  j < (5-i) or j>= (5+i):
                print("* ",end="")
            else:
                print("  ",end="")
        else:
            if j < (i-4) or j>= (14-i):
                print("* ",end = "")
            else:
                print("  ",end="")
        
    print()

    
print("^-^ "*7)
# 第二种

'''
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * *

'''
for i in range(5):
    for k in range(5):
        if k<=(4-i):
            print("* ",end="")
        else:
            print("  ",end="")


    for j in range(5):
        if j>=i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

for m in range(5):
    for n in range(5):
        if n<=m :
            print("* ",end="")
        else:
            print("  ",end="")
    for L in range(5):
        if L + m >= 4 :
            print("* ",end="")
        else:
            print("  ",end="")
    print()    
