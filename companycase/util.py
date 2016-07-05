def evaluate(ccase, threshold, input):
    correct, incorrect = 0, 0
    with open(input) as f:
        for line in f:
            line = line.strip('\n')
            cased = ccase.apply(line.upper(), threshold)
            if line == cased:
                correct += 1
            else:
                incorrect += 1

    print "Total           :", correct + incorrect
    print "Correct case    :", correct
    print "Incorrect case  :", incorrect
    print "% correct       :", float(correct) / (correct + incorrect)
