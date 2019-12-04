# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 3

# YOUR NAME: Davit Barblishvili
# YOUR UNI: db3230

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
##### Part A (a) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
int: number  of vertices , int: number  of edges , list: sorted  list of  degrees in ascending order.
'''
def graph_properties(G):
    num_vert = G.number_of_nodes()
    num_edge = G.number_of_edges()
    degrees = [val for (node,val) in G.degree()]
    degrees.sort()


    return num_vert,num_edge, degrees
          

##### Part A (b) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if handshake theorem is true, False if handshake theorem is false
.
'''
def verify_handshake(G):
    # WRITE  YOUR  CODE  HERE
    properties = graph_properties(G);
    degrees = properties[2]
    
    sum_degrees = sum(degrees)
    num_edge = 2*(G.number_of_edges())
  
    if (sum_degrees == num_edge):
        return True
    else:
        return False
    

##### Part A (c) #####
'''
Parameters:
G: a graph object of the class networkx

Returns: no return
'''
def plot_graph(G):
    # WRITE  YOUR  CODE  HERE
    nx.draw(G)
    plt.show()
    return # No return

##### Part B (a) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if G is a true, False if not.
'''
def is_tree(G):
    # WRITE  YOUR  CODE  HERE
    is_conn = nx.is_connected(G)
    try:
        nx.find_cycle(G)
        no_cycle = False
    except:
        pass
        no_cycle = True
    
    if(no_cycle == True and is_conn == True):
        return True
    else:
        return False
    # return True #True or  False

##### Part B (b) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if e <= 3v - 6, False otherwise
'''
def verify_planar_necessary_condition(G):
    properties = [graph_properties(G)]
    num_vert = properties[0][0]     
    num_edges = properties[0][1]

    if num_vert >= 3:
        if num_edges <= 3*(num_vert) - 6:
            is_plannar = True
        else:
            is_plannar = False
    else:
        is_plannar = False
            
        
    return is_plannar

##### Part B (c) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if Eulerian, False otherwise.
'''
def is_Eulerian(G):
    # WRITE  YOUR  CODE  HERE
    is_conn = nx.is_connected(G)
    properties = [graph_properties(G)]
   
    
    degrees = properties[0][2]
   
    for num in degrees:
        if num % 2 == 0:
            is_even = True
        else:
            is_even = False
            break
    
    if is_conn == True and is_even == True:
        return True
    else:
        return False
    
        

##### Part C (a) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
int: the index of category that G1 and G2 fall into
'''
def are_isomorphic(G1, G2):
    # WRITE  YOUR  CODE  HERE  
    '''case 1 - vertices'''
    properties_G1 = graph_properties(G1)
    properties_G2 = graph_properties(G2)
    

    
    vert_G1 = properties_G1[0]
    vert_G2 = properties_G2[0]
    if vert_G1 != vert_G2:
        return 1
    
    '''case 2 - edges'''
    edge_G1 = properties_G1[1]
    edge_G2 = properties_G2[1]
    if edge_G1 != edge_G2:
        return 2
    
    '''case 3 - degrees'''
    degrees_G1 = properties_G1[2]
    degrees_G1.sort()
    
    degrees_G2 = properties_G2[2]
    degrees_G2.sort()
    
    if degrees_G1 != degrees_G2:
        return 3
    
    
    '''case 4 - adjacency'''
    G1_degrees = [val for (node,val) in G1.degree()]
    G2_degrees =[val for (node,val) in G2.degree()]
   
    if G1_degrees != G2_degrees:
        return 4
    
    
    
    '''case 5 - cycle'''
    G1_cycle = True
    G2_cycle = True
    
    try:
        nx.find_cycle(G1)
        nx.find_cycle(G2)
        G1_cycle = True
        G2_cycle = True
    except:
        pass
        G1_cycle = False
        G2_cycle = False
        
         
    if G1_cycle != G2_cycle:
        return 5
    
    
    '''case 6 - connected graphs'''
    G1_conn = nx.is_connected(G1)
    
    G2_conn = nx.is_connected(G2)
    
    if G1_conn != G2_conn:
        return 6
       
    return 7 # Index of Category the input graphs fit into

