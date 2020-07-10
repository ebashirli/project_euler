def longestCollatzSequence(limit):
    counter = 0
    longest_producer = 0
    for i in range(1, limit):
        starting_number = i
        temp_counter = 1
        while(True):
            starting_number = starting_number/2 if starting_number%2 == 0 else 3*starting_number+1
            temp_counter+=1
            if starting_number==1:
                if counter < temp_counter:
                    counter = temp_counter
                    longest_producer = i
                    temp_counter = 0
                break
    return longest_producer

print(longestCollatzSequence(1000000))