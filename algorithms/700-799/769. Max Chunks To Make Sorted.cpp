class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        if (arr.empty()) return 0;
        int currentMax = 0, res = 0;
        for (int i = 0; i < arr.size(); ++i){
            currentMax = max(currentMax, arr[i]);
            if(currentMax == i){
                res += 1;
            }
        }
        return res;
    }
};