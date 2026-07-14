# Logical Operators - combine 2 or more conditions. TRUE or FALSE
    # and : both conditions must be TRUE
    # or : either condition must be TRUE
    # not : negates the boolean value

coffee = True
milk = False

result = coffee and milk, coffee or milk, not coffee, not milk
print(result)