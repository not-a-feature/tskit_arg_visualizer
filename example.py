import msprime
import random
from visualizer import visualizer

# Generate a random tree sequence with record_full_arg=True so that you get marked recombination nodes
rs = random.randint(0,10000)   
ts = msprime.sim_ancestry(
    samples=2,
    recombination_rate=1e-8,
    sequence_length=3_000,
    population_size=10_000,
    record_full_arg=True,
    random_seed=rs
)

print("random seed:", rs)
d3arg = visualizer.D3ARG(ts=ts)
d3arg.draw(width=1000, height=750, y_axis_labels=True, y_axis_scale="log_time", tree_highlighting=True, line_type="line")