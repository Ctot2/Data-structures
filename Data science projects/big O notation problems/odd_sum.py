def odd_sum(nums):
    has_odd = False
    has_even = False

    for i in nums:
        if i % 2 == 0:
            has_even = True
        else:
            has_odd = True
    if has_odd == True and has_even == True:
        return True
    else:
        return False


print(odd_sum([0, 0, 1]))

