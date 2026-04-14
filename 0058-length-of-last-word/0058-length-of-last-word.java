class Solution {
    public int lengthOfLastWord(String s) {
        String[] tokens = s.split(" ");
        String word = tokens[tokens.length - 1];

        return word.length();
    }
}