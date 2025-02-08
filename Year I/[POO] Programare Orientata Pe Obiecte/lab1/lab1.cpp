#include <iostream>
using namespace std;

class Nod{
private:
    int val;
    Nod* prev = nullptr;
    Nod* next = nullptr;
public:
    Nod(int val): val{val}{}
    Nod* getNext(){
        return next;
    }
    int getVal(){
        return val;
    }
    ~Nod(){
        delete prev;
        delete next;
    }
};

class Lista{
private:
    Nod* head;

public:
    Lista() {head=nullptr;}

    friend ostream& operator<<(ostream& os, Lista& l){
        
        Nod* aux = l.head;
        while(aux != nullptr){
            os<<aux->getVal()<<std::endl;
            aux = aux->getNext();
        }
        return os;
    }

    void adaugareNod(int val){
        Nod nod = Nod(val);
        if(head == nullptr)
            head = &nod;
        else
        {
            Nod* aux = head;
            while(aux->getNext() != nullptr){
                aux = aux->getNext();
            } 
            aux->getNext() = nod;
        }
    }

    ~Lista(){
        Nod* aux = head;
        while(aux != nullptr){
            Nod* aux2 = aux->getNext();
            delete aux;
            aux = aux2;
        }
    }
};

int main(){
    
    return 0;
}