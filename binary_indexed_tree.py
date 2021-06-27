class BinaryIndexedTree:
    def __init__(self, n):
        """
        :param n: Size of the tree
        """
        self.tree = [0]*(n+1)
        self.n = n
    
    def update(self, index, value, array):
        while index < len(array):
            self.tree[index] += value
            index += index & -index
    
    def get_sum(self, index):
        """
	    Calculates the sum of the elements from the beginning to the index
        """
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= index & -index
        return ans
    
    def get_sum_range(self, left, right):
        """
	    Calculates the sum in range
        """
        return self.get_sum(right) - self.get_sum(left - 1)
 
    def build(self, arr): 
        """
        Builds a tree from a given array
        """
        for i in range(1, self.n+1):
            self.update(i, arr[i], arr)

        
