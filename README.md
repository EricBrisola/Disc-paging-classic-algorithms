# Page Replacement Algorithms Evaluation

This Python script evaluates different page replacement algorithms including FIFO (First-In-First-Out), LRU (Least Recently Used), and Second Chance. The algorithms are assessed based on the number of page faults they generate.

## Overview

This script simulates the behavior of three page replacement algorithms using a random sequence of pages as input. The main objective is to analyze and compare the efficiency of these algorithms in terms of handling page faults.

## How to Use

1. Input the desired parameters:
   - `numPaginas`: Number of random pages to simulate.
   - `tamanhoQuadro`: Initial size of the page frames.
   - `tamanhoQuadroFinal`: Final size of the page frames.

2. Run the script and observe the results.

## Algorithms Implemented

### FIFO (First-In-First-Out)

The FIFO algorithm replaces the oldest page in memory. When a page fault occurs and the page frames are full, the oldest page is removed to accommodate the new page.

### LRU (Least Recently Used)

The LRU algorithm replaces the page that has not been used for the longest time. It aims to minimize the number of page faults by discarding the least recently accessed page.

### Second Chance

The Second Chance algorithm combines elements of both FIFO and LRU. It gives a "second chance" to pages by not immediately evicting a page when selected. If the page is accessed again before another replacement occurs, it remains in memory.

## Result Visualization

The script generates a plot illustrating the number of page faults for each algorithm across a range of different page frame sizes. This visualization helps in understanding how each algorithm performs with varying memory constraints.

## Dependencies

The script relies on the following libraries:
- `random`: For generating random page sequences.
- `matplotlib.pyplot`: For creating the plot that visualizes the results.

## Example

Here's an example of how to use the script:

```python
python trabalhoSopComGrafico.py
