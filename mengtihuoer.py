import random


#定义每次门后面的随机产生的东西
def door():
    list1 = [0, 1, 2]
    things = ['car','goat1','goat2']
    random.shuffle(things)
    a = things.index('car')
    return a,list1
    
    
#主持人的选择
def second_host(a,list1,num_st):
    if a != num_st:
        list1.remove(a)
        list1.remove(num_st)
        num_nd = list1[0]
        print('山羊在' + str(num_nd) + '号门里')
        #在这种情况下，最后主持人能提出选择的门已经确定了
        if (input('你想选择' +str(a) + '号门么？（Y/N）')) == 'Y':
            print('you win')
        else:
            print('you lose')
    else:
        list1.remove(num_st)
        num_nd = random.choice(list1)
        print('山羊在' + str(num_nd) + '号门里')
        #这个时候参与者的剩下的选择肯定是山羊，则
        list1.remove(num_nd)
        num_rd = list1[0]
        if (input('你想选择' +str(num_rd) + '号门
                  么？（Y/N）')) == 'Y':
            print('you lose')
        else:
            print('you win')


def Body():
    print('---------------')
    a,list1 = door()
    #参与者的选择
    num_st = int(input('你的第一次选择是：'))
    second_host(a,list1,num_st)

Body()
while (input('还想来么？（Y/N）') == 'Y'):
    Body()
