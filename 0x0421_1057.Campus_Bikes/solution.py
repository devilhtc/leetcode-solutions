# solution by shantanubhadoria@
class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        distances = []
        # create a list of distances for each worker-bike combination,
        # put distance in the first tuple element and worker index in second tuple element
        # and bike index in third. we will sort this list of tuples later.
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))

        # Sort the tuples
        distances.sort()

        result = [-1] * len(workers)
        bike_taken = (
            set()
        )  # Mark a bike as taken by putting it in this set as we traverse the tuples from shortest distance onwards.
        for distance, i, j in distances:
            # print(distance, i, j)
            if result[i] == -1 and j not in bike_taken:
                result[i] = j
                bike_taken.add(j)
        return result
