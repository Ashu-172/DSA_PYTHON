import java.io.BufferedReader;
import java.io.InputStreamReader;

// https://www.youtube.com/watch?v=1xNbjMdbjug&t=3564s
public class _001_GCD_of_two_numbers {
    public static void main(String [] args){
        try{
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            int a = Integer.parseInt(reader.readLine());
            int b = Integer.parseInt(reader.readLine());
            
            System.out.println("GCD of "+a+" and "+b+" is: "+calculateGcd(a,b));
            System.out.println(b+" Power of "+a+" is: "+powerExp(a, b));
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }

    // Euclidean algorithm: GCD(a,b) = GCD(a-b, b) or GCD(a,b) = GCD(a, b-a) 
    // or GCD(a,b) = GCD(a%b, b) or GCD(a,b) = GCD(a, b%a)
    // where a >= b
    // Time complexity: O(log(min(a,b)))
    private static int calculateGcd(int a, int b){
        if(a == 0)
            return b;

        return calculateGcd(Math.max(a,b)%Math.min(a,b), Math.min(a,b));
    }

    private static long powerExp(int a, int b){
        /*
        Solution 1
        if (b==1)
            return a;
        boolean is_odd = b%2!=0?true:false;
        long res = powerExp(a, b/2);
        if (is_odd)  
            return res*res*a;
        else
            return res*res;
        */
        
        /* 
        a=3,b=5
        is_odd = true 
            a=3, b=2
            is_odd=false
                a=3, b=1
                return 3
            return 3*3=9
        return 9*9*3=243
        */
        // Solution 2
        if (b==0)
            return 1;

        if(b%2==0)
            return powerExp(a*a, b/2);
        else
            return a*powerExp(a*a, b/2);

    }
    
    private static void powerExpLoop(int a, int b){
        // Solution 3 with loop
       int ans=1;
       while(b>0){
            if(b%2==0){
                a=a*a;
            }
            else{
                ans = ans*a;
                a= a*a;
            }
            b=b/2;
       }
       System.out.println(ans);
       /*
       ans=1 a=2 b=5
       b->5, ans=1*2=2, a=2*2=4,
       b->2, ans=2, a=4*4=16
       b->1, ans=2*16=32, a=16*16
       */
    }
}

