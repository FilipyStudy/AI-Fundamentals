#### BinaryTree class documentation:

##### getRootVal()
Return the data inside the root node. The type of this value depends on the value implemented by the user.

##### includeNode(Data, orientation, position, fatherID)
Include a node, the data type is defined by the user.


* Data: * Defined by the user, but using python, the user can use various types on the tree.
* orientation: * is about the node side.
* position: * Position in the Father node.
* fatherID: * Father identification.

##### getKeys()
Get a list of the node id's.

##### removeNode(nodeID)
Remove a node if he dosn't have any children.

##### getChildrens(nodeID)
Return a list containing the children's id's of this node. If this node dosn't have any children, a list containing two None values is returned.

##### getNodeData(nodeID)
Return the data inside the node specified by the user.

##### defineNodeData(nodeID, data)
Define the data of the node specified by the user.