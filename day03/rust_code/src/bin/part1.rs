use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::iter::zip;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_path = &args[1];
    let input_file = File::open(input_path).expect("Can't open file!");
    part1(input_file);
}

fn part1(_input_file: File) {
}

