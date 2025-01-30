# Exercise 1: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Exercise 2: Graph Traversal
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def is_connected(self, start, end):
        if start == end:
            return True, [start]
        
        visited = set()
        queue = deque([(start, [start])])
        
        while queue:
            vertex, path = queue.popleft()
            visited.add(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor == end:
                    return True, path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return False, []

# Exercise 3: Knapsack Problem
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected

# Exercise 4: Merge Intervals
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(interval)
    
    return merged

# Exercise 5: Maximum Subarray Sum (Kadane's Algorithm)
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = curr_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            curr_start = i
        else:
            max_ending_here = max_ending_here + arr[i]
            
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = curr_start
            end = i
            
    return max_so_far, arr[start:end+1]

# Test cases
if __name__ == "__main__":
    # Binary Search Test
    print("Binary Search Tests")
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(f"\nArray: {sorted_array}\tTarget: {target}\tIndex: {binary_search(sorted_array, target)}\n")
    
    # Additional Binary Search Tests
    test_cases = [
        ([1, 3, 5, 7, 9], 3),
        ([2, 4, 6, 8, 10], 5),
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5], 6)
    ]
    
    for arr, val in test_cases:
        print(f"\nArray: {arr}\tTarget: {val}\tIndex: {binary_search(arr, val)}\n")
    
    print("\n\n")
    
    # Graph Traversal Test
    print("Graph Traversal Tests")
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(f"BFS Test: {g.bfs(0)}")
    print(f"DFS Test: {g.dfs(0)}")
    
    # Check if two locations are connected and find the shortest path
    start, end = 0, 3
    connected, path = g.is_connected(start, end)
    print(f"Is Connected Test: {connected}, Path: {path}")
    
    print("\n\n")
    
    # Knapsack Test
    print("Knapsack Tests")
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value, selected = knapsack(values, weights, capacity)
    print(f"Knapsack Test: Value = {max_value}, Selected Items = {selected}")
    
    # Additional Knapsack Tests
    knapsack_test_cases = [
        ([20, 30, 40], [5, 10, 15], 20),
        ([10, 20, 30], [1, 2, 3], 5),
        ([15, 25, 35], [3, 4, 5], 7),
        ([50, 60, 70], [10, 20, 30], 40),
        ([5, 10, 15], [1, 2, 3], 3)
    ]
    
    for vals, wts, cap in knapsack_test_cases:
        max_val, sel_items = knapsack(vals, wts, cap)
        print(f"Knapsack Test: Values = {vals}, Weights = {wts}, Capacity = {cap}, Max Value = {max_val}, Selected Items = {sel_items}")
    
    print("\n\n")
    
    # Merge Intervals Test
    print("Merge Intervals Tests")
    intervals = [(1,3), (2,6), (8,10), (15,18)]
    print(f"Merge Intervals Test : input: {intervals}, output: {merge_intervals(intervals)}")
    
    # Additional Merge Intervals Tests
    merge_intervals_test_cases = [
        ([(1, 2), (3, 4), (5, 6)], "No Overlaps"),
        ([(1, 5), (2, 6), (3, 7)], "Full Overlaps"),
        ([(1, 3), (2, 4), (5, 7)], "Partial Overlaps"),
        ([(1, 4), (4, 5), (6, 8)], "Touching Intervals"),
        ([(1, 10), (2, 3), (4, 5)], "Nested Intervals")
    ]
    
    for intervals, description in merge_intervals_test_cases:
        print(f"Merge Intervals Test: input : {intervals}, ({description})  : Output : {merge_intervals(intervals)}")
    
    print("\n\n")
    
    # Kadane's Algorithm Test
    print("Kadane's Algorithm Tests")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = kadane(arr)
    print(f"Kadane's Algorithm Test: Max Sum = {max_sum}, Subarray = {subarray}")
    
    # Additional Kadane's Algorithm Tests
    kadane_test_cases = [
        ([-1, -2, -3, -4], "All Negative"),
        ([1, 2, 3, 4], "All Positive"),
        ([-1, 2, -3, 4, -5, 6], "Mixed"),
        ([0, -1, 2, -3, 4, -5, 6], "Mixed with Zero"),
        ([5, -2, 3, -1, 2, -1, 2], "Mixed with Positive Sum")
    ]
    
    for arr, description in kadane_test_cases:
        max_sum, subarray = kadane(arr)
        print(f"Kadane's Algorithm Test ({description}): Max Sum = {max_sum}, Subarray = {subarray}")