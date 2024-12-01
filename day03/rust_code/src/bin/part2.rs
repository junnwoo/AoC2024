use std::fs::File;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_path= &args[1];
    let input_file = File::open(input_path).expect("Can't open file!");
    part2(input_file);
}

fn part2(_input_file: File) {
}
