class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin() ,people.end());
        int i, j;
        for (i = 0, j = people.size() - 1; i <= j; j--) {
            if (people[i] + people[j] <= limit) {
                i++;
            }
        }
        return people.size() - 1 - j;
    }
};