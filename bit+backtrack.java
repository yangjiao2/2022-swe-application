
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
// 1601. Maximum Number of Achievable Transfer Requests


class Solution {
    public int maximumRequests(int n, int[][] requests) {
        int max = 0;
        int mask = (1 << requests.length) - 1;
        while (mask > 0) {
            if (isAchiv(n, requests, mask)) {
                max = Math.max(max, Integer.bitCount(mask));
            }
            mask--;
        }

        return max;
    }

    private boolean isAchiv(int n, int[][] requests, int mask) {
        int[] count = new int[n];
        int len = requests.length;

        for (int i = 0; i < len; i++) {
            if ((mask & (1 << i)) == 0) {
                continue;
            }

            int from = requests[i][0], to = requests[i][1];
            count[from]--;
            count[to]++;
        }

        for (int i = 0; i < n; i++) {
            if (count[i] != 0) {
                return false;
            }
        }

        return true;
    }
}
