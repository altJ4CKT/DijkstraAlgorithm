# visited  Node, cost from start, Previous Node
# The node is the KEY, see example below
visited =  {
              'A':[0, None],
              'B':[5, 'A'],
              'C':[8, 'A'],
              'D':[9, 'C'],
              'E':[11, 'D']
              }
node = input(" Enter a node  ")

print (visited[node]) # prints cost from start and previous node

print(visited[node][0])  # prints the cost from start 

print(visited[node][1])   # prints the previous Node   
##
##
### similarly, univisited can be represented using graph, here is an example: at the start we set all nodes costs to infinity
### 9999 is used to represent infinity 
## This is how you start the list of unvisited nodes:
unvisited =  {
              'A':[0   , None],
              'B':[9999, None],
              'C':[9999, None],
              'D':[9999, None],
              'E':[9999, None]
              }
print (unvisited)
print()
print()

# challenge 
# write line of code to update node C on the unvisited list  with Cost = 5 and Previous node to A
unvisited['C'] = [5, 'A']

# write another code to update the other nodes.
unvisited['B'] = [8, 'A']
unvisited['D'] = [7, 'C']
unvisited['E'] = [10, 'D']

print("Updated unvisited list:")
print(unvisited)
