class BinaryTree:

    try:        
        binaryTree = { #Data, level, ramifications, sonID's, FatherID, orientation.
                0 : [None, 0, 2, [1, 2],None, None],
                1 : [None, 1, 0, [None, None], 0, 'left'],
                2 : [None, 1, 0, [None, None], 0, 'right']
                }

        #Init the class
        def __init__ (self, rootData, leftData, rightData):
            BinaryTree.binaryTree[0][0] = rootData 
            BinaryTree.binaryTree[1][0] = leftData
            BinaryTree.binaryTree[2][0] = rightData
        

        #Get the root val    
        def getRootVal():
            return BinaryTree.binaryTree[0][0]

        
        #Include another node
        def includeNode(Data, orientation, position, int:fatherID):
            if fatherID not in list(BinaryTree.binaryTree.keys()):
                "Not found that father identification, use getKeys to get a list of ID's"

            if str(orientation).lower() == 'left':
                maxID = max([i for i in list(BinaryTree.binaryTree.keys()) if i % 2 != 0])
            else:
                maxID = max([i for i in list(BinaryTree.binaryTree.keys()) if i % 2 == 0])
            
            if str(position).lower() == 'right' and BinaryTree.binaryTree[fatherID][3][0] == True:
                BinaryTree.binaryTree[fatherID][3][1] = maxID + 2

            elif str(position).lower() == 'left' and BinaryTree.binaryTree[fatherID][3][1] == True:
                BinaryTree.binaryTree[fatherID][3][0] = maxID + 2 
            
            else:
                return "This node already have a descendent in this position"

            identification = maxID + 2
            flagValue = BinaryTree.binaryTree[fatherID][2]
            BinaryTree.binaryTree[fatherID][2] = flagValue + 1
            
            level = BinaryTree.binaryTree[fatherID][1] + 1
            
            BinaryTree.binaryTree[identification] = [Data,
                                                    level,
                                                    0, 
                                                    [None, None], 
                                                    fatherID, 
                                                    str(orientation).lower()]
            return "Sucesfully added"


        #Get a list of keys.
        def getKeys():
            return f"List of keys: {list(BinaryTree.binaryTree.keys())}"


        #Remove a node from the tree.
        def removeNode(nodeID):
            if BinaryTree.binaryTree[nodeID][3] != [None, None]:
                return f"The node have {len(BinaryTree.binaryTree[nodeID][3])} children's"
            elif BinaryTree.binaryTree[nodeID][3] == [None, None]:
                BinaryTree.binaryTree.pop(nodeID)
            else:
                return "Use the getKeys() function to get the node id's and try again."


        #Get the children's id from the father node.
        def getChildrens(nodeID):
            if type(NodeID) != int:
                return "Verify the nodeID and try again."
            
            else:
                return f"{BinaryTree.binaryTree[nodeID][3]}"


        #Get the data from a node using the id.
        def getNodeData(nodeID):
            if type(nodeID) != int:
                return "Verify the node id, use getKeys to get a list of node id's"
            
            elif nodeID not in list(BinaryTree.binaryTree.keys()):
                return "This node ID dosn't exist, use getKeys() method to get a list of the node id's" 
            else:
                return BinaryTree.binaryTree[nodeID][0]


        #Define the data inside the node.
        def defineNodeData(nodeID, data):
            if type(nodeID) != int and nodeID not in list(BinaryTree.binaryTree.keys()):
                return "Verify the node id, and try again. Use getKeys() to get a list of node id's"

            else:
                BinaryTree.binaryTree[nodeID][0] = data

    except Exception as E:
        return E
