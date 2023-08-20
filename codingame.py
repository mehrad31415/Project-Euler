# question inspired by codingame
# the question is that the input array is a pre-defined array of strings with the format of "number->number"
# each string corresponds to a guard and the numbers inside the string represent the duration which the guard has a shift.
# take for example the input = ["3->18", "15->20"]. This means that we have two guards and the first guards shift
# is from 3 to 18 and the second guards shift is from 15 to 20. Obviously the guards shift are between 0 and 24 (inclusive)
# the question in hand is we want to steal from the market... 
# define all the durations which would be the best to do this.
# ps: the best times are when we have the lowest amount of guards.
# for example in the example input = ["3->18", "15->20"] the asnwer should be:
# answer = ["0->2", "20->24"]. (I know that between 2 to 3 we have no guards and should be counted but to make it simple all durations are inclusive and only the exact hours matter in this case).

input = ["3->18", "15->20"]
hours = list(range(0,25))
hours_dic ={}
for i in hours:
    hours_dic[i]=0
print(hours_dic)
for i in input:
    shift = i
    shift_split = shift.split("->")
    shift_split_int = list(map(int,shift_split))
    for j in hours_dic:
        if j>=shift_split_int[0] and j<shift_split_int[1]:
            hours_dic[j]+=1
values = list(hours_dic.values())
minimum = min (values)
final = []
for i in hours_dic:
    if hours_dic[i]==minimum:
        final.append(i)
f = []
temp = []
for i in range (len(final)-1):
    temp.append(final[i])
    if final[i] != final[i+1]-1:
        f.append(temp)
        temp = []
    if (temp != [] and i == len(final)-2):
        f.append(temp)
d = []
for i in f:
    maximum = max(i)
    minimum = min(i)
    d.append(f"{minimum}->{maximum}")
print (d)

        



    
