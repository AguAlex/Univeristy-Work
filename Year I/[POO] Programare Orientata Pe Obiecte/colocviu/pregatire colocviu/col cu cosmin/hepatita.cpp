#include <iostream>
#include <vector>

using namespace std;


class Vaccin{
protected:
    double pret;
    int temperatura;
    vector<string> substante;
    

public:

    Vaccin() = default;
    Vaccin(double p, int t, vector<string>& s){
        pret = p;
        temperatura = t;
        substante = s;
    }

    virtual ~Vaccin() = default;

    friend istream& operator>>(istream& is, Vaccin& v){
        cout << "Pret: ";
        is >> v.pret; cout<<endl;
        cout<<"Temperatura: ";
        is >> v.temperatura; cout<<endl;
        cout<<"Nr. substante: ";
        int nr_subst; string subst;
        is>>nr_subst;
        for(int i = 1; i<= nr_subst; i++){
            is >> subst;
            v.substante.push_back(subst);
        }
            
        cout<<endl;

        return is;
    }

    friend ostream& operator<<(ostream& os, Vaccin& v){
        os << "-----Afisare vaccin-----" << endl
           << "Pret: " << v.pret << endl
           << "Temperatura: " << v.temperatura << endl
           << "Substante: ";
        for(auto s : v.substante){
            os << s <<" ";
        }
        os<<endl;
        
        return os;
    }

    virtual void schema_vaccinare() = 0;
};

class Antigripal : virtual public Vaccin{
protected:
    string tulpina;
    bool recomandari;

public:
    Antigripal() = default;
    Antigripal(double p, int t, vector<string>& s, string tulp, bool r)
    : Vaccin(p, t, s), tulpina{tulp}, recomandari{r}{}

    void schema_vaccinare(){
        cout<<"Schema pentru Antigripal"<<endl;
    }

    friend istream& operator>>(istream& is, Antigripal& v){
        cout << "Pret: ";
        is >> v.pret; cout<<endl;
        cout<<"Temperatura: ";
        is >> v.temperatura; cout<<endl;
        cout<<"Nr. substante: ";
        int nr_subst; string subst;
        is>>nr_subst;
        for(int i = 1; i<= nr_subst; i++){
            is >> subst;
            v.substante.push_back(subst);
        }
        cout<<"Tulpina: ";
        is >> v.tulpina; cout<<endl;
        cout<<"Recomandari: ";
        is >> v.recomandari; cout<<endl;

        return is;
    }

    friend ostream& operator<<(ostream& os, Antigripal& v){
        
        os << "-----Afisare vaccin-----" << endl
           << "Pret: " << v.pret << endl
           << "Temperatura: " << v.temperatura << endl
           << "Substante: ";
        for(auto s : v.substante){
            os << s <<" ";
        }
        
        os << "Tulpina: " << v.tulpina << endl <<"Recomandari: " << v.recomandari << endl;
        
        return os;
    }

    
};

class Antihepatita : virtual public Vaccin{
protected:
    string tip, mod_vaccinare;
public:

    Antihepatita() = default;

    friend istream& operator>>(istream& is, Antihepatita& v){
        cout << "Pret: ";
        is >> v.pret; cout<<endl;
        cout<<"Temperatura: ";
        is >> v.temperatura; cout<<endl;
        cout<<"Nr. substante: ";
        int nr_subst; string subst;
        is>>nr_subst;
        for(int i = 1; i<= nr_subst; i++){
            is >> subst;
            v.substante.push_back(subst);
        }
        cout<<"Tipul: ";
        is >> v.tip; cout<<endl;
        cout<<"Mod vaccinare: ";
        is >> v.mod_vaccinare; cout<<endl;

        return is;
    }

