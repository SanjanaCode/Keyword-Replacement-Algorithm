from random import choice
import time


def calculateTimeForEachT(myFn, tVals,  tweets, abbreviations_dict, numTrials=20):
    tValues = []
    timeValues = []
    for t in tVals:
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst1 = [ choice(tweets) for i in range(t) ] # generate a random list of tweets of length n
            start = time.time()
            myFn( lst1, abbreviations_dict )
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        tValues.append(t)
        timeValues.append(runtime)
    return tValues, timeValues