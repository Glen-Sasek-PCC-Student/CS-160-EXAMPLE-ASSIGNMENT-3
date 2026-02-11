#same list uses a for loop to print
def main():
    nums = [2, -3, 10, -1, 7]

    length = len(nums)

    for index in range(length):
        print(index, nums[index])
        
main()
