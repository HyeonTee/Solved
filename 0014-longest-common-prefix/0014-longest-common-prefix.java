class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            boolean done = false;
            for (String str : strs) {
                if (i >= str.length() || c != str.charAt(i)) {
                    done = true;
                    break;
                }
            }
            if (done) {
                break;
            }
            sb.append(c);
        }

        return sb.toString();
    }
}