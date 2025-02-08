#include <iostream>
#include <vector>
using namespace std;

class Drum{
protected:
    string denumire;
    double lungime;
    int nr_tronsoane;
public:
    Drum() = default;
    Drum(string d, double l, int n);

    friend istream& operator>>(istream& is, Drum* d){
        d->read(is);
        return is;
    }

    friend ostream& operator<<(ostream& os, Drum* d){
        d->write(os);
        return os;
    }

    virtual void read(istream& is) = 0;
    virtual void write(ostream& os) = 0;
};

Drum::Drum(string d, double l, int n):
    denumire{d}, lungime{l}, nr_tronsoane{n}{}

class DrumNational : virtual public Drum{
private:
    int nr_judete;

public:
    DrumNational() = default;

    DrumNational(string d, double l, int n, int j):
    Drum(d, l, n), nr_judete{j}{}

    void read(istream& is){
        cout<<"------Citire drum national-------" << endl;
        cout<<"\nDenumire: ";
        is >> denumire;
        cout<<"\nLungime: ";
        is >> lungime;
        cout<<"Nr. tronsoane: ";
        is >> nr_tronsoane;
        cout<<"Nr. judete: ";
        is >> nr_judete;
        cout<<endl;
    }

    void write(ostream& os){
        os<<"\n-------Afisare Drum National-------";
        os<<"\nDenumire: " << denumire <<"\nLungime: " << lungime << "\nNr. tronsoane: " << nr_tronsoane << "\nNr. judete: " <<
        nr_judete<<endl;
        
    }

};

class DrumEuropean : virtual public Drum{
protected:
    int nr_tari;

public:
    DrumEuropean() = default;

    DrumEuropean(string d, double l, int n, int t):
    Drum(d, l, n), nr_tari{t}{}

    void read(istream& is){
        cout<<"\nDenumire: ";
        is >> denumire;
        cout<<"\nLungime: ";
        is >> lungime;
        cout<<"\nNr. tronsoane: ";
        is >> nr_tronsoane;
        cout<<"\nNr. tari: ";
        is>>nr_tari;
        cout<<endl;
    }

};

class Autostrada : virtual public Drum{
protected:
    int nr_benzi;
public:
    Autostrada() = default;

    Autostrada(string d, double l, int n, int b):
    Drum(d, l, n), nr_benzi{b}{}
};

class AutostraziEu : virtual public Autostrada, virtual public DrumEuropean{
private:

public:
    AutostraziEu() = default;
    AutostraziEu(string d, double l, int n, int b, int t):
    Drum(d, l, n){
       nr_benzi = b;
       nr_tari = t;
    }
};

class Contract{
private:
    static int cnt;
    int id;
    string nume, cif;
    Drum* drum;
    int nr_tronson;
    double cost;

public:
    Contract(){
        id = ++cnt;
        drum = nullptr;
        cost = calcul_cost();
    };

    ~Contract(){
        delete drum;
    }
    

    Contract(string n, string c, Drum* d, int nt){
        nume = n;
        cif = c;
        drum = d;
        nr_tronson = nt;
    }

    void setDrum(Drum* d){
        this->drum = d;
    }

    double calcul_cost();

    friend istream& operator>>(istream &is, Contract& c){
        cout<<"------Citire contract-------";
        cout<<"\nNume: ";
        is >> c.nume;
        cout<<"\nCif: ";
        is >> c.cif;
        cout<<"\nNr. tronson: ";
        is >> c.nr_tronson;



        return is;
    }

    friend ostream& operator<<(ostream& os, Contract& c){
        cout<<"\n-------------Afisare Contract-----------";
        cout<<"\nDrumul contractului: ";
        c.drum->write(cout);

        cout<<"\nId: " <<c.id;
        cout<<"\nNume: " << c.nume;
        cout<<"\nCif: " << c.cif;
        cout<<"\nNr. tronson: " <<c.nr_tronson;
        return os;
    }

};

int Contract::cnt = 0;

double Contract::calcul_cost(){
    return 0;
}

class Meniu{
private:
    vector<Contract*> contracte;

public:
    Meniu() = default;

    ~Meniu(){
        for(auto& c : contracte){
            delete c;
        }
    }

    void afisare_optiuni();

    void start();

    void adauga_contract(){
        
    Contract* c = new Contract();
        int tip_drum;

        cout<<"Introduce tip drum pentru contract(0-national, 1-european, 2-autostrada, 3-autostradaeu) ";

        while(true){
            cin>>tip_drum;
            if(tip_drum < 4)
                break;
            else
                cout<<"\nValoare gresita! " << endl;
        }

        if(tip_drum == 0){
            DrumNational* d = new DrumNational();
            d->read(cin);
            c->setDrum(d);
        }
            
        
        cin >> *c;

        
        contracte.push_back(c);

    }

    void afisare_contracte();

};

void Meniu::afisare_optiuni(){
    cout << "\n1. Adauga contract." << "\n2. Afisare contracte." << 
    "\n3. Lungime totala drumuri. "<< "0. Exit"<<endl;
}

void Meniu::afisare_contracte(){
    for(auto c : contracte)
        cout << *c;
}



void Meniu::start(){
    while(true){
        afisare_optiuni();

        int optiune;
        cin >> optiune;

        if(optiune == 1){
            adauga_contract();
        }
            
        else
            if(optiune == 2)
                afisare_contracte();
    }
}

int main(){

    Meniu m;
    m.start();

    return 0;
}