impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x_str = x.to_string();
        let n = x_str.len();
        for i in 0..n / 2 + 1 {
            if x_str.chars().nth(i).unwrap() != x_str.chars().nth(n - i - 1).unwrap() {
                return false;
            }
        }
        true
    }
}
