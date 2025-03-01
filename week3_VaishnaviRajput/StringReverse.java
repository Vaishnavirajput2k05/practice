import java.util.Scanner;

public class StringReverse {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string:");
        String input = sc.nextLine();
        System.out.print("Reversed string:");

        int i = 0;
        while (i < input.length()) {
            System.out.print(input.charAt(input.length() - i - 1));

        }
        System.out.println(" ");
        sc.close();
    }
}