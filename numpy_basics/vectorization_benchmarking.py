import time 
import numpy as np


def main():
    # pure python
    start_time = time.perf_counter()
    
    list_num = [i*2 for i in range(10000000)]
    
    end_time = time.perf_counter()
    
    print(f"Total time taken {(end_time-start_time):.4f}")
    
    
    # numpy
    start_time = time.perf_counter()
        
    np_array = np.arange(10000000)*2
    
    end_time = time.perf_counter()
    
    print(f"Total time taken {(end_time-start_time):.4f}")
    
if __name__ == "__main__":
    main()