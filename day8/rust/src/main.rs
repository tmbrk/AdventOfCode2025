use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = if args.len() > 1 {
        &args[1]
    } else {
        "input.txt"
    };

    let content = fs::read_to_string(filename).expect("Unable to read file");
    let content = content.trim();

    println!("Part 1: {}", solve_part1(content));
    println!("Part 2: {}", solve_part2(content));
}

fn solve_part1(content: &str) -> i64 {
    let _lines: Vec<&str> = content.lines().collect();
    //let tree = KdTree::new(3);
    // TODO: Implement Part 1
    0
}

fn solve_part2(content: &str) -> i64 {
    let _lines: Vec<&str> = content.lines().collect();
    // TODO: Implement Part 2
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let content = fs::read_to_string("input_test.txt").expect("Unable to read test file");
        assert_eq!(solve_part1(content.trim()), 40);
    }
}
