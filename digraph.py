from arc import*
from linked import*
from bstnode import*

class Digraph:

    def __init__(self):
        """
        Digraph() produces a new empty directed graph.
        Effects: Creates a new Digraph.
        __init__: -> Digraph

        """
        self._arcs = None
        self._vertices = None

    def find_arc_node(self, tail, head):
        """
        self.find_arc_node(tail, head) produces the 
            Double containing the arc with tail ID tail
            and head ID head.
        find_arc_node: Digraph Str Str -> Double
        Requires: tail and head are IDs of the tail
                  and head of an arc in self

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                return double
            else:
                # if not check for next double
                double = double.next()
        return "find_arc_node error"
        
        


    def find_vertex_node(self, ID):
        """
        self.find_vertex_node(ID) produces the BSTNode
            containing the vertex with ID ID.
        find_vertex_node: Digraph Str -> BSTNode
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # return the node if equals
                return node
        return "find_vertex_node error"


    
                
    def vertex_value(self, ID):
        """
        self.vertex_value(ID) produces the value of the 
            vertex with ID ID.
        vertex_value: Digraph Str -> Any
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # return the value of node if ID equals
                return node.access_value()
        return "vertex_value error"


    def vertex_weight(self, ID):
        """
        self.vertex_weight(ID) produces the weight of the 
            vertex with ID ID.
        vertex_weight: Digraph Str -> Int
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # return the weight of node if ID equals
                return node.access_weight()
        return "vertex_weight error"
        

    def vertex_colour(self, ID):
        """
        self.vertex_colour(ID) produces the colour of the 
            vertex with ID ID.
        vertex_colour: Digraph Str -> Str
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # return the colour of node if ID equals
                return node.colour_value()
        return "vertex_colour error"


    def arc_value(self, tail, head):
        """
        self.arc_value(tail, head) produces the value of the 
            arc with tail ID tail and head ID head.
        arc_value: Digraph Str Str -> Any
        Requires: tail and head are IDs of the tail
                  and head of an arc in self

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                return arc.arc_value()
            else:
                # if not check for next double
                double = double.next()
        return "arc_value error"


    def arc_weight(self, tail, head):
        """
        self.arc_weight(tail, head) produces the weight of the 
            arc with tail ID tail and head ID head.
        arc_weight: Digraph Str Str -> Int
        Requires: tail and head are IDs of the tail
                  and head of an arc in self

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                return arc.arc_weight()
            else:
                # if not check for next double
                double = double.next()
        return "arc_weight error"

    def arc_colour(self, tail, head):
        """
        self.arc_colour(tail, head) produces the colour of the 
            arc with tail ID tail and head ID head.
        arc_colour: Digraph Str Str -> Str
        Requires: tail and head are IDs of the tail
                  and head of an arc in self

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                return arc.arc_colour()
            else:
                # if not check for next double
                double = double.next()
        return "arc_colour error"

    
    def in_neighbours(self, one):
        """
        self.in_neighbours produces a list containing
            IDs of the in-neighbours of the vertex with
            ID one.
        in_neighbours: Digraph Str -> (listof Str)
        Requires: ID is the ID of a vertex in self

        """
        # initial the double with current arcs 
        Double = self._arcs
        # initial an empty list
        list_in = []
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            if arc.arc_head() == one :
                list_in.append(arc.arc_tail())
            else:
                # if not check for next double
                double = double.next()
                # the loop would end when the first literation end 
                if double == self._arcs :
                    break
        return list_in




    def out_neighbours(self, one):
        """
        self.out_neighbours produces a list containing
            IDs of the out-neighbours of the vertex with
            ID one.
        in_neighbours: Digraph Str -> (listof Str)
        Requires: ID is the ID of a vertex in self

        """
         # initial the double with current arcs 
        Double = self._arcs
        # initial an empty list
        list_out = []
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            if arc.arc_tail() == one :
                list_out.append(arc.arc_head())
            else:
                # if not check for next double
                double = double.next()
                # the loop would end when the first literation end 
                if double == self._arcs :
                    break
        return list_out

    def is_arc(self, tail, head):
        """
        self.is_arc(tail, head) produces True if self contains
            an arc with tail tail and head head and False
            otherwise.
        is_arc: Digraph Str Str -> Bool
      
        """
        # initial the double with current arcs 
        double = self._arcs
        # special situation
        if double == None :
               return False
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                return True
            else:
                # if not check for next double
                double = double.next()
                # the loop would end when the first literation end 
                if double == self._arcs :
                    break
        return False
        
    def set_vertex_value(self, ID, new):
        """
        self.set_vertex_value(ID) changes the value of 
            the vertex with ID ID to new.
        Effects: Mutates self by changing the value of
            the vertex with ID ID to new.            
        set_vertex_value: Digraph Str Any -> None
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # change the value to new if we find the correct self
                node.store_value(new)
                break
        return "set_vertex_value error"


    def set_vertex_weight(self, ID, new):
        """
        self.set_vertex_weight(ID) changes the weight of 
            the vertex with ID ID to new.
        Effects: Mutates self by changing the weight of
            the vertex with ID ID to new.            
        set_vertex_weight: Digraph Str Int -> None
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # change the weight to new if we find the correct self
                node.store_weight(new)
                break
        return "set_vertex_weight error"

    def set_vertex_colour(self, ID, new):
        """
        self.set_vertex_colour(ID) changes the colour of 
            the vertex with ID ID to new.
        Effects: Mutates self by changing the colour of
            the vertex with ID ID to new.            
        set_vertex_colour: Digraph Str Str -> None
        Requires: ID is the ID of a vertex in self

        """
        # initial the node with current vertice
        node = self._vertices
        # recursion to find the location
        while node != None:
            # get node id
            node_ID = node.access_ID()
            # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                node = node.access_right()
            elif node_ID > ID:
                node = node.access_left()
            else:
                # change the colour to new if we find the correct self
                node.store_colour(new)
                break
        return "set_vertex_colour error"

    def set_arc_value(self, tail, head, new):
        """
        self.set_arc_value(tail, head, new) changes 
            the value of the arc with tail ID tail
            and head ID head to new.
        Effects: Mutates self by changing the value
            of the arc with tail ID tail and head
            ID head to new.
        set_arc_value: Digraph Str Str Any -> None

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                # change the value to new if we find the arc
                arc.arc_change_value(new)
                break
            else:
                # if not check for next double
                double = double.next()
        return "set_arc_value error"

    def set_arc_weight(self, tail, head, new):
        """
        self.set_arc_weight(tail, head, new) changes 
            the weight of the arc with tail ID tail
            and head ID head to new.
        Effects: Mutates self by changing the weight
            of the arc with tail ID tail and head
            ID head to new.
        set_arc_weight: Digraph Str Str Int -> None

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                # change the weight to new if we find the arc
                arc.arc_change_weight(new)
                break
            else:
                # if not check for next double
                double = double.next()
        return "set_arc_weight error"
        
    def set_arc_colour(self, tail, head, new):
        """
        self.set_arc_colour(tail, head, new) changes 
            the colour of the arc with tail ID tail
            and head ID head to new.
        Effects: Mutates self by changing the colour
            of the arc with tail ID tail and head
            ID head to new.
        set_arc_colour: Digraph Str Str Str -> None

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                # change the colour to new if we find the arc
                arc.arc_change_colour(new)
                break
            else:
                # if not check for next double
                double = double.next()
        return "set_arc_colour error"

    def add_vertex(self, ID, value=0, weight=0, colour="white"):
        """
        self.add_vertex(ID, weight, colour) adds a new
            vertex with specified ID, weight, and colour.
        Effects: Mutates self by adding a new vertex.
        add_vertex: Digraph Str Any Int Str -> None
        Requires: self does not contain a vertex with
                      ID ID

        """
        # new vertex
        vertex = BSTNode(ID, value, weight, colour, None, None, None)
        node = self._vertices
        # special situation
        if node == None :
            self._vertices = vertex
            vertex._parent = vertex
            return
        # loop to get the right position to add vertex 
        while node != None :
            node_ID = node.access_ID()
             # if ID less than node id, next node is left node, vice versa
            if node_ID < ID :
                # if right node is empty we can directly link the vertex
                if node.access_right() == None :
                    node.link_right(vertex)
                    vertex.link_parent(node)
                    return
                else:
                    # if not we would check for the right child of the node
                    node = node.access_right()
            elif node_ID > ID:
                # if left node is empty we can directly link the vertex
                if node.access_left() == None :
                    node.link_left(vertex)
                    vertex.link_parent(node)
                    return
                else:
                    # if not we would check for the left child of the node
                    node = node.access_left()
            else:
                return "add_vertex error"


    def add_arc(self, tail, head, value = 0, weight = 0,
                colour = "white"):
        """
        self.add_arc(self, tail, head, value, weight, colour)
            produces a new arc with specified tail, head,
            value, weight, and colour.
        Effects: Mutates self by adding a new arc.
        add_arc: Digraph Str Str Any Int Str -> None
        Requires: head and tail are IDs of vertices in 
                  self

        """
        # new arc
        arc = Arc(tail, head, value, weight, colour)
        # new double which contain new arc
        double = Double(arc, None, None)
        # special situation
        if self._arcs == None:
            self._arcs = double
        else :
            #link prev and next
            self._arcs.link_prev(double)
            double.link_next(self._arcs)
            self._arcs = double
            

        
        

    def delete_arc(self, tail, head):
        """
        self.delete_arc(self, tail, head) deletes the arc
            with tail ID tail and head ID head.
        Effects: Mutates self by deleting an arc.
        delete_arc: Digraph Str Str -> None
        Requires: head and tail are head and tail of
                  an arc in self

        """
        # initial the double with current arcs 
        double = self._arcs
        # recursion to find the location
        while double != None :
            # get arc
            arc = double.access()
            # check if this double contains arc with tail and head
            if(arc.arc_tail() == tail and arc.arc_head() == head):
                # get the prev and nect
                prev = double.prev()
                next = double.next()
                # special situation
                if(prev == None):
                    self._arcs = next
                    self._arcs.link_prev(None)
                else :
                    prev.link_next(next)
                    # in next is not empty, then link to prev
                    if(next != None):
                        next.link_prev(prev)
            else:
                # if not check for next double
                double = double.next()
        return "delete_arc error"
