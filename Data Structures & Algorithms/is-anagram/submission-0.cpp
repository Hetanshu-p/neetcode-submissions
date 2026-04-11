#include <map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> count = {};
        if (s.length() != t.length()) {return false;}
        for (int i = 0; i < s.length(); i++) {
            if (count.contains(s[i])) { 
                count[s[i]]++; 
            }
            else {
                count[s[i]] = 1; 
            }
        }
        for (int i = 0; i < t.length(); i++) {
            count[t[i]]--; 
            if (count[t[i]] == 0) {
                count.erase(t[i]);
            }
 
        }
        if (count.empty() == 1) {
            return true;
        }
        return false; 
    }
};
