import java.util.Scanner;

public class CaseSeparator{

static void  LowerCase(String input){
int i=0;
while(i<input.length()){
char lc=input.charAt(i);
if(Character.isLowerCase(lc)){
System.out.print(lc);
}
i++;
}}

static  void UpperCase(String input){
int i=0;
while(i<input.length()){
char uc=input.charAt(i);
if(Character.isUpperCase(uc)){
System.out.print(uc);
}
i++;
}}

public static void main(String [] args){

Scanner sc= new Scanner(System.in);
System.out.print("Enter a string:");
String input=  sc.next();

UpperCase(input);
System.out.println();
LowerCase(input);

sc.close();
}
}