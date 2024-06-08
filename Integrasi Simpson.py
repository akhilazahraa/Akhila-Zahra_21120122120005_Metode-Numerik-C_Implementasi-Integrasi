import numpy as np
import time

def f(x):
    return 4 / (1 + x**2)

def simpson_1_3(a, b, N):
    if N % 2 != 0:
        raise ValueError("N must be an even number.")
    
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    
    integral = y[0] + y[-1]
    for i in range(1, N, 2):
        integral += 4 * y[i]
    for i in range(2, N-1, 2):
        integral += 2 * y[i]
        
    integral *= h / 3
    return integral

def compute_error_and_time(N, true_value):
    start_time = time.time()
    estimated_pi = simpson_1_3(0, 1, N)
    end_time = time.time()
    
    rms_error = np.sqrt((estimated_pi - true_value)**2)
    execution_time = end_time - start_time
    
    return estimated_pi, rms_error, execution_time

def main():
    true_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]
    
    for N in N_values:
        estimated_pi, rms_error, exec_time = compute_error_and_time(N, true_pi)
        print(f"N = {N}")
        print(f"Estimated Pi: {estimated_pi}")
        print(f"RMS: {rms_error}")
        print(f"Execution Time: {exec_time} seconds")
        print("-------------------------------")

if __name__ == "__main__":
    main()