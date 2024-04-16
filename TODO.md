# Example TODO list

## MUST DO:
- [ ] Implement brute-force approach: https://en.wikipedia.org/wiki/Travelling\_salesman\_problem#Exact\_algorithms

## Later: (look at the title)
- [ ] Implement Held-Karp algorithm: https://en.wikipedia.org/wiki/Held%E2%80%93Karp\_algorithm
- [ ] Implement Linear programming solution: https://en.wikipedia.org/wiki/Travelling\_salesman\_problem#Integer\_linear\_programming\_formulations
- [ ] Implement branch & bound solution: https://www.math.cmu.edu/~bkell/21257-2014f/tsp.pdf
- [ ] Implement genetic programming algorithm: you know what to do
- [ ] Figure out how to prove that no shorter distance exists
- [ ] Redo everything with constraints (Middle East/Australia races start at the beginning/end)

--------------------------------------------------------------------------------
## Already done:
- [x] Get list of circuits and their coordinates
- [x] Create adjacency matricies for each city in relation to the other cities (REMEMBER TO USE geographiclib)
- [x] Make a dataclass for circuits (the main fields are the city's location in coordinates and its adjacency list, other fields include circuit name and the city and country it's in)****
- [x] Learn what a dataclass is (I didn't end up using it)
- [x] Find algorithms/libraries for finding the distance between 2 points
