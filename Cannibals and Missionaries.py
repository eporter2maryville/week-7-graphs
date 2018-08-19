# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 7.1 Cannibals and Missionaries

#starting counts

counts =[(3,3,1),(3,2,1),(2,2,1),(2,2,0),(2,1,1),(2,2,0),(1,1,1),(1,1,0),(0,1,0),(0,1,1)]


class bankCounts():
    def __init__(self, missionaries, cannibals, boat):
        self.cann = cannibals
        self.miss = missionaries
        self.boat = boat
        
    def is_goal(self,miss,cann,boat):
        if self.cann == 0 and self.miss == 0:
            return True
        else:
            return False

    def is_valid(self,miss,cann,boat):
        if self.miss >= self.cann or self.miss == 0 or self.cann == 0:
            return True
        else:
            return False


from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def buildGraph(counts):
    d = {'miss':(3,2,1,0),'cann':(3,2,1,0),'boat':(1,0)}
    g = Graph()
    counts = counts
    # add vertices and edges for carying counts on the initial beach
    for counts in d.keys():
        for state1 in d[counts]:
            for state2 in d[counts]:
                if state1 != state2:
                    g.addEdge(state1,state2)
    return g

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')
    
def main():
    start = bankCounts(3,3,1) #The list contains the left bank counts for missionaries, cannibals, and the boat in that order
    goal = bankCounts(0,0,0)
    validTest=start.is_valid(3,3,1)
    print(validTest)
    vertex = Vertex(start)
    graph=buildGraph(counts)
    print(graph.getVertices)
    breadthFirstSearch=bfs(graph,vertex)

main()