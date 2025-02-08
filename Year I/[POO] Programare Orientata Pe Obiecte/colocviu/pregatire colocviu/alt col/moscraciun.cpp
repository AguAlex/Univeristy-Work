#include <iostream>
#include <vector>

using namespace std;


class Jucarie{
protected:
    string denumire;
    int dimensiune;
    string tip;

public:
    Jucarie() = default;

    Jucarie(string d, int di, string t):denumire{d}, dimensiune{di},
    tip{t}{}

    friend istream& operator>>(istream& is, Jucarie& j){
        cout<<"\nDenumire: ";
        is >> j.denumire;
        cout<<"\nDimensiune: ";
        is >> j.dimensiune;
        cout<<"Tip: ";
        is >> j.tip;
        cout<<endl;
        return is;
    }

    friend ostream& operator<<(ostream& os, Jucarie& j){
        cout<<"\nDenumire: " << j.denumire <<"\nDimensiune: " <<
        j.dimensiune <<"\nTip: " << j.tip << endl;
        return os;
    }


};

class JucarieClasica : virtual public Jucarie{
private:
    string material, culoare;

public:

};

class JucarieEducativa : virtual public Jucarie{
protected:
    string abilitate;

public:

};

class JucarieElectronica : virtual public Jucarie{
protected:
    int nr_baterii;
public:

};

class JucarieModerna : virtual public JucarieEducativa, virtual public JucarieElectronica{
private:
    string brand, model;

public:
    JucarieModerna(){
        nr_baterii = 1;
        abilitate = "generala";
    }

    JucarieModerna(string d, int di, string t, string b, string m){
        Jucarie(d, di, t);
        brand = b;
        model = m;
    }
};

class Copil{
protected:
    static int cnt;
    int id;
    string nume, prenume, tip;
    int varsta, fapte_bune;
    vector<Jucarie*> jucarii;

public:
    Copil(){
        id = ++cnt;
    }
    ~Copil(){
        for(auto j : jucarii)
            delete j;
    }

    Copil(string n, string p, int v, int f){
        id = ++cnt;
        nume = n;
        prenume = p;
        varsta = v;
        fapte_bune = f;
    }

    string getTip(){
        return this->tip;
    }

    string getNume(){
        return this->nume;
    }

    int getId(){
        return this->id;
    }
        
    friend std::istream &operator>>(std::istream&in,Copil* ob){
        ob->read(in);
        return in;
    }
    friend std::ostream &operator<<(std::ostream&out,Copil* ob){
        ob->write(out);
        return out;
    }

    virtual void read(std::istream &in)=0;
    virtual void write(std::ostream &out)=0;
};

int Copil::cnt = 0;

class CopilCuminte : virtual public Copil{
private:
    int nr_dulciuri;

public:
    CopilCuminte(){
        tip = "cuminte";
    }

    

    void read(std::istream& is){
        cout<<"\nCiteste copil cuminte: ";
        cout << "\nNume: ";
        cin >> nume;
        cout << "\nPrenume: ";
        cin >> prenume;
        cout << "\nVarsta: ";
        cin >> varsta;
        cout << "\nFapte bune: ";
        cin >> fapte_bune;
        cout << "\nNr. dulciuri: ";
        cin >> nr_dulciuri;

       
    }

    void write(ostream& os){
        os << "\nId: " << id;
        os << "\nNume: " << nume;
        os << "\nPrenume: " << prenume;
        os << "\nVarsta: " << varsta;
        os << "\nFapte bune: " << fapte_bune;
        os << "\nNr. dulciuri: " << nr_dulciuri;

        
    }
};

class CopilNeastamparat : virtual public Copil{
private:
    int nr_carbuni;

public:
    CopilNeastamparat(){
        tip = "neastamparat";
    }

    void read(istream& is){
        cout<<"\nCiteste copil neastamparat: ";
        cout << "\nNume: ";
        is >> nume;
        cout << "\nPrenume: ";
        is >> prenume;
        cout << "\nVarsta: ";
        is >> varsta;
        cout << "\nFapte bune: ";
        is >> fapte_bune;
        cout << "\nNr. carbuni: ";
        is >> nr_carbuni;
    }

    void write(ostream& os){
        os << "\nId: " << id;
        os << "\nNume: " << nume;
        os << "\nPrenume: " << prenume;
        os << "\nVarsta: " << varsta;
        os << "\nFapte bune: " << fapte_bune;
        os << "\nNr. carbuni: " << nr_carbuni;
    }
};

class Meniu{
private:
    vector<Copil*> copii;

public:
    Meniu() = default;

    ~Meniu(){
        for(auto c : copii){
            delete c;
        }

    
    }

    void afisare_optiuni(){
        cout<<"\n1. Citire copii." << "\n2. Citire jucarii." <<
        "\n3. Cauta nume." << "\n4. Afisare copii." "\n0. Exit meniu";

    }

    void afisare_copii(){
        // cout << "\n-------------Copii cuminti-------------- ";
        // for(auto c : copii){
        //     cout << *c;
        // }

        cout << "\n\n----------Copii neastamparati---------------- ";
        for(auto c : copii){
            // if(dynamic_cast<CopilCuminte*>(c))
            // cout << dynamic_cast<CopilCuminte*>(c);

            // if(dynamic_cast<CopilNeastamparat*>(c))
            // cout<< dynamic_cast<CopilNeastamparat*>(c);
            c->write(cout);
        }
        cout<<endl<<endl;
    }

    void citire_copii(){
        int n;
        cout<<"\nIntroduce nr. de copii: ";
        cin >> n;
        int copil;
        for(int i=1; i<=n; i++){
            cout<<"\nIntroduce tip copil(0 - cuminte, 1 - neastamparat): ";
            cin >> copil;
            
            if(copil == 0){
                CopilCuminte* c = new CopilCuminte();
                c->read(cin);
                copii.push_back(c);
            }
            else{
                CopilNeastamparat* c = new CopilNeastamparat();
                c->read(cin);
                copii.push_back(c); 
            }
            
            

        }
    }

    void citire_jucarii(){

    }

    void cauta_nume(string nume){
        for(auto c : copii){
            if(c->getNume() == nume)
                cout<<"\nCopilul cu id: " << c->getId() <<" si numele: " << c->getNume();

        }

        // for(auto c : copii_neastamparati){
        //     if(c->getNume() == nume)
        //         cout<<"\nCopilul cu id: " << c->getId() <<" si numele: " << c->getNume();
                
        // }
    }

    void start(){
        while(true){
            afisare_optiuni();
            int optiune;

            cout<<"\nAlege o optiune: ";
            cin >> optiune;

            if(optiune == 1)
                citire_copii();
            else
                if(optiune == 2)
                    citire_jucarii();
            else
                if(optiune == 3){
                    string aux;
                    cout<<"\nIntroduceti un nume: ";
                    cin >> aux;
                    cout<<endl;
                    cauta_nume(aux);
                }
                    
            else
                if(optiune == 0){
                    cout<<"Meniu inchis";
                    break;
                }
            else
                if(optiune == 4)
                    afisare_copii();  
            else{
                cout<<"Optiune incorecta!";
            }
        }
    }
};

int main(){
    Meniu m;
    m.start();


    return 0;
}