use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_path = &args[1];
    let input_file: File = File::open(input_path).expect("Can't open file!");
    let results = part1(input_file);
    println!("Safe reports: {}", results);
}

fn part1(input_file: File) -> i32 {
    let reader = BufReader::new(input_file);
    let mut safe_reports: i32 = 0;
    for line in reader.lines() {
        let input = line.expect("Could not read the lines from input file.");
        let levels: Vec<i32> = input
            .split_whitespace()
            .map(|s| s.parse().expect("Could not parse int"))
            .collect();
        if is_valid_report(&levels) {
            safe_reports += 1;
        }
    }
    safe_reports
}

fn is_valid_report(report: &Vec<i32>) -> bool {
    let increasing = report[1] - report[0] > 0;
    for slice in report.windows(2) {
        let first= slice[0];
        let second = slice[1];
        if increasing {
            if second - first > 3 || second - first <= 0 {
                return false;
            }
        }
        else {
            if first - second > 3 ||  first - second <= 0 {
                return false;
            }
        }
    }
    true
}
