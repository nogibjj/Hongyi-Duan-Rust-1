fn main() {
    println!("Rust standalone execution: Testing Fibonacci calculation.");
    
    let n = 10; // Example input for testing Fibonacci
    let result = calculate_fibonacci(n);
    
    println!("Fibonacci of {} is: {}", n, result);
}

// A simple Fibonacci calculation for local Rust testing.
fn calculate_fibonacci(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2),
    }
}
