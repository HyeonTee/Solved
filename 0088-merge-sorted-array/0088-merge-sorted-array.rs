impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &Vec<i32>, n: i32) {
        let mut i = m as i32 - 1;
        let mut j = n as i32 - 1;
        let mut k = (m + n) as i32 - 1;

        while j >= 0 {
            if i >= 0 && nums1[i as usize] > nums2[j as usize] {
                nums1[k as usize] = nums1[i as usize];
                i -= 1;
            } else {
                nums1[k as usize] = nums2[j as usize];
                j -= 1;
            }
            k -= 1;
        }
    }
}