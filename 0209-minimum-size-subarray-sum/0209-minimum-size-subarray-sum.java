class Solution {
      public int minSubArrayLen(int target, int[] nums) {
          int answer = Integer.MAX_VALUE;
          int sum = 0;
          int lt = 0;

          for (int rt = 0; rt < nums.length; rt++) {
              sum += nums[rt];
              while (sum >= target) {           // 조건 만족하면 최대한 왼쪽을 줄인다
                  answer = Math.min(answer, rt - lt + 1);
                  sum -= nums[lt];
                  lt++;
              }
          }

          return answer == Integer.MAX_VALUE ? 0 : answer;
      }
  }