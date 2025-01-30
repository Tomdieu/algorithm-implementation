import unittest
from algorithms import (
    binary_search,
    Graph,
    knapsack,
    merge_intervals,
    kadane
)

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test fixtures."""
        # Create a graph for testing
        self.test_graph = Graph()
        self.test_graph.add_edge(0, 1)
        self.test_graph.add_edge(0, 2)
        self.test_graph.add_edge(1, 2)
        self.test_graph.add_edge(2, 3)

    def test_binary_search(self):
        """Test binary search with various scenarios."""
        # Test case 1: Normal search
        arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr1, 7), 6)
        
        # Test case 2: Element at start
        self.assertEqual(binary_search(arr1, 1), 0)
        
        # Test case 3: Element at end
        self.assertEqual(binary_search(arr1, 10), 9)
        
        # Test case 4: Element not in array
        self.assertEqual(binary_search(arr1, 11), -1)
        
        # Test case 5: Empty array
        self.assertEqual(binary_search([], 1), -1)
        
        # Test case 6: Single element array
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)

    def test_graph_bfs(self):
        """Test breadth-first search traversal."""
        # Test case 1: Normal BFS from start node
        self.assertEqual(self.test_graph.bfs(0), [0, 1, 2, 3])
        
        # Test case 2: BFS from middle node
        self.assertEqual(self.test_graph.bfs(1), [1, 0, 2, 3])
        
        # Test case 3: BFS from end node
        self.assertEqual(self.test_graph.bfs(3), [3, 2, 0, 1])

    def test_graph_dfs(self):
        """Test depth-first search traversal."""
        # Test case 1: Normal DFS from start node
        self.assertEqual(self.test_graph.dfs(0), [0, 1, 2, 3])
        
        # Test case 2: DFS from middle node
        result = self.test_graph.dfs(1)
        self.assertTrue(all(x in result for x in [0, 1, 2, 3]))
        
        # Test case 3: DFS from end node
        result = self.test_graph.dfs(3)
        self.assertTrue(all(x in result for x in [0, 1, 2, 3]))

    def test_graph_connectivity(self):
        """Test graph connectivity checking."""
        # Test case 1: Direct connection
        connected, path = self.test_graph.is_connected(0, 1)
        self.assertTrue(connected)
        self.assertEqual(path, [0, 1])
        
        # Test case 2: Indirect connection
        connected, path = self.test_graph.is_connected(0, 3)
        self.assertTrue(connected)
        self.assertEqual(path, [0, 2, 3])
        
        # Test case 3: Same node
        connected, path = self.test_graph.is_connected(1, 1)
        self.assertTrue(connected)
        self.assertEqual(path, [1])
        
        # Test case 4: Disconnected nodes (create new disconnected node)
        self.test_graph.graph[4] = []
        connected, path = self.test_graph.is_connected(0, 4)
        self.assertFalse(connected)
        self.assertEqual(path, [])

    def test_knapsack(self):
        """Test knapsack problem with various scenarios."""
        # Test case 1: Normal case
        values1 = [60, 100, 120]
        weights1 = [10, 20, 30]
        capacity1 = 50
        max_value, selected = knapsack(values1, weights1, capacity1)
        self.assertEqual(max_value, 220)
        self.assertFalse(all(x in selected for x in [0, 1]))
        
        # Test case 2: No items fit
        values2 = [60, 100, 120]
        weights2 = [10, 20, 30]
        capacity2 = 5
        max_value, selected = knapsack(values2, weights2, capacity2)
        self.assertEqual(max_value, 0)
        self.assertEqual(selected, [])
        
        # Test case 3: All items fit
        values3 = [60, 100, 120]
        weights3 = [10, 20, 30]
        capacity3 = 60
        max_value, selected = knapsack(values3, weights3, capacity3)
        self.assertEqual(max_value, 280)
        self.assertTrue(all(x in selected for x in [0, 1, 2]))
        
        # Test case 4: Single item
        values4 = [60]
        weights4 = [10]
        capacity4 = 15
        max_value, selected = knapsack(values4, weights4, capacity4)
        self.assertEqual(max_value, 60)
        self.assertEqual(selected, [0])

    def test_merge_intervals(self):
        """Test merging intervals with various scenarios."""
        # Test case 1: Normal overlapping intervals
        intervals1 = [(1, 3), (2, 6), (8, 10), (15, 18)]
        expected1 = [(1, 6), (8, 10), (15, 18)]
        self.assertEqual(merge_intervals(intervals1), expected1)
        
        # Test case 2: No overlapping intervals
        intervals2 = [(1, 2), (3, 4), (5, 6)]
        expected2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(merge_intervals(intervals2), expected2)
        
        # Test case 3: All overlapping intervals
        intervals3 = [(1, 5), (2, 6), (3, 7), (4, 8)]
        expected3 = [(1, 8)]
        self.assertEqual(merge_intervals(intervals3), expected3)
        
        # Test case 4: Empty list
        self.assertEqual(merge_intervals([]), [])
        
        # Test case 5: Single interval
        intervals5 = [(1, 2)]
        self.assertEqual(merge_intervals(intervals5), [(1, 2)])
        
        # Test case 6: Touching intervals
        intervals6 = [(1, 2), (2, 3), (3, 4)]
        expected6 = [(1, 4)]
        self.assertEqual(merge_intervals(intervals6), expected6)

    def test_kadane(self):
        """Test Kadane's algorithm with various scenarios."""
        # Test case 1: Normal case with mixed numbers
        arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        max_sum, subarray = kadane(arr1)
        self.assertEqual(max_sum, 6)
        self.assertEqual(subarray, [4, -1, 2, 1])
        
        # Test case 2: All positive numbers
        arr2 = [1, 2, 3, 4]
        max_sum, subarray = kadane(arr2)
        self.assertEqual(max_sum, 10)
        self.assertEqual(subarray, [1, 2, 3, 4])
        
        # Test case 3: All negative numbers
        arr3 = [-1, -2, -3, -4]
        max_sum, subarray = kadane(arr3)
        self.assertEqual(max_sum, -1)
        self.assertEqual(subarray, [-1])
        
        # Test case 4: Single element array
        arr4 = [5]
        max_sum, subarray = kadane(arr4)
        self.assertEqual(max_sum, 5)
        self.assertEqual(subarray, [5])
        
        # Test case 5: Array with zeros
        arr5 = [0, -1, 2, -3, 4, -5]
        max_sum, subarray = kadane(arr5)
        self.assertEqual(max_sum, 4)
        self.assertTrue(len(subarray) > 0)

def run_tests():
    """Run all test cases."""
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests()