use std::collections::HashMap;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let pattern_chars = pattern.chars().collect::<Vec<char>>();
        let s_words = s.split_whitespace().collect::<Vec<&str>>();

        if pattern_chars.len() != s_words.len() {
            return false;
        }

        let mut result = true;
        let mut map: HashMap<char, &str> = HashMap::new();
        for i in 0..pattern_chars.len() {
            if map.contains_key(&pattern_chars[i]) {
                if map.get(&pattern_chars[i]).unwrap() != &s_words[i] {
                    result = false;
                    break;
                }
            } else {
                if map.values().any(|&v| v == s_words[i]) {
                    result = false;
                    break;
                }
                map.insert(pattern_chars[i], s_words[i]);
            }
        }

        result
    }
}