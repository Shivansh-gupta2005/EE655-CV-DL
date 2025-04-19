import numpy as np

def transposed_convolution(input_matrix, kernel, stride, crop):
    input_h, input_w = input_matrix.shape
    kernel_h, kernel_w = kernel.shape
    stride_h, stride_w = stride
    
    # Compute the output size before cropping
    output_h = (input_h - 1) * stride_h + kernel_h
    output_w = (input_w - 1) * stride_w + kernel_w
    
    # Initialize output matrix with zeros
    output_matrix = np.zeros((output_h, output_w))
    
    # Perform transposed convolution
    for i in range(input_h):
        for j in range(input_w):
            output_matrix[i * stride_h : i * stride_h + kernel_h, j * stride_w : j * stride_w + kernel_w] += input_matrix[i, j] * kernel
    
    # Apply cropping
    if crop > 0:
        output_matrix = output_matrix[crop:-crop, crop:-crop]
    
    return output_matrix

input_matrix = []
for i in range(2):
    row = list(map(int, input().split()))
    input_matrix.append(row)

print(input_matrix)


kernel = []
for i in range(2):
    row = list(map(int, input().split()))
    kernel.append(row)

print(kernel)

input_matrix = np.array(input_matrix)
kernel = np.array(kernel)

# Define stride and crop
stride_h = int(input())
stride_w = int(input())
print((stride_h, stride_w))

stride = (stride_h, stride_w)

crop = int(input())
print(crop)

output = transposed_convolution(input_matrix, kernel, stride, crop)
print("Output Matrix:")
print(output)
