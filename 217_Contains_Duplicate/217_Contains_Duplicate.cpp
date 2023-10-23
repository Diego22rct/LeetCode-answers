#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(const vector<int>& nums) {
        unordered_set<int> s;
        for (const auto& num : nums) {
            if (s.count(num) > 0) {
                return true;
            }
            s.emplace(num);
        }
        return false;
    }
};