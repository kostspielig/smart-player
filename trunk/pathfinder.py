#!/usr/bin/python

from priorityqueueset import PriorityQueueSet 
 
 
class PathFinder(object):
    """ Computes a path in a graph using the A* algorithm. 
     
        Initialize the object and then repeatedly compute_path to  
        get the path between a start point and an end point. 
         
        The points on a graph are required to be hashable and  
        comparable with __eq__. Other than that, they may be  
        represented as you wish, as long as the functions  
        supplied to the constructor know how to handle them.
    """
    def __init__(self, successors, move_cost, heuristic_to_goal): 
        """ Create a new PathFinder. Provided with several  
            functions that represent your graph and the costs of 
            moving through it. 
         
            successors: 
                A function that receives a point as a single  
                argument and returns a list of "successor" points, 
                the points on the graph that can be reached from 
                the given point. 
             
            move_cost: 
                A function that receives two points as arguments 
                and returns the numeric cost of moving from the  
                first to the second. 
                 
            heuristic_to_goal: 
                A function that receives a point and a goal point, 
                and returns the numeric heuristic estimation of  
                the cost of reaching the goal from the point.
        """
        self.successors = successors 
        self.move_cost = move_cost 
        self.heuristic_to_goal = heuristic_to_goal 
     

    def compute_path(self, start, goal, movType = 0, PM = 7): 
        """ Compute the path between the 'start' point and the  
            'goal' point.  
             
            The path is returned as an iterator to the points,  
            including the start and goal points themselves. 
             
            If no path was found, an empty list is returned.
        """ 
        # 
        # Implementation of the A* algorithm. 
        # 
        closed_set = {} 
         
        start_node = self._Node(start.pos, start.face) 
        start_node.g_cost = 0 
        start_node.f_cost = self._compute_f_cost(start_node, goal) 
         
        open_set = PriorityQueueSet() 
        open_set.add(start_node) 
         
        while len(open_set) > 0: 
            # Remove and get the node with the lowest f_score from  
            # the open set             
            # 
            curr_node = open_set.pop_smallest() 
            # If we reached the tarjet  Take care of END FACE 
            if curr_node.coord == goal.pos: 
                return self._reconstruct_path(curr_node) 
             
            closed_set[curr_node] = curr_node            
            for succ_coord in self.successors(curr_node.coord,movType, PM): 
                succ_node = self._Node(succ_coord) 
                (succ_node.g_cost, succ_node.face) = self._compute_g_cost(curr_node, succ_node, movType) 
                succ_node.f_cost = self._compute_f_cost(succ_node, goal) 
                          
                if succ_node in closed_set: 
                    continue 
                    
                if open_set.add(succ_node): 
                    succ_node.pred = curr_node 
         
        return [] 
 

    def compute_path_until_PM(self, start, goal, movType = 0, PM = 7): 
        """ Compute the path between the 'start' point and the  
            'goal' point.  
             
            The path is returned as an iterator to the points,  
            including the start and goal points themselves. 
             
            If no path was found, an empty list is returned.
        """ 
        # 
        # Implementation of the A* algorithm. 
        # 
        closed_set = {} 
         
        start_node = self._Node(start.pos, start.face) 
        start_node.g_cost = 0 
        start_node.f_cost = self._compute_f_cost(start_node, goal) 
         
        open_set = PriorityQueueSet() 
        open_set.add(start_node) 
         
        while len(open_set) > 0: 
            # Remove and get the node with the lowest f_score from  
            # the open set             
            # 
            curr_node = open_set.pop_smallest()
            # If we reached the tarjet  Take care of END FACE 
            if curr_node.coord == goal.pos: 
                if curr_node.face != goal.face:
                    new = self._Node(curr_node.coord, goal.face, curr_node.g_cost+abs(curr_node.face - goal.face) , 0, curr_node)
                    return self._reconstruct_path_until_PM(new, PM)
                else:
                    return self._reconstruct_path_until_PM(curr_node, PM)
                
            closed_set[curr_node] = curr_node            
            for succ_coord in self.successors(curr_node.coord,movType, PM): 
                succ_node = self._Node(succ_coord) 
                (succ_node.g_cost, succ_node.face) = self._compute_g_cost(curr_node, succ_node, movType) 
                succ_node.f_cost = self._compute_f_cost(succ_node, goal) 
                          
                if succ_node in closed_set: 
                    continue 
                    
                if open_set.add(succ_node): 
                    succ_node.pred = curr_node 
         
        return [], False, 0
 
    ########################## PRIVATE ########################## 
     
    def _compute_g_cost(self, from_node, to_node, movType = 0):
        f = Pos(from_node.coord, from_node.face)
        t = Pos(to_node.coord, to_node.face)
        m_c = self.move_cost(f, t, movType)
        return (from_node.g_cost + m_c[0], m_c[1]) 
 
    def _compute_f_cost(self, node, goal):
        x = Pos(node.coord, node.face)
        return node.g_cost + self._cost_to_goal(x, goal) 
 
    def _cost_to_goal(self, node, goal):
        return self.heuristic_to_goal(node, goal) 
 
    def _reconstruct_path(self, node): 
        """ Reconstructs the path to the node from the start node 
            (for which .pred is None)
        """
        temp = Pos(node.coord, node.face)
        pth = [temp] 
        n = node 
        while n.pred: 
            n = n.pred 
            pth.append(Pos(n.coord, n.face)) 
         
        return reversed(pth) 

    def _reconstruct_path_until_PM(self, node, PM): 
        """ Reconstructs the path to the node from the start node 
            (for which .pred is None)
        """

        can = True
        cost = 0
        pth = []
        temp = Pos(node.coord, node.face)
        if node.g_cost <= PM:
            cost = node.g_cost
            pth = [temp] 
        else:
            can = False 
            pth =[]
        n = node 
        while n.pred: 
            n = n.pred 
            if n.g_cost <= PM:
                pth.append(Pos(n.coord, n.face)) 
                if n.g_cost > cost: cost = n.g_cost
        return (list(reversed(pth)), can, cost)

    class _Node(object): 
        """ Used to represent a node on the searched graph during 
            the A* search. 
             
            Each Node has its coordinate (the point it represents), 
            a g_cost (the cumulative cost of reaching the point  
            from the start point), a f_cost (the estimated cost 
            from the start to the goal through this point) and  
            a predecessor Node (for path construction). 
             
            The Node is meant to be used inside PriorityQueueSet, 
            so it implements equality and hashinig (based on the  
            coordinate, which is assumed to be unique) and  
            comparison (based on f_cost) for sorting by cost. 
        """ 
        def __init__(self, coord, face = 0, g_cost=None, f_cost=None, pred=None): 
            self.coord = coord 
            self.g_cost = g_cost 
            self.f_cost = f_cost 
            self.pred = pred 
            self.face = face # Initially North
         
        def __eq__(self, other): 
            return self.coord == other.coord 
         
        def __cmp__(self, other): 
            return cmp(self.f_cost, other.f_cost) 
         
        def __hash__(self): 
            return hash(self.coord) 
 
        def __str__(self): 
            return 'N(%s) -> g: %s, f: %s' % (self.coord, self.g_cost, self.f_cost) 
 
        def __repr__(self): 
            return self.__str__() 
 
