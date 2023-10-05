def palindrom(s, query, sub):
    substr = s[query[0]:query[1]+1]
    
    dict = {}
    for x in substr:
        if(x in dict.keys()):
            dict[x] = dict[x]+1
        else:
            dict[x] = 1

    count = 0
    for x in dict:
        if(dict[x]%2 != 0):
            count += 1

    if(count%2 != 0 and len(substr)%2 == 0):
        return 0

    subs_needed = int(count/2)

    if(subs_needed <= sub):
        return 1
    else:
        return 0

s = input()
start_index = input().lstrip('[ ').rstrip(' ]').split(', ')
end_index = input().lstrip('[ ').rstrip(' ]').split(', ')
subs = input().lstrip('[ ').rstrip(' ]').split(', ')

subs = [int(x) for x in subs]
    
queries = []
for i in range(len(start_index)):
    queries.append((int(start_index[i]), int(end_index[i])))

ans = [0 for i in range(len(queries))]

for i in range(len(queries)):
    ans[i] = palindrom(s, queries[i], subs[i])

print(ans)
