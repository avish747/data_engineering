def solution (S,A):
    ans=""
    k=0
    for i in range(len(S)):
        ans += S[k]
        if k==0:
            break
    return ans

print(solution("cdeo", [3,2,0,1]))