public class Rectangle implements Shape{
    double length=0;
    double width=0;
    Rectangle(double len, double width){
        this.length = len;
        this.width = width;
    }

    public double getArea(){
        double result = (double)this.length*this.width;
        return result;
    }

    public string toString(){
        System.out.print();
    }
}