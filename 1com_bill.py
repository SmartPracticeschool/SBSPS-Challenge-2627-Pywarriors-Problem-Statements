IndianStandard=[1,2,5,10,20,50,100,200,500,2000]
def bill_count(user_amt,lst_money):
    money_count=[]
    count,i=0,0
    lst_money.sort(reverse=True)
    while user_amt != 0:
        if lst_money[i] <= user_amt and lst_money[i] in IndianStandard:
            user_amt-=lst_money[i]
            count+=1
        else:
            money_count.append((lst_money[i],count))
            i+=1
            count=0
    money_count.append((lst_money[i],count))
    return money_count

if __name__ == '__main__':
    test=0
    while test!=1:
        user_amt,lst_money=int(input()),list(map(int,input().split()))#lst_money is get from the user in single line(like 20 10 1)
        if user_amt>0 and len([i for i in lst_money if i>0])!=0:
            bill=bill_count(user_amt,lst_money)
            print("We require"," and ".join(str(str(i[1])+"  "+str(i[0])+"Rs bill")for i in bill if i[1]!=0),"to equal Rs "+str(user_amt))
            print("Therefore, Minimum Count Money Bills is"," + ".join(str(i[0])for i in bill if i[1]!=0),sum([i[1]for i in bill if i[1]!=0]))
            test=1
        else:
            print("The Amount and The List of Money bills should be a positive value")




'''        
print(bill_count(1001,[1,20,5]),sum([i[1]for i in bill_count(1001,[1,20,5])]))
print(bill_count(100,[1,20,10]),sum([i[1]for i in bill_count(100,[1,20,10])]))
print(bill_count(1050,[1,20,10,100]),sum([i[1]for i in bill_count(1050,[1,20,10,100])]))
print(bill_count(3,[1,10]),sum([i[1]for i in bill_count(3,[1,10])]))
print(bill_count(55,[1,10,5,50]),sum([i[1]for i in bill_count(55,[1,10,5,50])]))
'''