##### Part C (b) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
list: edge lists of the non-isomorphic graphs with four vertices
'''
def all_non_isomorphic_four():
    # WRITE  YOUR  CODE  HERE  
    all_edges =[]
    '''Graph 1'''
    G1 = nx.Graph()
    G1.add_node(1)
    G1.add_node(2)
    G1.add_node(3)
    G1.add_node(4)
    G1.add_edges_from([])
    G1_edges = [[]]
    all_edges.extend(G1_edges)
    
    
    '''Graph 2'''
    G2 = nx.Graph()
    G2.add_node(1)
    G2.add_node(2)
    G2.add_node(3)
    G2.add_node(4)
    G2.add_edges_from([(3,4)])
    G2_edges = [[(3,4)]]
    all_edges.extend(G2_edges)
    
    
    '''Graph 3'''
    G3 = nx.Graph()
    G3.add_node(1)
    G3.add_node(2)
    G3.add_node(3)
    G3.add_node(4)
    G3.add_edges_from([(1,2),(2,3)])
    G3_edges = [[(1,2),(2,3)]]
    all_edges.extend(G3_edges)
    
    
    '''Graph 4'''
    G4 = nx.Graph()
    G4.add_node(1)
    G4.add_node(2)
    G4.add_node(3)
    G4.add_node(4)
    G4.add_edges_from([(1,2),(3,4)])
    G4_edges = [[(1,2),(3,4)]]
    all_edges.extend(G4_edges)
    
    
    '''Graph 5'''
    G5 = nx.Graph()
    G5.add_node(1)
    G5.add_node(2)
    G5.add_node(3)
    G5.add_node(4)
    G5.add_edges_from([(1,2),(2,3),(2,4)])
    G5_edges = [[(1,2),(2,3),(2,4)]]
    all_edges.extend(G5_edges)
   
    
    '''Graph 6'''
    G6 = nx.Graph()
    G6.add_node(1)
    G6.add_node(2)
    G6.add_node(3)
    G6.add_node(4)
    G6.add_edges_from([(1,2),(2,3),(3,4)])
    G6_edges = [[(1,2),(2,3),(3,4)]]
    all_edges.extend(G6_edges)
    
    
    '''Graph 7'''
    G7 = nx.Graph()
    G7.add_node(1)
    G7.add_node(2)
    G7.add_node(3)
    G7.add_node(4)
    G7.add_edges_from([(1,2),(2,3),(3,1),(1,4),(2,4),(3,4)])
    G7_edges = [[(1,2),(2,3),(3,1),(1,4),(2,4),(3,4)]]
    all_edges.extend(G7_edges)
   
    
    
    '''Graph 8'''
    G8 = nx.Graph()
    G8.add_node(1)
    G8.add_node(2)
    G8.add_node(3)
    G8.add_node(4)
    G8.add_edges_from([(1,2),(2,3),(3,4),(4,1),(1,3)])
    G8_edges = [[(1,2),(2,3),(3,4),(4,1),(1,3)]]
    all_edges.extend(G8_edges)
    
    
    
    '''Graph 9'''
    G9 = nx.Graph()
    G9.add_node(1)
    G9.add_node(2)
    G9.add_node(3)
    G9.add_node(4)
    G9.add_edges_from([(1,2),(2,3),(3,4),(2,4)])
    G9_edges = [[(1,2),(2,3),(3,4),(2,4)]]
    all_edges.extend(G9_edges)
    
    
    
    '''Graph 10'''
    G10 = nx.Graph()
    G10.add_node(1)
    G10.add_node(2)
    G10.add_node(3)
    G10.add_node(4)
    G10.add_edges_from([(1,2),(2,3),(3,4),(4,1)])
    G10_edges = [[(1,2),(2,3),(3,4),(4,1)]]
    all_edges.extend(G10_edges)
    
    
    
    '''Graph 11'''
    G11 = nx.Graph()
    G11.add_node(1)
    G11.add_node(2)
    G11.add_node(3)
    G11.add_node(4)
    G11.add_edges_from([(1,2),(2,3),(3,1)])
    G11_edges = [[(1,2),(2,3),(3,1)]]
    all_edges.extend(G11_edges)
    
    return all_edges # edge lists of all non-isomorphic  graphs  with  four  vertices

##### Part D (a) #####
'''
Returns:
networkx.Graph object
'''
def form_G_code():
    # WRITE YOUR CODE HERE  
    '''node'''
    G_code = nx.Graph()
    G_code.add_node(graph_properties)
    G_code.add_node(verify_handshake)
    G_code.add_node(plot_graph)
    G_code.add_node(is_tree)
    G_code.add_node(verify_planar_necessary_condition)
    G_code.add_node(is_Eulerian)
    G_code.add_node(are_isomorphic)
    G_code.add_node(all_non_isomorphic_four)
    
    
    '''edges'''
    G_code.add_edges_from([(graph_properties,verify_handshake)])
    G_code.add_edges_from([(graph_properties,verify_planar_necessary_condition)])
    G_code.add_edges_from([(graph_properties,are_isomorphic)])
    G_code.add_edges_from([(graph_properties,is_Eulerian)])
    
    
    plot_graph(G_code)
   
    return G_code # a networkx Graph object


'''
G: a graph object of the class networkx

