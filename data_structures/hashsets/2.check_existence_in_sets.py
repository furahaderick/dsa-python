import time


def hash_set_operations():

    hash_set = set()
    list_data = []

    data_range = 10**7

    for i in range(data_range):
        hash_set.add(i)
        list_data.append(i)

    # Non-existent element
    test_element = data_range + 1

    start_time = time.time()
    print("Hash set test results: ", test_element in hash_set)
    print("Searching in hash set took: ", time.time() - start_time)
    print("This is over 4000x list searching...")

    start_time = time.time()
    print("List test results: ", test_element in list_data)
    print("List searching took: ", time.time() - start_time)


hash_set_operations()
