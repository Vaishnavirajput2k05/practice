import java.util.Scanner;

public class DigitSum {
    static  int Sumdigit(int temp){
        
        int sum = 0;
        int i=0;
       for( i=0;temp != 0;i++) {
           int k=temp%10;
            sum += k;
            temp /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:");
        int input = sc.nextInt();
       

        System.out.println("Sum:" + Sumdigit(input));
        sc.close();
    }
}