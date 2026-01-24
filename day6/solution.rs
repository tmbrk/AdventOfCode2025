use std::env;
use std::fs;
use std::iter::zip;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = if args.len() > 1 { &args[1] } else { "input.txt" };

    let content = fs::read_to_string(filename).expect("Unable to read file");

    solve_part1(&content);
    solve_part2(&content);
}

fn solve_part1(content: &str) {
    let lines: Vec<&str> = content.lines().collect();
    if lines.is_empty() {
        return;
    }

    // Parse all lines as rows of tokens
    let mut data: Vec<Vec<String>> = lines.iter()
        .map(|line| line.split_whitespace().map(|s| s.to_string()).collect())
        .collect();

    if data.is_empty() {
        return;
    }

    // Last row contains operators
    let operators = data.pop().unwrap();
    
    // The remaining rows are operands. 
    // We need to transpose: treat the i-th element of each row as a column of operands.
    // Note: The python code assumes a rectangular shape for operands based on genfromtxt.
    // However, split_whitespace might result in varying lengths if the file isn't perfect, 
    // but the problem implies a structure.
    
    let num_columns = operators.len(); 
    // Assuming all operand rows have the same number of columns as operators (based on the problem structure)
    // or we just zip. The Python code zips operand_columns and operators.

    let mut results = Vec::new();

    for col_idx in 0..num_columns {
        let mut operands = Vec::new();
        for row in &data {
            if col_idx < row.len() {
                if let Ok(num) = row[col_idx].parse::<i64>() {
                    operands.push(num);
                }
            }
        }
        
        let op = &operators[col_idx];
        if !operands.is_empty() {
            let res = calculate(&operands, op);
            results.push(res);
        }
    }

    let total: i64 = results.iter().sum();
    println!("Part 1: {}", total);
}

fn solve_part2(content: &str) {
    let lines: Vec<&str> = content.lines().collect();
    if lines.is_empty() {
        return;
    }

    // Pad lines to max length to form a grid
    let max_len = lines.iter().map(|l| l.len()).max().unwrap_or(0);
    let grid: Vec<Vec<char>> = lines.iter()
        .map(|line| {
            let mut chars: Vec<char> = line.chars().collect();
            while chars.len() < max_len {
                chars.push(' ');
            }
            chars
        })
        .collect();

    // Last row is operators (grid[grid.len() - 1])
    let last_row_idx = grid.len() - 1;
    let operator_row = &grid[last_row_idx];

    // Numbers are grid[0..last_row_idx]
    let number_grid = &grid[0..last_row_idx];

    // Transpose logic for numbers
    // Iterate columns
    let mut column_strings: Vec<String> = Vec::new();
    for col in 0..max_len {
        let mut s = String::new();
        for row in number_grid {
            s.push(row[col]);
        }
        column_strings.push(s.trim().to_string());
    }

    // Group non-empty strings
    let mut operand_groups: Vec<Vec<i64>> = Vec::new();
    let mut current_group: Vec<i64> = Vec::new();
    
    // The python code uses groupby on (x == "").
    // "1", "24", "356", "", "369", ...
    // Group 1: 1, 24, 356
    // Group 2: 369...
    
    for s in column_strings {
        if s.is_empty() {
            if !current_group.is_empty() {
                operand_groups.push(current_group);
                current_group = Vec::new();
            }
        } else {
            if let Ok(num) = s.parse::<i64>() {
                current_group.push(num);
            }
        }
    }
    if !current_group.is_empty() {
        operand_groups.push(current_group);
    }

    // Filter operators from last row
    let valid_operators: Vec<String> = operator_row.iter()
        .filter(|c| !c.is_whitespace())
        .map(|c| c.to_string())
        .collect();

    let mut results = Vec::new();
    for (operands, op) in zip(operand_groups, valid_operators) {
        let res = calculate(&operands, &op);
        results.push(res);
    }

    let total: i64 = results.iter().sum();
    println!("Part 2: {}", total);
}

fn calculate(operands: &[i64], op: &str) -> i64 {
    if operands.is_empty() {
        return 0;
    }
    let mut acc = operands[0];
    for &val in &operands[1..] {
        match op {
            "*" => acc *= val,
            "+" => acc += val,
            "-" => acc -= val,
            "/" => acc /= val, // integer division as per python's operator.truediv with integers?
                               // Wait, python operator.truediv returns float. 
                               // Advent of code usually sticks to int math. 
                               // Let's check python code imports.
                               // from functools import reduce
                               // import operator
                               // OPERATORS = {"/": operator.truediv}
                               // If the input produces integers that divide evenly, float is fine, but result is cast to sum?
                               // The python return type hint says 'int'. 
                               // Let's assume integer division or exact division.
                               // In Rust, `/` on integers is integer division.
            _ => panic!("Unknown operator: {}", op),
        }
    }
    acc
}
