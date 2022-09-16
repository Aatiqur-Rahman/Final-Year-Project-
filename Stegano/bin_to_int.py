def method(bin_numbers):
    sum=0
    for i in range(0,8):
        if bin_numbers[i]==1:
            j=7-i
            sum+=2**j
    return sum



