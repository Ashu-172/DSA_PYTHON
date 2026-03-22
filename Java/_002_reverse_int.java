import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

// https://leetcode.com/problems/reverse-integer/description/

public class _002_reverse_int {
    public static void main(String [] args){
        try{
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            int a = Integer.parseInt(reader.readLine());
            
            System.out.println("Reverse of "+a+" is: "+reverse(a));
            System.out.println("is "+a+" an armstrong number: "+(isArmStrong(a)==1?"True":"False"));
            printAllDivisors(a);
            ArrayList<Integer> output = new ArrayList<Integer>();
            printAllDivisorsRecursive(a, 1, output);
            System.out.println("List of devisiors of "+a+" is: "+output);
            System.out.println("Number "+a+" is "+(checkPrime(a, 1)?"":"not ")+"prime");

        }
        catch(Exception e){
            e.printStackTrace();
        }
    }

    private static int reverse(int x) {
        int rev = 0; // or make it long to store rev if it is greater than MAX or MIN (no need to divide MIN or MAX by 10)
        while(x>= 1 || x<=-1){
                if(rev > Integer.MAX_VALUE/10 || rev < Integer.MIN_VALUE/10)
                    return 0; // returning 0 when reverse number can not be stored in int (larger than max int value)

                rev = rev*10 + x%10;
                x = x/10;
        }
        return rev;
    }

    private static int isArmStrong(int x) {
        int orig = x;
        int sum = 0;
        while(x > 0){
            int last = x%10;
            sum += last*last*last;
            x/=10;
        }
        return sum==orig?1:0;
    }

    private static void printAllDivisors(int x){
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i=1; i*i<=x; i++){
            if(x%i == 0){
                res.add(i);
                if(x/i != i)
                    res.add(x/i);
            }
        }
        res.sort(null);
        System.out.println(res);
    }

    private static void printAllDivisorsRecursive(int x, int i, ArrayList<Integer> res){
        if(i*i > x)
            return;

        if(x%i == 0)
            res.add(i);
        printAllDivisorsRecursive(x, i+1, res);
        if(x%i == 0) 
            res.add(x/i);
    }

    private static boolean checkPrime(int x, int i){
        if(i*i >x)
            return true;
        if (x%i == 0 && i!=1)
            return false;
        return checkPrime(x, i+1);
    }
}
