use std::io::{BufRead, BufReader};
use std::env;
use std::fs::File;
use regex::Regex;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = &args[1];
    let input_file: File = File::open(input).expect("Can't open file!");
    let ans = part1(input_file);
    println!("The answer is: {}", ans);
}

fn part1(input_file: File) -> i32 {
    let reader = BufReader::new(input_file);
    let re = Regex::new(r"mul\((\d+,\d+)\)").unwrap();
    let mut ans = 0;
    for line in reader.lines() {
        let input_string = line.expect("Could not read line from input file");
        for capture in re.captures_iter(&input_string) {
            let matches = capture.get(1).unwrap().as_str();
            let digits: Vec<i32> = matches.split(",").map(|s| s.parse().expect("Could not parse numbers")).collect();
            ans += digits[0] * digits[1];
        }
    }
    ans
}