def uniq_add(my_list=[]):
    total = 0
    nums = []

    for num in my_list:
        if num in nums:
            continue
        else:
            nums.append(num)

    for i in nums:
        total += i

    return total

if __name__ == "__main__":
    uniq_add(my_list)