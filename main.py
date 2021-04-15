"""This is a sample Python script to find all
possible combinations of the integers that produce the target sum """
import datetime

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

    target = 12
    start = datetime.datetime.now()
    subsets = subset_sum(nums, target)
    end = datetime.datetime.now() - start
    print(subsets)
    print(end)
    print("There are {} distinct combinations for the sum {}.".format(len(subsets), target))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
