/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pckg;

/**
 *
 * @author mehradhq
 */
import java.util.Scanner;
import java.nio.file.Paths;
import java.util.Arrays;
public class Problem22 {
    public static void main(String[] args){
        String msg = "";
        try (Scanner scanner = new Scanner (Paths.get("/Users/mehradhq/Downloads/Target.txt"))){
            
            while (scanner.hasNextLine()){
                msg += scanner.nextLine();
            }
        } catch(Exception e){
            System.out.println(e.getMessage());
        }
        String[] sp = msg.split(",");
        Arrays.sort(sp);
        System.out.println(sp);
        int sum = 0;
        for (int i = 0; i<sp.length; i++){
            System.out.println(sp[i]);
            String temp = sp[i];
            sum += (i+1)*score(temp);
        }
        System.out.println(sum);
    }
    
    public static int score(String t){
        int s = 0;
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toUpperCase().toCharArray();
        
        for (int i = 0; i<t.length(); i++){
            for (int j = 0; j<alphabet.length; j++){
                if (t.charAt(i) == alphabet[j]){
                    s+=(j+1);
                    break;
                }
            }
        }
        return s;
    }
    
}
