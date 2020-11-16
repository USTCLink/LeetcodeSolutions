class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty()) return 0;
        int n = nums.size();
        if (n == 1) return nums[0];
        int prev = nums[0], curr = max(nums[0], nums[1]);
        int temp;
        for (int i = 2; i < n; ++i){
            temp = curr;
            curr = max(prev + nums[i], temp);
            prev = temp;
        }
        return curr;
    }
};