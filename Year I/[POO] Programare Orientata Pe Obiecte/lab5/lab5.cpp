#include <iostream>

class A{
    private:
    int a;
    int b;
    public:

    void afisare(){
        std::cout<<"Afisat";
    }

};

class B : protected A{

};

int main(){
    
    A clasa1;
    B clasa2;
    
    
    return 0;
}