use regex::Regex;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = &args[1];
    let input_file: File = File::open(input).expect("Can't open file!");
    let ans = part2(input_file);
    println!("The answer is: {}", ans);
}

fn part2(input_file: File) -> i32 {
    let reader = BufReader::new(input_file);
    let mut ans = 0;
    for line in reader.lines() {
        let input_string = line.expect("Could not read line from input file");
        for do_string in input_string.split("do()") {
            let muls: Vec<&str> = do_string.split("don't()").collect();
            println!("muls: {:?}", muls);
            ans += part1(&muls[0]);
        }
    }
    ans
}

fn part1(input_string: &str) -> i32 {
    let mut sum = 0;
    let re = Regex::new(r"mul\((\d+,\d+)\)").unwrap();
    for capture in re.captures_iter(input_string) {
        let matches = capture.get(1).unwrap().as_str();
        let digits: Vec<i32> = matches
            .split(",")
            .map(|s| s.parse().expect("Could not parse numbers"))
            .collect();
        println!("digits: {:?}", digits);
        sum += digits[0] * digits[1];
    }
    sum
}
