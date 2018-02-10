class Leaf(object):

    def __init__(self,label):
        if label is None:
            raise ValueError      # If no value is passed, then this leaf node is horrible.
        self.label = label

class Node(object):

    def __init__(self,value,left,right):
        if value is None:
            raise ValueError      # If no value is not given, this node is invalid.

        self.value = value
        self.left  = left
        self.right = right

class RTLearner(object):

  <<init>>
  <<addEvidence>>
  <<buildTree>>
  <<query>>
