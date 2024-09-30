"""Description:
Description:

We want to generate a function that computes the series starting from 0 and ending until the given number.

Example:
Input:

> 6
Output:

0+1+2+3+4+5+6 = 21

Input:

> -15
Output:

-15<0

Input:

> 0
Output:

0=0""";

public class SequenceSum{

    public static String showSequence(int value){
      int sum = 0;
      StringBuilder result = new StringBuilder();
      if(value < 0){
        return value + "<0";
      }
      else if (value == 0){
        return "0=0";
      }
      else{
        for(int i = 0; i <= value; i ++){
          sum += i;
          result.append(i);
          if (i < value) {
            result.append("+");
           }
       }
       return result.append(" = ").append(sum).toString();
      }
    }
  
    public static void main(String args[]){
      int param=Integer.parseInt(args[0]);
      SequenceSum.showSequence(param);
    }
  }