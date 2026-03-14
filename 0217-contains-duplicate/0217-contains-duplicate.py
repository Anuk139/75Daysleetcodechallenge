class Solution(object):
        def containsDuplicate(self,num):
            n=set() 
            for i in num:
               if i in n:
                  return True
               else:
                  n. add(i) 
               
            return False