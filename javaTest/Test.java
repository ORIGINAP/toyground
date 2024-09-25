public class Test extends Rectangle{
    public string toString(){
        System.out.println(this.getArea());
    }
    public static void main(String[] args){
        Rectangle rec = new Rectangle(10,5);
        Test out_r = rec;
        out_r.toString();
    }
}