def show_even_nums():
    for x in range(0, 20):
        if x % 2 == 0:
            print(x)

def show_names_upper(names):
    for name in names:
        print(name.upper())

def sum_nums(nums):
    sum=0
    for num in nums:
        sum+=num
    print(sum)

def vowels(word):
    vowel_sum=0
    for char in word:
        if char in 'aeiou':
            vowel_sum+=1
    print(vowel_sum)

def fibonacci():
    n=0
    n1=0
    n2=1
    for i in range(10):
        n=n1+n2
        n2=n1
        n1=n
        print(n)

def bigger_num(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                aux=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=aux
    print(nums.pop(len(nums)-1))

def invert_str(word):
    word_formatted=""
    for char in range(len(word)-1,-1,-1):
        word_formatted+=word[char]
    print(word_formatted)

def remove_duplicated(elements:list):
    for element in elements:
        if elements.count(element)>1:
            for e in range(elements.count(element)-1):
                elements.remove(element)
    print(elements)

def val_crescent(nums):
    for i in range(len(nums) - 1):  # Ensure we don’t access nums[i+1] out of bounds
        if nums[i] > nums[i + 1]:
            return False
    return True