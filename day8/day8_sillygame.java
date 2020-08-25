import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class day8_sillygame {
      static int sieveOfEratosthenes(int n) 
    { int count=0;
        boolean prime[] = new boolean[n+1]; 
        
        for(int p = 2; p*p <=n; p++) 
        { 
           
            if(prime[p] ==false)  
            { 
                for(int i = p*p; i <= n; i += p) 
                    prime[i] = true; 
            } 
        } 
          
         
        for(int i = 2; i <= n; i++) 
        { 
            if(prime[i] == false) 
               count++;
        }

    return count;} 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int g = in.nextInt();
        for(int i = 0; i< g; i++){
            int n = in.nextInt();
           
            if(sieveOfEratosthenes(n) % 2 == 0)
                System.out.println("Bob");
            else
                System.out.println("Alice"); 
        }
    }
}