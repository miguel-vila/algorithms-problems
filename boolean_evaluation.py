
# from cracking the code interview:
# last one on chapter 8
def countEval(exp, b):
    if len(exp) == 1:
        return 1 if int(exp) == b else 0
    count = 0
    for i in xrange(len(exp)):
        if exp[i] == '|' or exp[i] == '&' or exp[i] == '^':
            left = exp[0:i]
            right = exp[i+1:len(exp)]

            leftTrue = countEval(left, True)
            rightTrue = countEval(right, True)
            leftFalse = countEval(left, False)
            rightFalse = countEval(right, False)

            totalWays = (leftTrue + leftFalse)*(rightTrue + rightFalse)

            totalExp = 0
            if exp[i] == '|':
                totalExp = leftTrue*rightFalse + leftFalse*rightTrue + leftTrue*rightTrue
            elif exp[i] == '&':
                totalExp = leftTrue * rightTrue
            else:
                totalExp = leftTrue * rightFalse + leftFalse * rightTrue

            count += totalExp if b else totalWays - totalExp
    return count
    
assert(countEval("1^0|0|1", False) == 2)
assert(countEval("0&0&0&1^1|0",True) == 10)

