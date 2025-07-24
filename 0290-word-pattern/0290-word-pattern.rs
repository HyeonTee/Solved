use std::collections::HashMap;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let pattern_chars = pattern.chars().collect::<Vec<_>>();
        let s_words = s.split_whitespace().collect::<Vec<_>>();

        if pattern_chars.len() != s_words.len() {
            return false;
        }

        let mut char_to_word = HashMap::new();
        let mut word_to_char = HashMap::new();

        for (ch, word) in pattern_chars.iter().zip(s_words.iter()) {
            match (char_to_word.get(ch), word_to_char.get(word)) {
                (Some(w), _) if w != word => return false,
                (_, Some(c)) if c != ch => return false,
                (None, None) => {
                    char_to_word.insert(*ch, *word);
                    word_to_char.insert(*word, *ch);
                }
                _ => {}
            }
        }

        true
    }
}