impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 {
            return s;
        }

        let num_rows = num_rows as usize;
        let mut stacks = vec![String::new(); num_rows];

        for (i, ch) in s.chars().enumerate() {
            let row = Self::cycle(i, num_rows);
            stacks[row].push(ch);
        }

        stacks.concat()
    }

    fn cycle(i: usize, n: usize) -> usize {
        let cycle = (n - 1) * 2;
        let pos = i % cycle;

        if pos < n {
            pos
        } else {
            cycle - pos
        }
    }
}