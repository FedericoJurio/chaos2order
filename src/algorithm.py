class SortingAlgorithm(object):
    def __init__(self):
        self.name = None

    def factory(type):
        if type == 'bubble': return BubbleSort()
        if type == 'quick': return QuickSort()
        if type == 'heap': return HeapSort()
        assert 0, 'Wrong algorithm: ' + type
    factory = staticmethod(factory)


class BubbleSort(SortingAlgorithm):
    def __init__(self):
        super(BubbleSort, self).__init__()
        self.name = 'bubble'

    def sort(self, array):
        array = list(array)
        swaps = []
        for i in range(len(array)):
            for k in range(len(array) - 1, i, -1):
                if array[k] < array[k - 1]:
                    swaps.append([k, k - 1])
                    tmp = array[k]
                    array[k] = array[k - 1]
                    array[k - 1] = tmp

        return swaps


class QuickSort(SortingAlgorithm):
    def __init__(self):
        super(SortingAlgorithm, self).__init__()
        self.name = 'quick'

    def sort(self, array):
        array = list(array)

        def _quicksort(swaps, array, begin, end):
            if begin >= end:
                return swaps

            pivot, new_swaps = self.partition(array, begin, end)
            swaps += new_swaps
            swaps = _quicksort(swaps, array, begin, pivot - 1)
            swaps = _quicksort(swaps, array, pivot + 1, end)

            return swaps

        return _quicksort([], array, 0, len(array) - 1)

    def partition(self, array, begin, end):
        pivot = begin
        swaps = []
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
                swaps.append([i, pivot])
        array[pivot], array[begin] = array[begin], array[pivot]
        swaps.append([pivot, begin])
        return pivot, swaps


class HeapSort(SortingAlgorithm):
    def __init__(self):
        super(HeapSort, self).__init__()
        self.name = 'heap'

    def sort(self, array):
        array = (array * 10000).astype(int)
        array = list(array)

        # convert array to heap
        swaps = []
        length = len(array) - 1
        for i in range(length // 2, -1, -1):
            self.move_down(array, swaps, i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if array[0] > array[i]:
                swaps.append([0, i])
                self.swap(array, 0, i)
                swaps = self.move_down(array, swaps, 0, i - 1)

        return swaps

    def move_down(self, array, swaps, first, last):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if (largest < last) and (array[largest] < array[largest + 1]):
                largest += 1

            # right child is larger than parent
            if array[largest] > array[first]:
                swaps.append([largest, first])
                self.swap(array, largest, first)
                # move down to largest child
                first = largest
                largest = 2 * first + 1
            else:
                break

        return swaps

    def swap(self, A, largest, first):
        tmp = A[largest]
        A[largest] = A[first]
        A[first] = tmp
