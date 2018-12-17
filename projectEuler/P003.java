package me.nionata.euler;

public class P003 {
	
	public static int run() {
		double num = 0;
		
		double i = 0;
		
		while (i < 600851475143.0) {
			int counter = 0;
			
			for(int q = 2; q < i; q++) {
				if(i % q == 0) {
					counter++;
				}
			}
			
			if(counter == 0) {
				if(i % 600851475143.0 == 0) {
					num = i;
				}
			}
			
		}
		
		return (int)num;
	}

}
