class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        StringBuilder[] stacks = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            stacks[i] = new StringBuilder();
        }
        for (int i = 0; i < s.length(); i++) {
            stacks[cycle(i, numRows)].append(s.charAt(i));
        }

        for (int i = 1; i < numRows; i++) {
            stacks[0].append(stacks[i]);
        }

        return stacks[0].toString();
    }

    int cycle(int i, int n) {
        int cycle = (n - 1) * 2;
        int pos = i % cycle;

        return pos < n ? pos : cycle - pos;
    }
}