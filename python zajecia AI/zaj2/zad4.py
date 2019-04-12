from treelib import Tree
import time
#
# def duplicate_node_path_check(tree, node):
#     check_node = tree.get_node(node)
#     current_node = check_node
#
#
#     while not current_node.is_root():
#         current_node = tree.parent(current_node.identifier)
#         if check_node.tag == current_node.tag:
#             return True
#     return False
def dupilcate_node_path_check(tree,node,tag):

    current_node = node


    while not current_node.is_root():
        current_node = tree.parent(current_node.identifier)
        if current_node.tag == tag:
            #print("z funkcji node.tag",node.tag)
            return True
    return False

def reachable_states(state):
    if state == "Gdansk":
        return [["Gdynia",24],["Koscierzyna",58],["Tczew",33],["Elblag",63]]

    if state == "Gdynia":
        return [["Gdansk",24],["Lebork",60],["Wladyslawowo",33]]

    if state == "Koscierzyna":
        return  [["Chojnice", 70], ["Bytów", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]]

    if state == "Tczew":
        return  [["Elblag", 53], ["Gdansk", 33], ["Koscierzyna", 59]]

    if state == "Elblag":
        return  [["Tczew", 53], ["Gdansk", 63]]

    if state == "Hel":
        return  [["Wladyslawowo", 35]]

    if state == "Wladyslawowo":
        return  [["Gdynia", 42], ["Leba", 63]]

    if state == "Leba":
        return  [["Ustka", 64], ["Lebork", 29], ["Wladyslawowo", 66]]

    if state == "Lebork":
        return  [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]]

    if state == "Ustka":
        return [["Slupsk", 21], ["Gdansk", 64]]

    if state == "Slupsk":
        return [["Ustka", 21], ["Lebork", 55], ["Bytow", 70]]

    if state == "Bytow":
        return [["Chojnice", 65], ["Koscierzyna", 40], ["Slupsk", 70]]

    if state == "Chojnice":
        return [["Bytow", 65], ["Koscierzyna", 70]]
    return []



def uniform_cost_search(start_state,target_state):
#do budowy drzewa potrzebujemy dla kazdego wierzcholka id
#bedziemy je pozniej inkrementowac

    id = 0

    #wrzucenie stanu startowego do drzewa (korzen) i kolejki

    tree = Tree()
    current_node = tree.create_node(start_state,id,data = 0)
    fifo_queue = []
    fifo_queue.append(current_node)


    #petla szukajaca sciezki do stnau koncowego
    #robimy ograniczenie na max wierzcholkow (id<200000)

    while id<200000:
        #jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego
        #drukowanie kolejki: print(fifo_queue)
        if len(fifo_queue) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1

        #jesli kolejka niepusta to wez pierwszy stan z kolejki
        fifo_queue = sorted(fifo_queue, key=lambda x: x.data)
        current_node = fifo_queue[0]
        #jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            tree.show()
            print("the target state "+str(current_node.tag)+" with id ="+str(current_node.identifier)+" has been reached after "+str(current_node.data)+" kms!")
            return 0

            #jesli stan niekoncowy to usun go z kolejki
        del(fifo_queue[0])
        #a nastepnie dodaj stany osiagalne z niego
        #na koniec kolejki i do drzewa

        for elem in reachable_states(current_node.tag):
            if dupilcate_node_path_check(tree,current_node,elem[0]) == False:
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                new_elem.data = current_node.data + elem[1]
                fifo_queue.append(new_elem)
    print("time limit exceeded")


#print(breadth_first_search("Tczew","Gdansk"))

start = time.time()
uniform_cost_search("Gdansk","Ustka")
end = time.time()
print(end - start)

#  IF
# the target state Gdynia with id = 6 has been reached!
# 0.0006566047668457031
# Switch
