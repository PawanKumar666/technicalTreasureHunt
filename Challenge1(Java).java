// Java program to check if a number
// is a krishnamurthy number.
import java.util.*;
import java.io.*;
public class Krishnamurthy {
    static int factorial(int n)
    {
        int fact = 1;
        while (n != 0) {
            fact = fact * n;
            n--;
        }
        return fact;
    }
    static int result_generator(int n)
    {
        int sum = 0;
  
        int temp = n;
        while (temp != 0) {
            sum += factorial(temp % 10);

            temp = temp / 10;
        }
  
        return (sum);
    }

    public static void main(String[] args)
    {
        int key;
        int n = 273;  //Kelvin wants to know the melting point!!
        key = result_generator(n);
        key = factorial(n);
        System.out.println("The key to next Folder "+ key);
    }
}