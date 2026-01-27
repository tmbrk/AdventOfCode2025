use std::env;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

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
    let mut points: Vec<[f64; 3]> = Vec::new();

    for line in content.lines() {
        let line = line.ok()?;
        let coord: Vec<f64> = line
            .split(',')
            .filter_map(|s| s.trim().parse().ok())
            .collect();

        if coord.len() == 3 {
            points.push([coord[0], coord[1], coord[2]]);
        }
    }

    let connections = if points.len() <= 20 { 10 } else { 1000 };
    let mut edges = all_edges(&points)?;
    edges.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

    let mut uf = UnionFind::new(points.len());
    for (_, i, j) in edges.into_iter().take(connections) {
        uf.union(i, j);
    }

    let mut sizes = uf.group_sizes();
    sizes.sort_unstable_by(|a, b| b.cmp(a));
    let product_top3: usize = sizes.into_iter().take(3).product();
    Some(product_top3 as i64)
}

fn all_edges(points: &[[f64; 3]]) -> Option<Vec<(f64, usize, usize)>> {
    let mut edges = Vec::new();
    for i in 0..points.len() {
        for j in (i + 1)..points.len() {
            let dist = squared_euclidean(&points[i], &points[j]);
            edges.push((dist, i, j));
        }
    }
    Some(edges)
}

struct UnionFind {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, a: usize, b: usize) {
        let mut ra = self.find(a);
        let mut rb = self.find(b);
        if ra == rb {
            return;
        }
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }

    fn group_sizes(&mut self) -> Vec<usize> {
        let mut counts = vec![0; self.parent.len()];
        for i in 0..self.parent.len() {
            let root = self.find(i);
            counts[root] += 1;
        }
        counts.into_iter().filter(|&c| c > 0).collect()
    }
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