class Pos(object):

    def __init__(self, pos, face=0):
        self.pos = pos
        self.face = face 

    def printPos (self):
        if (self.pos[1]+1 <= 9): x = "0"+str(self.pos[1]+1)
        else: x = str(self.pos[1]+1)
        if (self.pos[0]+1 <= 9): y = "0"+str(self.pos[0]+1)
        else: y = str(self.pos[0]+1)
        return x+y

    def printFace (self):
        return self.face+1

    def __eq__(self, other): 
        return (self.pos == other.pos) and (self.face == other.face)
         
    def __cmp__(self, other): 
        return cmp(self.face, other.face) 
         
    def __hash__(self): 
        return hash(self.pos) 
 
    def __str__(self): 
        return 'N(%s, %s) -> face: %s' % (self.pos[1]+1, self.pos[0]+1, self.face+1) 
 
    def __repr__(self): 
        return self.__str__() 
 
if __name__ == "__main__": 
    from Board import Board
    import Movement

    start = 11,12
    goal = 8,10
    PM = 5

    s = Pos(start, 3)
    g = Pos(goal, 1)
    tm = Board()
    tm.readBoard("../ficheros2/manglar.sbt")

    pf = PathFinder(tm.successors, tm.move_cost, tm.heuristic_to_goal)
    
    #import time 
    #t = time.clock() 
    path = list(pf.compute_path(s, g, 1,PM)) 
    #print "Elapsed: %s" % (time.clock() - t) 

    #path2, can, cost = pf.compute_path_until_PM(s, g, 1,PM)

    print path
   # print str(can) + "cost: " + str (cost)
   # print path2
    
    print Movement.calculate_steps(path)
