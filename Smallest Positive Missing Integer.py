###################################
#smallest missing positive integer#
#         Emer Csmpbell           #
#            2018                 #
###################################

def Smallest(A):
    A.sort() #sort array in ascending order
    length = len(A)-1 #find index of last item
    smallest = 1    #smallest possible positive integer
    largest = A[length]+1  #find largest integer currently in array and add 1
  
    for i in range(smallest,largest): #loop through all positive consecutive integers from 1 to largest
                                      #item currently in list
        try:                          #check if current value of i present in list
            temp = A.index(i)            
        except:                       #if not present, i must be smallest missing integer
            return i

#code only executed if i not found - means that smallest integer must be bigger than any value currently in the array
    smallest = A[length] + 1 #find largest value in array and add one to it 
                             #(for example if array contains values 1,2,3,4,5 then missing value is 6)
    if smallest < 1: #if value found is still a negative number then smallest positive missing integer must be one
        return 1     #(for example if array contains values -5,-4,-3,-2        
    else:
        return smallest

#main program

A = [1,-2,3,6,7,9]
smallest = Smallest(A)
print('The smallest missing positive integer is ',smallest)
                   
                   
    
