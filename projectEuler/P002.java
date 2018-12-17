package me.nionata.euler;

public class P002 {
	
	public static int run() {
		int sum = 0;
		
		int x = 1;
		int y = 2; 
		
		while(x < 4000000) {
			if (x % 2 == 0) {
				sum += x;
			}
			
			int z = x + y;
			x = y;
			y = z;
		}
		return sum;
	}

}
