import random
import time

class PageReplacementSimulator:
    def __init__(self, num_frames, page_references):
        self.num_frames = num_frames
        self.page_references = page_references
        self.page_faults = 0

    def simulate_fifo(self):
        frames = []
        for page in self.page_references:
            if page not in frames:
                self.page_faults += 1
                if len(frames) == self.num_frames:
                    frames.pop(0)
                frames.append(page)
        return self.page_faults

    def simulate_lru(self):
        frames = []
        for page in self.page_references:
            if page not in frames:
                self.page_faults += 1
                if len(frames) == self.num_frames:
                    frames.pop(0)
                frames.append(page)
            else:
                frames.remove(page)
                frames.append(page)
        return self.page_faults

    def simulate_optimal(self):
        frames = []
        for page in self.page_references:
            if page not in frames:
                self.page_faults += 1
                if len(frames) == self.num_frames:
                    future_pages = self.page_references[self.page_references.index(page):]
                    frames.remove(max(frames, key=lambda x: future_pages.index(x) if x in future_pages else float('inf')))
                frames.append(page)
        return self.page_faults


# Generate a sequence of page references for simulation purposes
num_pages = 20
page_references = [random.randint(1, 10) for _ in range(num_pages)]

# Simulate FIFO algorithm
simulator_fifo = PageReplacementSimulator(num_frames=3, page_references=page_references)
fifo_faults = simulator_fifo.simulate_fifo()

# Simulate LRU algorithm
simulator_lru = PageReplacementSimulator(num_frames=3, page_references=page_references)
lru_faults = simulator_lru.simulate_lru()

# Simulate Optimal algorithm
simulator_optimal = PageReplacementSimulator(num_frames=3, page_references=page_references)
optimal_faults = simulator_optimal.simulate_optimal()

# Analyze the results
print('****Analyzing FIFO faults***')
time.sleep(1)
print("FIFO faults:", fifo_faults)
print('****Analyzing LRU faults***')
time.sleep(1)
print("LRU faults:", lru_faults)
print('****Analyzing Optimal faults***')
time.sleep(1)
print("Optimal faults:", optimal_faults)
print('Execution completed')