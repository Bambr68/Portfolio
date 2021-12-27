def isValid(s):
        nabor = {')':'(',']':'[','}':'{'}
        stek=[]
        for i in s:
            if i not in nabor.keys():
                stek.append(i) 
            else:
                if stek:
                    if nabor[i] == stek[-1]:
                        del stek[-1]
                    else:
                        stek+=i
                else:
                    stek+=i
        print('stek',stek)
        if len(stek)==0:
            return True
        else:
            return False


input_str="[([])]"
print('Длина выражения = ', len(input_str))
print(isValid(input_str))

