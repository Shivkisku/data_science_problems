def partition(n):
    def partition_helper(n, current_partition):
        if n == 0:
            partitions.append(current_partition[:])
            return
        if n < 0:
            return
        
        for i in range(1, n + 1):
            # Avoid duplicate partitions by considering only non-decreasing order
            if not current_partition or i >= current_partition[-1]:
                current_partition.append(i)
                partition_helper(n - i, current_partition)
                current_partition.pop()
    
    partitions = []
    partition_helper(n, [])
    return partitions

# Example usage:
n = 4
partitions = partition(n)
print(partitions)
