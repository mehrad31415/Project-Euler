/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pckg;

/**
 If p=120 is the perimeter of a right angle triangle with integral length sides, we can have three possible solutions.
For which value of p <= 1000 is the number of solutions maximised?
 * @author mehradhq
 */
import java.util.ArrayList;

public class Problem39 {

    public static void main(String[] args) {
        // we have put the maximum 0.
        int max = 0;
        // also the perimeter corresponding to the maximum number of combinations has been initialized.
        int perimeter = 0;
        // we check all the perimeters from 1 -- 1000.
        for (int p = 1; p <= 1000; p++) {
            // this is a counter for the number of correct combinations.
            int counter = 0;
            // the largest edge has the minimum of p/3 (if lower its not the largest) and the maximum of p/2 (if higher the tri-inequality will not hold).
            int lowerBound = p/3;
            int higherBound = p / 2;
            // we examine all the combinations where the biggest edge is defined.
            for (int j = lowerBound; j <= higherBound; j++) {
                // the sum of the other two edges.
                int sumOfTwoEdges = p - j;
                // the second biggest edge cannot be below sumOfTwoEdges/2 because if both below this then the sum will be under sumOfTwoEdges.
                int lowerBound2 = sumOfTwoEdges/2;
                for (int l = lowerBound2; l < sumOfTwoEdges; l++) {
                    // we check the combination of the three edges.
                    if (rightTri(j, l, sumOfTwoEdges - l)) {
                        counter++;
                    }
                }
            }
            // if the number exceeds the max we change the max.
            if (counter > max) {
                max = counter;
                perimeter = p;
            }
        }
        System.out.println(perimeter);
    }

    // this method detects whether three numbers form a right triangle or not.
    // this means we have to check whether they adhere to the triangle inequality and pythagoreon theorem.
    public static boolean rightTri(int a, int b, int c) {
        ArrayList<Integer> t = new ArrayList<>();
        t.add(a);
        t.add(b);
        t.add(c);
        int temp = Math.max(Math.max(a, b), c);
        t.remove(Integer.valueOf(temp));
        int s = 0;
        int s2 = 0;
        for (int i : t) {
            s += Math.pow(i, 2);
            s2 += i;
        }
        return s == Math.pow(temp, 2) && temp < s2;
    }

}
