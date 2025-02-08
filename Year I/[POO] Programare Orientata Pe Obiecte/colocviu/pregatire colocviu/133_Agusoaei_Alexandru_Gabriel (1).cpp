//Agusoaei Alexandru Gabriel - 133
//VS Code
//Stefan Daniel Wagner

#include <iostream>
#include <vector>

using namespace std;
//Clasa pentru fiecare element din inventar
class Element{
protected:
    static int cnt;
    int id;
    int cost_upgrade; //Are nevoie de o functie virtuala pentru a putea fi implementat sa se calculeze costul pentru fiecare tip de element. (am ramas fara timp)

public:
    Element(){
        id = ++cnt;
    };
    ~Element() = default;

    friend istream& operator>>(istream& is, Element* ob){
        ob->read(is);
        return is;
    }

    friend ostream& operator<<(ostream& os, Element* ob){
        ob->write(os);
        return os;
    }


    virtual void read(istream& is) = 0;
    virtual void write(ostream& os) = 0;

};

int Element::cnt = 0;

class Zid : public Element{
private:
    int inaltime, lungime, grosime;

public:
    Zid() = default;

    Zid(int i, int l, int g);

    void read(istream& is){
        cout<<"\n------Citire zid------";
        cout << "\nInaltime: ";
        is >> inaltime;
        cout<< "\nLungime: ";
        is >> lungime;
        cout<< "\nGrosime: ";
        is >> grosime;
        cout<<endl;
    }

    void write(ostream& os){
        cout<<"\n------Afisare zid------";
        cout<<"\nId: " << id;
        cout << "\nInaltime: " << inaltime;
        cout<< "\nLungime: " << lungime;
        cout<< "\nGrosime: " << grosime;
        cout<<endl;
    }

};

Zid::Zid(int i, int l, int g){
    inaltime = i;
    lungime = l;
    grosime = g;
}

class Turn : public Element{
private:
    int putere_laser;

public:

    Turn() = default;

    void read(istream& is){
            cout<<"\n------Citire turn------";
            cout << "\nPutere laser: ";
            is >> putere_laser;
            
            cout<<endl;
        }

        void write(ostream& os){
            os<<"\n------Afisare turn------";
            os<<"\nId: " << id;
            os << "\nPutere laser: " << putere_laser;
            
            os<<endl;
        }
};

class Robot : virtual public Element{
protected:
    int damage, nivel, viata;

public:

    Robot() = default;

    Robot(int d, int n, int v);

    void read(istream& is);

    void write(ostream& os);
};

Robot::Robot(int d, int n, int v){
    damage = d;
    nivel = n;
    viata = v;
}

void Robot::read(istream& is){
    
        
        cout<<endl;
    
}

void Robot::write(ostream& os){
        
    }

class RobotAerian : virtual public Robot{
protected:
    int autonomie_zbor;

public:
    RobotAerian() = default;

    void read(istream& is);

    void write(ostream& os);

};

void RobotAerian::read(istream& is){
    cout<<"\n------Citire robot aerian------";
    cout << "\nDamage: ";
    is >> damage;
    cout<< "\nNivel: ";
    is >> nivel;
    cout<< "\nViata: ";
    is >> viata;
    cout<<"\nAutonomie zbor: ";
    cin >> autonomie_zbor;
    cout<<endl;
}

void RobotAerian::write(ostream& os){
    cout<<"\n------Afisare robot aerian------";
    cout<<"\nId: " << id;
    cout << "\nDamage: " << damage;
    cout<< "\nNivel: " << nivel;
    cout<< "\nViata: " << viata;
    cout<<endl;
    cout << "\nAutonomie zbor: " << autonomie_zbor <<endl;
}

class RobotTerestru : virtual public Robot{
private:
    int nr_gloante;
    bool scut;

public:
    RobotTerestru() = default;

    void read(istream& is);

    void write(ostream& os);

};

void RobotTerestru::read(istream& is){
    cout<<"\nNr. gloante: ";
    cin >> nr_gloante;
    cout<<"\nScut(0-false sau 1-true): ";
    cin>>scut;
    cout<<endl;
}

void RobotTerestru::write(ostream& os){
    cout << "\nNr. gloante: " << nr_gloante << "\nScut: " << scut << endl;
}

class Inventar{
private:
    vector<Zid*> ziduri;
    vector<Turn*> turnuri;
    vector<Robot*> roboti;

public:
    Inventar() = default;

