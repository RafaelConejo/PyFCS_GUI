"""
Benchmark Script for Evaluating Color Space Creation Speed

This script is designed to benchmark the time and memory usage involved in
creating a new fuzzy color space with a user-defined number of colors. It is 
intended for performance testing and evaluating the program's capacity to 
handle different palette sizes. After the test, the generated file is deleted.
"""

import numpy as np
import time
import tracemalloc
import os
import sys
from skimage import color

# Get the path to the directory containing PyFCS
current_dir = os.path.dirname(__file__)
pyfcs_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Add the PyFCS path to sys.path
sys.path.append(pyfcs_dir)

### Import custom library ###
from PyFCS import Input


def load_color_data(file_path):
    """
    Reads color data from a file and converts LAB values to RGB.
    Returns a dictionary of colors with their LAB and RGB values.
    """
    input_class = Input.instance('.cns')
    color_data = input_class.read_file(file_path)

    colors = {}
    for color_name, color_value in color_data.items():
        lab = np.array(color_value['positive_prototype'])
        rgb = tuple(map(lambda x: int(x * 255), color.lab2rgb([lab])[0]))
        colors[color_name] = {"rgb": rgb, "lab": lab}
    return colors

# Generate a sample palette with synthetic LAB colors
def generate_sample_palette(n=50):
    return {
        f"Color_{i}": np.array([i * 10.0, i * 5.0, i * 3.0])
        for i in range(1, n + 1)
    }

# ISCC_NBS color spaces
def generate_color_space(color_space):
    if color_space == 1:
        cs_path = 'ISCC_NBS_BASIC.cns'
    elif color_space == 2:
        cs_path = 'ISCC_NBS_EXTENDED.cns'
    else:
        cs_path = 'ISCC_NBS_COMPLETE.cns'

    color_space_path = os.path.join(os.getcwd(), 'fuzzy_color_spaces', 'cns', cs_path)
    colors = load_color_data(color_space_path)
    
    lab_only = {
        name: np.array(data['lab'])
        for name, data in colors.items()
        if 'lab' in data
    }
    
    return lab_only

def benchmark_full_color_space_creation():
    color_space = 1
    palette = generate_color_space(color_space)
    name = "BenchmarkColorSpaceCreate"
    file_path = os.path.join(os.getcwd(), "fuzzy_color_spaces", f"{name}.fcs")

    # Start memory and time tracking
    tracemalloc.start()
    start_time = time.perf_counter()

    # Create and save the color space
    input_class = Input.instance('.fcs')
    input_class.write_file(name, palette)

    # End tracking
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Display benchmark results
    print(f"✔ Color space '{name}' created with {len(palette)} colors.")
    print(f"⏱ Total time: {end_time - start_time:.6f} seconds")
    print(f"📦 Current memory usage: {current / 1024:.2f} KB")
    print(f"📈 Peak memory usage: {peak / 1024:.2f} KB\n")

    # Delete the generated file after benchmarking
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"🗑 File '{file_path}' deleted after benchmark.")

if __name__ == "__main__":
    benchmark_full_color_space_creation()
