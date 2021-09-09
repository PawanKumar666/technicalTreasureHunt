//Have you imported the necessities?Check!
public class Main {
    public void main(String[] args) {
        String[] words = {"kctyugam"};
         String[] morse = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        Set<String> ans = new HashSet<String>();
        for(String word : words){
            char[] each = word.tocharArray();
            StringBuilder temp = new StringBuilder();
            for(char x : each){
                temp.append(morse[ x -'97']); //I think you need the help of ASCII table
            }
            ans.add(word.toString());
        }
        int res = ans.size();
        
        System.out.println(ans);
    }
}