use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::iter::zip;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_path = &args[1];
    let input_file = File::open(input_path).expect("Can't open file!");
    let results = part1(input_file);
    println!("The total distance is: {}", results);
}

fn part1(input_file: File) -> i32 {
    let reader = BufReader::new(input_file);
    let mut left_numbers: Vec<i32> = vec![];
    let mut right_numbers: Vec<i32> = vec![];
    for line in reader.lines() {
        let input = match line {
            Ok(line) => line,
            Err(error) => panic!("Can't read line, error: {}", error),
        };
        let mut numbers = input.split_whitespace();
        let first = numbers.next();
        let second = numbers.next();
        let left = first.as_deref().unwrap();
        let right = second.as_deref().unwrap();
        left_numbers.push(left.parse().unwrap());
        right_numbers.push(right.parse().unwrap());
    }
    left_numbers.sort();
    right_numbers.sort();
    let mut distance = 0;
    for (left, right) in zip(left_numbers, right_numbers) {
        distance += get_distance(left, right);
    }
    distance
}

fn get_distance(left: i32, right: i32) -> i32 {
    let distance: i32 = left - right;
    distance.abs()
}
