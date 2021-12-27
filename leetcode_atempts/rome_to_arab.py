
def transf(roman):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    
    for i in range(0, len(roman)):
        if  i==0 or dict[roman[i]] <= dict[roman[i - 1]]:
            res += dict[roman[i]]
        else:    
            res += dict[roman[i]] - 2* dict[roman[i-1]]
    return res
 
       


roman_input = 'IV'
number_output = transf(roman_input)
print('Roman numeral {0} equal to:{1}'.format(roman_input, number_output))

