class Solution {
public:
    int climbStairs(int n) {
        int prev = 1, curr = 1;
        int temp;
        for (int i = 0; i < n - 1; ++i){
            temp = curr;
            curr = prev + temp;
            prev = temp;
        }
        return curr;
    }
};