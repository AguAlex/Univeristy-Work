#include <iostream>
class Vector{
private:
    float x;
    float y;
public:
    Vector(float a=0, float b=0){
        x = a;
        y = b;
    }

    float getX(){
        return x;
    }

    
    friend std::ostream& operator<<(std::ostream& COUT, Vector& v){
    COUT<< v.x <<" "<<v.y;
    return COUT;
    }

    friend std::istream& operator>>(std::istream& is, Vector& v){
        std::cout<<"x= ";
        is >> v.x;
        std::cout<<"y= ";
        is >> v.y;
    }

    Vector operator+(Vector& v)const{
        return Vector(x + v.x, y + v.y);
    }

}; 


int main(){
    Vector v1 = Vector();
    std::cin>>v1;
    Vector v2 = Vector(3, 1);
    Vector v3 = v1 + v2;
    std::cout<<v3;
    return 0;
}