Returns:
list, boolean, boolean, boolean, boolean, boolean: a list of graph properties [vertices, edges, and degree list from part A(a)] and 5 more Boolean values
'''
def explore_graph(G):
    # WRITE YOUR CODE HERE
    '''properties'''
    properties_G_code = graph_properties(G)
    
    '''is tree'''
    is_tree_G = is_tree(G)
    
    '''is Eulerian'''
    is_eulerian_G = is_Eulerian(G)
    
    
    '''is connected'''
    is_connected_G = nx.is_connected(G)
    
    
    '''cycle'''
    try:
        nx.find_cycle(G)
      
        G_code_cycle = True
   
    except:
        pass
        G_code_cycle= False
        
        
        
    '''planar necessary condition'''
    is_planar_G_code = verify_planar_necessary_condition(G)
    
    
     
   
    
    return properties_G_code, is_tree_G,is_eulerian_G,is_connected_G,G_code_cycle,is_planar_G_code

 

### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
if __name__ == '__main__':
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (2, 6)])
    G2 = nx.Graph()
    G2.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (3, 6)])
    K_5 = nx.complete_graph(5)
    K_3_5 = nx.complete_bipartite_graph(3, 5)
    planar_graph = nx.dodecahedral_graph()

    print("#######################################")
    print("Welcome to Coding 3: Graph Theory!")
    print("#######################################")
    print()
    
    print("---------------------------------------")
    print("PART A: Basics in Graph theory")
    print("---------------------------------------")
    print("Part (a)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = graph_properties(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", (6, 5, [1, 1, 1, 2, 2, 3]))
    print()
    print("Test Case 2: ")
    student_ans_2 = graph_properties(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", (5, 10, [4, 4, 4, 4, 4]))
    print("---------------------------------------")

    print("Part (b)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = verify_handshake(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", True)
    print()
    print("Test Case 2: ")
    student_ans_2 = verify_handshake(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", True)
    print("---------------------------------------")

    print("Part (c)")
    print("---------------------------------------")
    print("Test Case 1: ")
    plot_graph(G2)
    

    print()
    print("Test Case 2: ")
    plot_graph(K_5)
    print("---------------------------------------")
    
    print("---------------------------------------")
    print("PART B: Cycle, Connectivity and Special graphs")
    print("---------------------------------------")
    print("Part (a)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = is_tree(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", True)
    print()
    print("Test Case 2: ")
    student_ans_2 = is_tree(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", False)
    print("---------------------------------------")

    print("Part (b)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = verify_planar_necessary_condition(planar_graph)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", True)
    print()
    print("Test Case 2: ")
    student_ans_2 = verify_planar_necessary_condition(G1)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", True)
    print("---------------------------------------")

    print("Part (c)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = is_Eulerian(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", False)
    print()
    print("Test Case 2: ")
    student_ans_2 = is_Eulerian(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", True)
    print("---------------------------------------")

    
    print("---------------------------------------")
    print("PART C: Isomorphism")
    print("---------------------------------------")
    print("Part (a)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = are_isomorphic(G1, G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", 7)
    print()
    print("Test Case 2: ")
    student_ans_2 = are_isomorphic(G1, G2)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", 4)
    print("---------------------------------------")

    print("Part (b)")
    print("---------------------------------------")
    print(all_non_isomorphic_four())
    print("---------------------------------------")
    
    print("---------------------------------------")
    print("PART D: Your code is a graph")
    print("---------------------------------------")
    print("Part (a)")
    G_code = form_G_code()
    print("---------------------------------------")
    print("Part (b)")
    print("---------------------------------------")
    print(explore_graph(G_code))