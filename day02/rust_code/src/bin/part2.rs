use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::cmp::min;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_path = &args[1];
    let input_file: File = File::open(input_path).expect("Can't open file!");
    let results = part2(input_file);
    println!("Safe reports: {}", results);
}

fn part2(input_file: File) -> i32 {
    let reader = BufReader::new(input_file);
    let mut safe_reports: i32 = 0;
    for line in reader.lines() {
        let input = line.expect("Could not read the lines from input file.");
        let levels: Vec<i32> = input
            .split_whitespace()
            .map(|s| s.parse().expect("Could not parse int"))
            .collect();
        let (is_valid, errors) = is_valid_report(&levels);
        if is_valid {
            safe_reports += 1;
        } else if errors <= 2 {
            for i in 0..levels.len() {
                let mut new_report: Vec<i32> = vec![];
                for (j, el) in levels.iter().enumerate() {
                    if i != j {
                        new_report.push(*el);
                    }
                }
                let (is_valid, _) = is_valid_report(&new_report);
                if is_valid {
                    safe_reports += 1;
                    break;
                }
            }
        }
    }
    safe_reports
}

fn is_valid_report(report: &Vec<i32>) -> (bool, i32) {
    let (v1, e1) = is_valid_report_orientation(report, true);
    let (v2, e2) = is_valid_report_orientation(report, false);
    return (v1 || v2, min(e1, e2));
}

fn is_valid_report_orientation(report: &Vec<i32>, increasing: bool) -> (bool, i32) {
    let mut errors: i32 = 0;
    for slice in report.windows(2) {
        let first = slice[0];
        let second = slice[1];
        if increasing {
            if second - first > 3 || second - first <= 0 {
                errors += 1;
            }
        } else {
            if first - second > 3 || first - second <= 0 {
                errors += 1;
            }
        }
    }
    if errors == 0 {
        return (true, 0);
    }
    (false, errors)
}
