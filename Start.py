from ast import For
from email.mime import image



class Solution(object):
     
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)
                
        

        
        dfs(sr, sc)
        return image
    """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

    
    
  
image=[[1,1,1],
       [1,1,0],
       [1,0,1]]

for x in image:
            print (x)

lis=Solution()
a=int(input())
b=int(input())
c=int(input())

lis.floodFill(image,a,b,c)            


for x in image:
            print (x)

            
