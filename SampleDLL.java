import java.util.Scanner;

public class SampleDLL{
    static{
        System.loadLibrary(libname:"SampleDLL");
    }

    public native int add(int num1,int num2);

    public static void main(String args[]){
        Scanner scanner=new Scanner(System.in);
        int num1=0;
        int num2=0;
        System.out.println("DLL example addition operation");
        System.out.println("Enter first numver");
        num1=scanner.nextInt();
        System.out.println("Enter second number: ");
        num2=scanner.nextInt();
        System.out.println("Result: " + new SampleDLL().add(num1,num2))
    }
}