use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_path= &args[1];
    let input_file = File::open(input_path).expect("Can't open file!");
    let results: u32 = part2(input_file);
    println!("The total similarity score is: {}", results);
}

fn part2(input_file: File) -> u32 {
    let reader = BufReader::new(input_file);
    let mut left_numbers: Vec<u32> = vec![];
    let mut right_number_occurances: HashMap<u32, u32> = HashMap::new();
    for line in reader.lines() {
        let input = match line {
            Ok(line) => line,
            Err(error) => panic!("Can't read line, error: {}", error),
        };
        let mut numbers = input.split_whitespace();
        let first = numbers.next();
        let second = numbers.next();
        let left: u32 = first.as_deref().unwrap().parse().unwrap();
        let right: u32 = second.as_deref().unwrap().parse().unwrap();
        left_numbers.push(left);
        *right_number_occurances.entry(right).or_insert(0) += 1;
    }
    let mut similarity_score: u32 = 0;
    for num in left_numbers.iter() {
        let occurances: u32 = match right_number_occurances.get(num) {
            Some(num) => *num,
            None => 0 
        };
        similarity_score += get_similarity_score(*num, occurances)
    }
    similarity_score
}

fn get_similarity_score(number: u32, occurances: u32) -> u32 {
    number * occurances
}
