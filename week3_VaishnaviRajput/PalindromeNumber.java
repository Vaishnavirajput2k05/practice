import java.util.Scanner;

public class PalindromeNumber {
  static int count(int n) {

    int digit = 0;
    while (n > 0) {
      n /= 10;
      digit += 1;

    }
    return digit;
  }

  public static void main(String [] args) {
    Scanner sc=new Scanner(System.in);
    System.out.print("Enter a number:");
    int n = sc.nextInt();

    int temp=n;
    int i = 0;
    int[] k = new int[count(n)];
    while (temp > 0) {
      k[i] = temp % 10;
      temp /= 10;
      i++;
    }
    boolean Ispalindrome = true;

    int q=0;
    for (q = 0; q < k.length / 2; q++) {
      if (k[q] != k[k.length - q- 1]) {
        Ispalindrome = false;
        break;
      }

    }
    if(Ispalindrome){
      System.out.print("True");
    }
    else{
      System.out.print("False");

    }
    
    
      sc.close();
  }
}
