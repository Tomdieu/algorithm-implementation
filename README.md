# Algorithm Implementation Collection

This repository contains implementations of five fundamental algorithms in Python, demonstrating various problem-solving approaches in computer science.

## Table of Contents
- [Algorithms Overview](#algorithms-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Details](#algorithm-details)
- [Contributing](#contributing)
- [License](#license)

## Algorithms Overview

1. **Binary Search**: An efficient search algorithm for sorted arrays
2. **Graph Traversal**: Implementation of BFS and DFS with path finding
3. **Knapsack Problem**: Dynamic programming solution for the 0/1 knapsack problem
4. **Merge Intervals**: Algorithm to merge overlapping intervals
5. **Maximum Subarray Sum**: Implementation of Kadane's Algorithm

## Requirements

- Python 3.6 or higher
- collections library (standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tomdieu/algorithm-implementation.git
cd algorithm-implementation
```

2. No additional package installation is required as the code uses only Python standard libraries.

## Usage

The code contains a main test section that demonstrates the usage of each algorithm. To run all tests:

```bash
python algorithms.py
```

### Individual Algorithm Usage

#### Binary Search
```python
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(sorted_array, target)
print(f"Found target {target} at index {result}")
```

#### Graph Traversal
```python
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

# Run BFS
bfs_result = graph.bfs(0)
print(f"BFS traversal: {bfs_result}")

# Run DFS
dfs_result = graph.dfs(0)
print(f"DFS traversal: {dfs_result}")

# Check connectivity
connected, path = graph.is_connected(0, 3)
print(f"Path from 0 to 3: {path}")
```

#### Knapsack Problem
```python
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected = knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {selected}")
```

#### Merge Intervals
```python
intervals = [(1,3), (2,6), (8,10), (15,18)]
merged = merge_intervals(intervals)
print(f"Merged intervals: {merged}")
```

#### Maximum Subarray Sum
```python
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = kadane(array)
print(f"Maximum sum: {max_sum}")
print(f"Maximum sum subarray: {subarray}")
```

## Algorithm Details

### Binary Search
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Used for finding elements in sorted arrays
- Returns the index of the target element or -1 if not found

### Graph Traversal
- Implements both BFS and DFS
- Time Complexity: O(V + E) where V is vertices and E is edges
- Space Complexity: O(V)
- Features:
  - Breadth-First Search
  - Depth-First Search
  - Path finding between vertices
  - Connectivity checking

### Knapsack Problem
- Dynamic Programming solution
- Time Complexity: O(nW) where n is number of items and W is capacity
- Space Complexity: O(nW)
- Returns maximum value possible and selected items

### Merge Intervals
- Time Complexity: O(n log n) due to sorting
- Space Complexity: O(n)
- Merges overlapping intervals into continuous ranges
- Useful for schedule/timeline optimization

### Maximum Subarray Sum (Kadane's Algorithm)
- Time Complexity: O(n)
- Space Complexity: O(1)
- Finds the contiguous subarray with the largest sum
- Returns both the maximum sum and the subarray

## Testing

The repository includes a comprehensive test suite that verifies the functionality of all implemented algorithms. The tests are written using Python's unittest framework.

### Running Tests

1. All tests:
```bash
python test_algorithms.py
```

2. Specific algorithm tests:
```bash
# Run only binary search tests
python -m unittest test_algorithms.TestAlgorithms.test_binary_search -v

# Run only graph traversal tests
python -m unittest test_algorithms.TestAlgorithms.test_graph_bfs test_algorithms.TestAlgorithms.test_graph_dfs -v

# Run only knapsack tests
python -m unittest test_algorithms.TestAlgorithms.test_knapsack -v

# Run only merge intervals tests
python -m unittest test_algorithms.TestAlgorithms.test_merge_intervals -v

# Run only Kadane's algorithm tests
python -m unittest test_algorithms.TestAlgorithms.test_kadane -v
```

### Test Cases Coverage

The test suite includes comprehensive test cases for each algorithm:

1. Binary Search:
   - Normal search scenarios
   - Edge cases (empty arrays, single elements)
   - Boundary testing (first/last elements)
   - Non-existent elements

2. Graph Traversal:
   - BFS and DFS from different starting points
   - Path finding between nodes
   - Connectivity testing
   - Edge cases (self-loops, disconnected nodes)

3. Knapsack Problem:
   - Various capacity scenarios
   - Different item combinations
   - Edge cases (no items fit, all items fit)
   - Single item cases

4. Merge Intervals:
   - Overlapping intervals
   - Non-overlapping intervals
   - Edge cases (empty input, single interval)
   - Touching intervals

5. Maximum Subarray Sum:
   - Mixed positive/negative numbers
   - All positive/negative cases
   - Single element arrays
   - Zero-containing arrays

### Test Output

The test suite provides detailed output including:
- Pass/fail status for each test
- Detailed error messages for failures
- Total test count and execution time
- Coverage of edge cases and normal scenarios

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details