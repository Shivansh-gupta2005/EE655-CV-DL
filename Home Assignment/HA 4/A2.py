import numpy as np

def intersection_over_union(matrix1, matrix2):
    # Validate input matrices are binary (contain only 0s and 1s)
    if not np.array_equal(matrix1, matrix1.astype(bool).astype(int)):
        raise ValueError("First input matrix is not binary (contains values other than 0 and 1)")
    
    if not np.array_equal(matrix2, matrix2.astype(bool).astype(int)):
        raise ValueError("Second input matrix is not binary (contains values other than 0 and 1)")
    
    # Check if matrices have the same shape
    if matrix1.shape != matrix2.shape:
        raise ValueError(f"Input matrices have different shapes: {matrix1.shape} vs {matrix2.shape}")
    
    # Calculate intersection (element-wise AND operation)
    intersection = np.logical_and(matrix1, matrix2).sum()
    
    # Calculate union (element-wise OR operation)
    union = np.logical_or(matrix1, matrix2).sum()
    
    # Handle edge case where both matrices are all zeros
    if union == 0:
        return 1.0  # By convention, IoU = 1 when both sets are empty
    
    # Calculate IoU
    iou = intersection / union
    
    return iou

# Example usage
if __name__ == "__main__":
    # Input two sample binary matrices

    n = int(input())

    matrix1 = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix1.append(row)
    
    matrix1 = np.array(matrix1)
    
    matrix2 = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix2.append(row)
    
    matrix2 = np.array(matrix2)
    
    # Calculate IoU
    iou_score = intersection_over_union(matrix1, matrix2)
    
    print("Matrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)
    print(f"\nIntersection over Union (IoU): {iou_score:.2f}")