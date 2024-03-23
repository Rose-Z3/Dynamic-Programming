def knapSack(C, w, val,n): 
    
    T = [[0 for x in range(C + 1)] for x in range(n + 1)] 
     
    #Build the table of 2D
    for i in range(n + 1): 
        for j in range(C + 1): 
            if i == 0 or j == 0: 
                T[i][j] = 0
            elif w[i-1] <= j: 
                T[i][j] = max(val[i-1] + T[i-1][j-w[i-1]], T[i-1][j]) 
            else: 
                T[i][j] = T[i-1][j]
                
    picked_items = [0] * n
    total_weight = C
    for i in range(n, 0, -1):
        if T[i][total_weight] != T[i - 1][total_weight]:
            picked_items[i - 1] = 1
            total_weight -= w[i - 1]
                
        
    return T[n][C] ,picked_items
    

 
C = int(input("Enter the capacity of the knapsack: ")) #the capacity of the knapsack
N = int(input("Enter the number of available items: "))
W = []#the weights of the available items
V = []#the values of the available items
for i in range(N):
    w = int(input("Enter the weight of item "+str(i+1)+": "))
    v = int(input("Enter the value of item "+str(i+1)+": "))
    W.append(w)
    V.append(v)

max_value, picked_items= knapSack(C, W, V, N)
print("\ntotal value: ",max_value)
print("\nitems",picked_items)