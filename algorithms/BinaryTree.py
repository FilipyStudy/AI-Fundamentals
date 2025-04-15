class BinaryTree:
    
    binaryTree = { #Data, level, ramifications, sonID's, FatherID, orientation.
            0 : [None, 0, 2, [1, 2],None, None],
            1 : [None, 1, None, [None, None], 0, 'left'],
            2 : [None, 1, None, [None, None], 0, 'right']
            }

    def __init__ (self, rootData, leftData, rightData):
        BinaryTree.binaryTree[0][0] = rootData 
        BinaryTree.binaryTree[1][0] = leftData
        BinaryTree.binaryTree[2][0] = rightData
    
        
    def getRootVal(self):
        return BinaryTree.binaryTree[0][0]


    def includeNode(self, Data, orientation, position, fatherID):
        if fatherID not in list(BinaryTree.binaryTree.keys()):
            print("Not found that father identification, use getKeys to get a list of ID's")

        if orientation.lower() == 'left':
            maxID = max([i for i in list(BinaryTree.binaryTree.keys()) if i % 2 != 0])
        else:
            maxID = max([i for i in list(BinaryTree.binaryTree.keys()) if i % 2 == 0])
        
        if str(position).lower() == 'right':
            BinaryTree.binaryTree[fatherID][3][1] = maxID + 1
        else:
            BinaryTree.binaryTree[fatherID][3][0] = maxID + 1 
        
        identification = maxID + 1
        flagValue = BinaryTree.binaryTree[fatherID][2]
        BinaryTree.binaryTree[fatherID][2] = flagValue + 1
        
        level = BinaryTree.binaryTree[fatherID][1] + 1
        
        BinaryTree.binaryTree.update({identification : [Data,
                                                   level,
                                                   None, 
                                                   [None, None], 
                                                   fatherID, 
                                                   str(orientation).lower()]})
        return "Sucesfully added"


    def getKeys(self):
        return f"List of keys: {BinaryTree.binaryTree.keys()}"
