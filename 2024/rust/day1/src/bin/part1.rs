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
        let input = line.expect("Could not read lines of input file");
        let mut numbers = input.split_whitespace();
        let left_number = numbers
            .next()
            .expect("Could not extract left number")
            .parse()
            .expect("Could not parse left number");
        let right_number = numbers
            .next()
            .expect("Could not extract right number")
            .parse()
            .expect("Could not parse right number");
        left_numbers.push(left_number);
        right_numbers.push(right_number);
    }
    left_numbers.sort();
    right_numbers.sort();
    let mut distance = 0;
    for (left, right) in zip(left_numbers, right_numbers) {
        distance += (left - right).abs()
    }
    distance
}
