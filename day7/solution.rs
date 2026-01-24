use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = if args.len() > 1 { &args[1] } else { "input.txt" };

    let content = fs::read_to_string(filename).expect("Unable to read file");
    let content = content.trim();

    println!("Part 1: {}", content);
    println!("Part 11: {}", solve_part1(content));
    println!("Part 2: {}", solve_part2(content));
}

fn solve_part1(content: &str) -> i64 {
    let _lines: Vec<&str> = content.lines().collect();
    // TODO: Implement Part 1
    0
}

fn solve_part2(content: &str) -> i64 {
    let _lines: Vec<&str> = content.lines().collect();
    // TODO: Implement Part 2
    0
}
