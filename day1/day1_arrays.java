import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


    

public class day1_arrays
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n;i++) 
        {
            arr[(i+n-d)%n] = sc.nextInt();
        }
        for(int i=0; i<n;i++) 
        {
            System.out.print(arr[i] + " ");
        }      
    }
}
