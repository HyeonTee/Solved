class Solution {
      public int lengthOfLongestSubstring(String s) {
          Map<Character, Integer> lastIndex = new HashMap<>();
          int answer = 0;
          int lt = 0;

          for (int rt = 0; rt < s.length(); rt++) {
              char c = s.charAt(rt);

              if (lastIndex.containsKey(c) && lastIndex.get(c) >= lt) {
                  lt = lastIndex.get(c) + 1;
              }

              lastIndex.put(c, rt);
              answer = Math.max(answer, rt - lt + 1);
          }

          return answer;
      }
  }