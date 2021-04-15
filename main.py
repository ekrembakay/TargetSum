"""This is a sample Python script to find all
possible combinations of the integers that produce the target sum """

def subset_sum(numbers, target, subset=[], results=[]):

    # check if the sub set sum is equals to target
    if sum(subset) == target:
        results += [subset] # add the sub set numbers to the results list.
    if sum(subset) >= target:
        return  # if we reach the number do not continue

    # loop through the items of the given numbers list
    for i in range(len(numbers)):
        n = numbers[i] # assign the current item in the list to a variable
        remaining = numbers[i + 1:] # make a new list from the remaining numbers
        subset_sum(remaining, target, subset + [n]) # recursively call the subset_sum function to check other numbers
    #return sorted(results, key=len) # return the final list of lists for the number combinations
    return results
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
    """, 11, 12, 13 ,14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 35, 37,38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66]"""
    target = 12
    subsets = subset_sum(nums, target)
    print(subsets)
    print("There are {} distinct combinations for the sum {}.".format(len(subsets), target))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
