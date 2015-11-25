// Project Euler Problem #1

fn main() {

	let mut sum:i32 = 0;
	let mut i:i32 = 1;

	while 3*i < 1000 {
		sum += 3*i; 
		i+=1;
	}

	i = 1;
	
	while 5*i < 1000 {
		if 5*i % 3 != 0{
		    sum += 5*i;
		}
		i+=1;
    } 
 	println!("The sum of all natural numbers <1000 and divisible by 3 or 5 is: {}", sum);
}
