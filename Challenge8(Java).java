//Execute all the functions in order of the source without modifying any values inside them to get the actual key
class yugam{
 void lock(){
System.out.println('E'+'R'+'R'+'O'+'R');
}
void key(){
Integer a=129;
Integer b =129;
if(a==b){
System.out.println((('I'+'S')%a)+b);
}
}
}
class treasure extends yugam{
void lock(){
    if(true){
System.out.println('F'+'U'+'N');
break;
}
}
}
public class Main{
public static void main(String[]args){
//For Object Creation
//\u000d yugam obj = new yugam();
yugam obj = new yugam();
obj.lock();
}
public static void main(String args){
treasure trail= new treasure();
trail.lock();
trail.key();
System.out.println("If you got an O/P: Verify - > Your key will be of length 9");
return;
}
}