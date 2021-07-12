
#Wish your peers Ram Navmi in this unique way..


for i in range(3):
    for j in range(i+1):
        print("*", end=" ")
    print()

        
        

             
for i in range(5):
    for j in range(i+1):
         print("*", end=" ")
        #if(j==0 or j==i or i==7):
            #print("*", end=" ")
            
        #else:
            #print(" ", end=" ")
        
    print()    
    
for i in range(5):
    print("*")
  

str="";    
for Row in range(0,6):    
    for Col in range(0,7):     
        if (Col == 1 or ((Row == 0 or Row == 3) and Col > 1 and Col < 5) or (Col == 5 and Row != 0 and Row < 3) or (Col == Row - 1 and Row > 2)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str); 

result_str="";    
for row in range(0,5):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);    

result_str="";    
for row in range(0,5):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            result_str=result_str+"* "    
        else:      
            result_str=result_str+"  "    
    result_str=result_str+"\n"    
print(result_str);  





##OUTPUT:

* 
* * 
* * * 
* 
* * 
* * * 
* * * * 
* * * * * 
*
*
*
*
*
 ****  
 *   * 
 *   * 
 ****  
 * *   
 *  *  

  ***  
 *   * 
 *   * 
 ***** 
 *   * 

  *       *   
  *       *   
  * *   * *   
  *   *   *   
  *       *   
       
        
