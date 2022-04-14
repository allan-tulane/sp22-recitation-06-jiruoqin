import random, time
import tabulate
import sys
print(sys.setrecursionlimit(5000))
# Make the stack size bigger allowing more test cases.

def random_pivot(a):
    return random.choice(a)

def fixed_pivot(a):
    return a[0]

def qsort(a, pivot_fn):
    if len(a) == 0:
        return a
    else:
        p = pivot_fn(a)
        l = list(filter(lambda x: x < p, a)) 
        r = list(filter(lambda x: x > p, a))  
        left = qsort (l, pivot_fn)
        right = qsort(r, pivot_fn)
        a = left + [p] + right 
    return a 

def qsort_random(a):
    return qsort(a, random_pivot)

def qsort_fixed(a):
    return qsort(a, fixed_pivot)

def ssort(a):
    for i in range(len(a) - 1):
        min = i
 
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        temp = a[min]
        a[min] = a[i]
        a[i] = temp 
    return a
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 300, 400, 500, 1000, 1500, 2000, 2500, 3000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = qsort_fixed
    qsort_random_pivot = qsort_random
    selection_sort = ssort
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(selection_sort, mylist), 
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def compare_random(sizes=[100, 200, 300, 400, 500, 1000, 1500, 2000, 2500, 3000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = qsort_fixed
    qsort_random_pivot = qsort_random
    selection_sort = ssort
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(selection_sort, mylist), 
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'selection-sort', 'tim-sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print("Running time of sorted permutations:\n")
    print_results(compare_sort())
    print("\n")
    print("Running time of random permutations:\n")
    print_results(compare_random())

random.seed()
test_print()
