nums,signs,ls,mp = [],[],"+-/*","*/"
ex = input("Enter an expression: ")
while ex != "":
    startindex,result,nums,signs,flag = 0,0,[],[],False
    for i in range(len(ex)):
        if ex[i] in ls:
            nums.append(float(ex[startindex:i]))
            signs.append(ex[i])
            startindex = i+1
    nums.append(float(ex[startindex::]))
    if len(signs) == 0:
        print(f"={ex}")
        ex = input("Enter an expression: ")
        continue
    while "*" in signs or "/" in signs:
        for i in range(len(signs)):
            if signs[i] in mp:
                if signs[i] == "/" and nums[i+1] == 0:
                    flag = True
                    signs.pop(i)
                    break
                elif signs[i] == "*":
                    nums[i] = nums[i] * nums[i+1]
                elif signs[i] == "/":
                    nums[i] = nums[i] / nums[i+1]
                nums.pop(i+1)
                signs.pop(i)
                break
    if flag:
        print("Expression not evaluated!")
        ex = input("Enter an expression: ")
        continue
    result = nums[0] if len(signs) == 0 else 0
    for i in range(len(signs)):
        if i == 0:
            if signs[i] == "+":
                result = nums[i] + nums[i+1]
            elif signs[i] == "-":
                result = nums[i] - nums[i+1]
        else:
            if signs[i] == "+":
                result += nums[i+1]
            elif signs[i] == "-":
                result -= nums[i+1]
    print(f"={format(result,'.10g')}")
    ex = input("Enter an expression: ")