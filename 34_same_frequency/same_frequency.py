def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    if len(num1) != len(num2):
        return False
    nums = set(num1)
    for num in nums:
        if num1.count(num) != num2.cout(num):
            return False
    return True