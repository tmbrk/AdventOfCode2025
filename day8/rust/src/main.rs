use std::env;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

use kdtree::ErrorKind;
use kdtree::KdTree;
use kdtree::distance::squared_euclidean;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = if args.len() > 1 {
        &args[1]
    } else {
        "input.txt"
    };

    let file = File::open(filename).expect("Unable to open file");
    let content = BufReader::new(file);

    println!("Part 1: {}", solve_part1(content).unwrap());
    //println!("Part 2: {}", solve_part2(content));
}

fn solve_part1(content: BufReader<File>) -> Option<i64> {
    let mut tree = KdTree::new(3);

    for (index, line) in content.lines().enumerate() {
        let line = line.ok()?;
        println!("{}", line);
        let coords: Vec<f64> = line
            .split(',')
            .filter_map(|s| s.trim().parse().ok())
            .collect();

        // 3. Add to tree if coordinates match our dimensions
        if coords.len() == 3 {
            let point = [coords[0], coords[1], coords[2]];
            // .add(coordinates, data)
            tree.add(point, index as i64).ok()?;
        }
    }

    let _nearest_box = find_nearest(&tree);

    // TODO: Implement Part 1
    Some(0)
}

fn find_nearest(tree: &KdTree<f64, i64, [f64; 3]>) -> Result<Vec<(f64, i64)>, ErrorKind> {
    // Inside your solve_part1 function, after the loop:

    let query_point = [10.0, 5.0, 2.0]; // The point you're looking for
    let num_results = 1; // How many neighbors to find

    // .nearest(target, count, distance_fn)
    let results = tree
        .nearest(&query_point, num_results, &squared_euclidean)
        .expect("Search failed");

    if let Some((dist, index)) = results.first() {
        println!(
            "Closest point was from line {}, squared distance: {}",
            index, dist
        );
    }

    Ok(results
        .into_iter()
        .map(|(dist, &idx)| (dist, idx))
        .collect())
}
/*
fn solve_part2(content: ) -> i64 {
    let _lines: Vec<&str> = content.lines().collect();
    // TODO: Implement Part 2
    0
}
*/

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let file = File::open("input_test.txt").expect("Unable to open file");
        let content = BufReader::new(file);

        assert_eq!(solve_part1(content), Some(40));
    }
}
