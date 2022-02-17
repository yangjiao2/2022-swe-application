
Count = how many 1


Count[j] = count[j&(j-1)] +1

for(j -> 0 - 1<<m-1){
i= Count[j] = count[j&(j-1)] +1
	for(int k = 0;k<m;k++){
        if (j>>k) & 1 == 0: continue
        p = count[j] - 1
		Dp[j] = max(  Dp[j - (1 << k)]+score[p][k], Dp[j]  )
	}
}
Return dp[(1<<m)-1];


- Flip last one bit: mask & (mask - 1)


- score[i][j] = (sys[i][k]^mts[j][k])^1
