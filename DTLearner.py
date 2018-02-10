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

  def __init__(self, leaf_size):
  
      if leaf_size is None:
         leaf_size = 1
      self.dataX = None                 # Training data is initially nothing
      self.dataY = None                 # Training data is initially nothing
      self.leaf_size = leaf_size
  def addEvidence(self,dataX,dataY):
       # Take the old data you already have and add the new data to that.
      self.dataX = mergeData(self.dataX, dataX)
      self.dataY = mergeData(self.dataY, dataY)
  
       # The old decision tree is no longer valid. make a new tree.
      self.random_tree = self.build_tree(self.dataX, self.dataY)
  
      
      def mergeData(oldData, newData):
          # Append new data to old data.
          return np.append(oldData, newData) if oldData else newData
          # TODO then prune out values that are not unique. np.unique doesn't seem to work as expected...
          #return np.unique(np.append(oldData, newData) if oldData else newData)
  def buildTree(self, dataX, dataY):
      self.tree = build_tree_helper(dataX,dataY)
  
  
  def build_tree_helper(self, dataX, dataY):
      # TODO check shape of both X andy Y?
      # Return leaf if:
      # 1. There is only one element left.
      # 2. There is less than or equal to the given leaf size elements.
      # 3. All remaining Y values are the same.
      if dataX.shape[0] == 1 or dataX.shape[0] <= self.leaf_size or all(dataY[0] == y for y in dataY):
          yMean = dataY.mean()
          return Leaf(ymean)
         # Determine random feature i to split on.
  
      i =  np.random.randint(dataX.shape[1])
       # Select 2 random values from ith feature.
      a = np.random.randint(dataX.shape[0])
      b = np.random.randint(dataX.shape[0])
  
  
      # Take avergage of the 2 randomly selected values.
      split_value = (dataX[a,i] + dataX[b,i]) / 2
  
      # Build left tree such that we pass it data that's less than or equal to the split value.
      # li is a set of boolean values that are true if the condition below is true. Think like Matlab
      li = dataX[:,i] < split_value
      left_tree = self.build_tree_helper(dataX[li,:], dataY[li])
      # Build left tree such that we pass it data that's greater than the split value.
      ri = dataX[:,i] > split_value
      right_tree = self.build_tree_helper(dataX[ri,:], dataY[ri])
      
       return Node(value = split_value,
                  left = left_tree,
                  right = right_tree)
  def query(self,questions):
  
      # Get a value for each point given.
      results = []
  
      for i in range(0, questions.shape[0]):
          results.append(self.queryHelper(question[i]))
  
      # Convert and return.
      return np.array(results)
  
  
  
  def queryHelper(self,node,questionValue):
  
      if isinstance(node,Leaf):
        return node.label
  
      if questionValue > node.value:
          queryHelper(node.right,questionValue)
      else: queryHelper(node.left,questionValue)