    Inventar(const Inventar& ob);

    vector<Zid*> getZiduri();

    vector<Turn*> getTurnuri();

    vector<Robot*> getRoboti();

    ~Inventar();

    void afiseaza_ziduri(){
        for(auto& z : ziduri)
            z->write(cout);
    }

    void afiseaza_turnuri(){
        for(auto& z : turnuri)
            z->write(cout);
    }

    void afiseaza_roboti(){
        for(auto& z : roboti)
            z->write(cout);
    }

    void adauga_zid(Zid* z){
        ziduri.push_back(z);
    }

    void adauga_turn(Turn* t){
        turnuri.push_back(t);
    }

    void adauga_robot(Robot* r){
        roboti.push_back(r);
    }
        

};

Inventar::~Inventar(){
    for(auto& i : ziduri)
        delete i;
    for(auto& i : turnuri)
        delete i;
    for(auto& i : roboti)
        delete i;
}

Inventar::Inventar(const Inventar& ob){
    this->ziduri = ziduri;
    this->turnuri = turnuri;
    this->roboti = roboti;

}

vector<Zid*> Inventar::getZiduri(){
    return ziduri;
}

vector<Turn*> Inventar::getTurnuri(){
    return turnuri;
}

vector<Robot*> Inventar::getRoboti(){
    return roboti;
}

class Jucator{
private:
    int puncte;
    Inventar* inventar;

public:
    Jucator(){
        this->puncte = 50000;
        inventar = new Inventar();
    }

    ~Jucator();

    void afisare_optiuni();

    void start();

    void adauga_element();

    void vinde();

    void afisare_roboti();

    void afisare_inventar();
};

Jucator::~Jucator(){
    delete inventar;
}

void Jucator::afisare_optiuni(){
    cout << "\n------Optiuni------" << "\n1. Adauga element." << "\n2. Upgrade element." << "\n3. Afisare roboti."<<"\n4. Afisare elemente." << "\n0. Paraseste meniu"
    <<"\nIntroduceti o optiune: ";
}

void Jucator::start(){

    while(true){
        afisare_optiuni();

        int optiune;
        cin >> optiune;

        if(optiune == 0){
            cout<<"Meniu inchis.";
            break;
        }
        else
            if(optiune == 1){
                adauga_element();
            }
        else
            if(optiune == 2){
                vinde();
            }
        else
            if(optiune == 3){
                afisare_roboti();
            }
        else
            if(optiune == 4){
                afisare_inventar();
            }
        else
            cout << "\nOptiune incorecta! Selecteaza alta optiune: ";
    }
}

void Jucator::adauga_element(){
    cout << "\nIntroduce un tip de element(0-zid, 1-turn, 2-robot): ";

    int optiune_element;

    cin >> optiune_element;

    if(optiune_element == 0){
        cout<<"\nAti ales un zid. Citire zid: ";

        Zid* el = new Zid();

        el->read(cin);

        inventar->adauga_zid(el);
    }
    else
        if(optiune_element == 1){
            cout<<"\nAti ales un turn. Citire turn: ";

            Turn* el = new Turn();

            el->read(cin);

            inventar->adauga_turn(el);
        }
    else
        if(optiune_element == 2){
            cout<<"\nAti ales un robot. Intorduceti tipul de robot(0-aerian, 1-terestru): ";

            int opt_robot;
            cin>>opt_robot;

            if(opt_robot == 0){
                RobotAerian* el = new RobotAerian();

                el->read(cin);

                inventar->adauga_robot(el);
            }
            else
                if(opt_robot == 1){
                    RobotTerestru* el = new RobotTerestru();

                    el->read(cin);

                    inventar->adauga_robot(el);
                }
            else
                cout<<"\nOptiune incorecta! Incercati din nou: ";
        

        }

}

void Jucator::afisare_inventar(){
    cout << "\n-------------Inventar----------------";
    cout<<"\nZiduri: ";
    
    inventar->afiseaza_ziduri();

    cout<<"\nTurnuri: ";

    inventar->afiseaza_turnuri();
    
    cout<<"\nRoboti: ";

     inventar->afiseaza_roboti();
    
}

void Jucator::vinde(){

}

void Jucator::afisare_roboti(){
    for(auto& r : inventar->getRoboti()){
        r->write(cout);
    }
}

int main(){
    //Se pot adauga si afisa elemente dupa cum doreste utilizatorul meniului.

    Jucator j;

    j.start();
    

    return 0;
}