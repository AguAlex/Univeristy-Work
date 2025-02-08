#include <iostream>
#include <vector>

using namespace std;

class Drum{
protected:
    string denumire;
    double lungime;
    int nr_tronsoane;

public:
    Drum(){
        denumire = "";
        lungime = -1;
        nr_tronsoane = -1;
    }

    Drum(string d, double l, int n){
        denumire = d;
        lungime = l;
        nr_tronsoane = n;
    }

    virtual double calcul_cost() = 0;
};

class National : public Drum{
protected:
    int nr_judete;

public:
    National(string d, double l, int n, int jud): Drum(d, l, n){
        nr_judete = jud;
    }
    friend ostream& operator<<(ostream& os, National& d){

        os<<d.denumire<<" "<<d.lungime<<endl;
        return os;
    }

    double calcul_cost(){
        return 3000;
    }
};

class European : public Drum{
private:
    int nr_tari;

public:
    European(string d, double l, int n, int tari): Drum(d, l, n){
        nr_tari = tari;
    }

    double calcul_cost(){
        return 5000;
    }
};

class Autostrada : public Drum{
private:
    int nr_benzi;
};

class AutostradaEU : public Autostrada, public European{

};

class Contract{
private:
    int id;
    static int cnt;
    string cif, nume;
    double cost;
    Drum *drum;

public:
    
    Contract();
    Contract(string n, string c, Drum* d){
        nume = n;
        cif = c;
        drum = d;
        id = ++cnt;
        cost = calcul_cost(d);
    }

    double calcul_cost(Drum *d){
        return d->calcul_cost();
    }

    friend istream& operator>>(istream& is, Contract& contract);
    friend ostream& operator<<(ostream& os, Contract& contract);
};

int Contract::cnt = 0;

Contract::Contract(){
    cif = "";
    nume = "";
    id = ++cnt;
}

istream& operator>>(istream& is, Contract& contract){
    cout<<"Nume: ";
    is >> contract.nume;
    cout<<endl<<"Cif: ";
    is >> contract.cif;
    
    return is;
}
ostream& operator<<(ostream& os, Contract& c){
    os << "Nume: " << c.nume << endl << "Cif: " << c.cif <<endl
    << "Id: " <<c.id<<endl<<"Cost: " <<c.cost<<endl;
    return os;
}

class Menu{
private:
    vector<Contract*> contracte;

public:
    Menu() = default;
    void adaugare_contract(Contract* c){
        contracte.push_back(c);
    }

    void afisare_contracte(){
        for(auto c : contracte)
            cout<<*c;
    }

    void adaugare_contracte(){
        cout<<endl<<"----------------------------------";
        cout<<"Numar de contracte de adaugat: ";
        int nr_contr;
        cin >> nr_contr;

        cout<<endl<<"Citire contracte:"<<endl;
        for (int i = 1; i <= nr_contr; i++){
            Contract* c_aux = new Contract();

            cout<<"Selectati tipul de drum:"
        }
    }

    void start(){
        while(true){
            cout<<"1. Afisare contracte" << endl << "2.Adaugare contracte" << endl << "0.Exit" <<endl << "Selectati o optiune: ";

            int optiune;
            cin >> optiune;

            if(optiune == 1){
                afisare_contracte();
            }
                
            if(optiune == 2){
                adaugare_contracte();
            }
        }
    }
};


int main(){
    National* drum = new National("A1", 12.4, 2, 4);
    Contract* c = new Contract("Contract 1", "cif1", drum);

    European* drum2 = new European("E1", 14, 5, 2);
    Contract* c2 = new Contract("Contract 2", "cif2", drum2);

    Menu menu;
    menu.adaugare_contract(c);
    menu.adaugare_contract(c2);
    //menu.afisare_contracte();

    menu.start();

    delete c;
    delete drum;
    delete drum2;
    delete c2;
    return 0;
}