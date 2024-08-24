impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x = x.to_string();
        let m = x.len() / 2;

        x.bytes().take(m).eq(x.bytes().rev().take(m))
    }
}
