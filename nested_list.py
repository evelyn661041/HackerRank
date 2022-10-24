#建立空list
Result =[]
scorelist = []

if __name__ == '__main__':
    #第一行input顯示i要跑幾次
    for _ in range(int(input())):
        #先input名字
        name = input()
        #再input分數
        score = float(input())
        #把名字和分數對應一起，然後加到result的list
        Result+=[[name,score]]
        #把分數塞到list裡
        scorelist+=[score]
    # sort分數列，找出第二低的分數
    b=sorted(list(set(scorelist)))[1] 
    #a,c對應到result裡的名字和分數列（sort->按照字母順序）
    for a,c in sorted(Result):
        #如果分數為第二低，print'a'（名字）
        if c==b:
            print(a)