use std::collections::HashMap;
use std::fs::read_to_string;
use std::{env, vec};

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut input_path = &args[1];
    // let input_file: File = File::open(input_path).expect("Could not open input file!");
    let input_data = read_to_string(&mut input_path).expect("Could not read file");
    let parts: Vec<String> = input_data.split("\n\n").map(|s| s.to_string()).collect();
    let ordering_rules: Vec<String> = parts[0].split_whitespace().map(|s| s.to_string()).collect();
    let updates: Vec<String> = parts[1].split_whitespace().map(|s| s.to_string()).collect();
    let mut ans = 0;
    let order = parse_ordering(&ordering_rules);

    for update in updates {
        let sequence: Vec<i32> = update
            .split(",")
            .map(|s| s.to_string().parse().expect("Could not parse number"))
            .collect();
        println!("Working with: {:?}", sequence);
        let (mut found, mut number_move) = get_invalid_number(&sequence, &order);
        while found {
            println!("The invalid number is: {}", number_move);
            let empty_vec : Vec<i32>= vec!();
            let new_sequence = insert_correct(
                &sequence,
                number_move,
                match &order.get(&number_move) {
                    Some(s)=> s,
                    None => &empty_vec
                },
            );
            println!("The new sequence is: {:?}", new_sequence);
            ans += validate_update(&new_sequence, &order);
            (found, number_move) = get_invalid_number(&new_sequence, &order);
        }
    }

    println!("Answer is: {}", ans);
}

fn insert_correct(sequence: &Vec<i32>, number: i32, order: &Vec<i32>) -> Vec<i32> {
    let mut new_sequence: Vec<i32> = vec![];
    let mut found: bool = false;
    for c in sequence.iter() {
        if !order.contains(c) && !found{
            new_sequence.push(number);
            found = true;
        } 
        if *c!=number {
            new_sequence.push(*c);
        }
    }
    new_sequence
}

fn parse_ordering(ordering_rules: &Vec<String>) -> HashMap<i32, Vec<i32>> {
    let mut order: HashMap<i32, Vec<i32>> = HashMap::new();
    for rule in ordering_rules {
        let numbers: Vec<String> = rule.split("|").map(|s| s.to_string()).collect();
        order
            .entry(numbers[1].parse().expect("Could not parse number"))
            .or_insert(vec![])
            .push(numbers[0].parse().expect("Could not parse number"));
    }
    order
}

fn get_invalid_number(sequence: &Vec<i32>, order: &HashMap<i32, Vec<i32>>) -> (bool, i32) {
    let mut last_number: &i32 = &sequence[0];
    for (i, c) in sequence.iter().enumerate() {
        if i > 0 {
            let this_set = match order.get(c) {
                Some(set) => set,
                None => {
                    return (true, *c);
                }
            };
            if !this_set.contains(last_number) {
                return (true, *c);
            }
        }
        last_number = c;
    }
    println!("=> true");
    (false, 0)
}

fn validate_update(sequence: &Vec<i32>, order: &HashMap<i32, Vec<i32>>) -> i32 {
    let mut last_number: &i32 = &sequence[0];
    for (i, c) in sequence.iter().enumerate() {
        if i > 0 {
            let this_set = match order.get(c) {
                Some(set) => set,
                None => {
                    println!("=> false");
                    return 0;
                }
            };
            if !this_set.contains(last_number) {
                println!("=> false");
                return 0;
            }
        }
        last_number = c;
    }
    println!("=> true");
    let mid_index: usize = sequence.len() / 2;
    sequence[mid_index]
}