    friend ostream& operator<<(ostream& os, Antihepatita& v){
        
        os << "-----Afisare vaccin-----" << endl
           << "Pret: " << v.pret << endl
           << "Temperatura: " << v.temperatura << endl
           << "Substante: ";
        for(auto s : v.substante){
            os << s <<" ";
        }
        
        os << "Tip: " << v.tip << endl <<"Mod vaccinare: " << v.mod_vaccinare << endl <<endl;
        
        return os;
    }

    void schema_vaccinare(){
        cout<<"Schema pentru Antihepatita"<<endl;
    }

};

class Sarscov : public Vaccin{
protected:
    vector<string> reactii_adverse;
    double rata_eficienta;
    vector<string> medicamente;
public:

    Sarscov() = default;

    friend istream& operator>>(istream& is, Sarscov& v){
        cout << "Pret: ";
        is >> v.pret; cout<<endl;
        cout<<"Temperatura: ";
        is >> v.temperatura; cout<<endl;
        cout<<"Nr. substante: ";
        int nr_subst; string subst;
        is>>nr_subst;
        for(int i = 1; i<= nr_subst; i++){
            is >> subst;
            v.substante.push_back(subst);
        }
        cout<<"Nr. reactii adverse: ";
        int nr_rc; is>>nr_rc;
        string aux;
        cout<<endl<<"Reactii: ";
        for(int i = 1; i<=nr_rc; i++){
            is >> aux;
            v.reactii_adverse.push_back(aux);
        }
        cout<<endl;
        cout<<"Rata eficienta: ";
        is >> v.rata_eficienta; cout<<endl;

        cout<<"Nr. medicamente: ";

        is>>nr_rc;
        cout<<endl<<"Medicamente: ";
        for(int i = 1; i<=nr_rc; i++){
            is >> aux;
            v.medicamente.push_back(aux);
        }

        cout<<endl;

        return is;
    }

    friend ostream& operator<<(ostream& os, Sarscov& v){
        
        os << "-----Afisare vaccin-----" << endl
           << "Pret: " << v.pret << endl
           << "Temperatura: " << v.temperatura << endl
           << "Substante: ";
        for(auto s : v.substante){
            os << s <<" ";
        }
        
        os << "Reactii adverse: ";
        for(auto a : v.reactii_adverse)
            cout<<a<<" ";

        os << endl;
        os << "Rata eficienta: " << v.rata_eficienta;

        os << "Medicamente: ";
        for(auto a : v.medicamente)
            cout<<a<<" ";

        os << endl <<endl;
        
        return os;
    }

    void schema_vaccinare(){
        cout<<"Schema pentru Sarscov"<<endl;
    }

};

class Comanda{
private:
    static int cnt;
    int id, zi, luna, an;
    string nume_client;
    vector<pair<string, int>> vaccinuri;

public:
    Comanda() = default;
    Comanda(int z, int l, int a, string nc, string v, int cant){
        id = ++cnt;
        zi = z;
        luna = l;
        an = a;
        nume_client = nc;
        vaccinuri.push_back(pair<string, int> {v, cant});
    }

};

int Comanda::cnt = 0;

class Meniu{
private:
    vector<Comanda*> comenzi;

public:
    Meniu() = default;

    ~Meniu(){
        for(auto aux : comenzi)
            delete aux;
    }

    void start(){

        while(true){
            afisare_optiuni();
        }
    }

    void afisare_optiuni(){
        cout<<"----OPTIUNI----"<<endl << "1.Adaugare vaccin." <<
        endl << "2.Afisare comenzi." <<endl;
    }

};

int main(){

    Antigripal a;
    Antihepatita b;
    Sarscov c;
    cin >> a;
    cout << a;

    Vaccin* list[3];
    list[0]=new Antigripal();
    list[1]=new Antihepatita();
    list[2]=new Sarscov();

    for(int i=0; i<3; i++)
    list[i]-> schema_vaccinare();
    Comanda com1(20, 12, 2020, "SpitalX", "AntiSarsCov2", 20);
    Comenzi lista;
    lista=lista+com1;
    cout<<lista[0];

    delete list;

    return 0;
}