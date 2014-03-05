#!/usr/bin/env python

import random
import strategy

def buildQuestions():
    nums = [(x+10,y,x+10-y) for x in range(1,10) for y in range(x+1,10)]
    return nums

class Question():
    def __init__(self):
        self.identity=''
        self.description=''
        self.ans=0
        self.recount=5
        self.correct=0
        self.intcorrect=0
        self.concount=0

def buildBallPool(leng):
    blist = [i for i in range(leng) for n in range(5)]
    return blist

def formatQuestion(tupl):
    pr = '%d - %s = ' % (tupl[0], tupl[1])
    return pr

def main():
    questions = buildQuestions()
    ballpool = buildBallPool(len(questions))
    leng = len(ballpool)
    while leng>0:
        bindex = random.randint(0,leng-1)
        qindex = ballpool[bindex]
        question = questions[qindex]
        print 'qleng', len(questions), 'pleng', leng, 'bindex', bindex, 'qindex', qindex
        if int(raw_input(formatQuestion(question))) == question[2]:
            print 'Right'
            ballpool.remove(qindex)
            if ballpool.count(qindex) == 0:
                print 'You grasped this question!'
        else:
            print 'Wrong'
            ballpool.append(qindex)
        leng = len(ballpool)
    print 'Congras, you grasped all questions'

if __name__ == '__main__':
    main()
