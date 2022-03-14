def mazesolver(x,y,maze,vis):
    if x==len(maze)-1 and y==len(maze)-1:
        vis[x][y]=1
        return True
    if x<0 or y<0 or x>=len(maze) or y>=len(maze) or vis[x][y]==1 or maze[x][y]==0:
        return False  
    vis[x][y]=1
    if mazesolver(x-1,y,maze,vis):
        return True 
    if mazesolver(x+1,y,maze,vis):
        return True
    if mazesolver(x,y-1,maze,vis):
        return True
    if mazesolver(x,y+1,maze,vis):
        return True
    vis[x][y]=0
    return False
def mazerunner(maze):
    vis= [ [ 0 for j in range(len(maze))] for i in range(len(maze))]
    if mazesolver(0,0,maze,vis):
         printsolution(vis)
         return True
        
    else:
        return False
def printsolution( vis):
    for i in vis:
        for j in i:
            print(str(j) + " ", end ="")
        print("")           

if __name__ == "__main__":
    print(" enter the values in 0 and 1")
    
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
  

    maze = []
    
    for i in range(R):          
     a =[]
     for j in range(C):      
         a.append(int(input()))
     maze.append(a)

    if  mazerunner(maze):
       print(" path exists")
       
    else:
       print(" no path exists")    



