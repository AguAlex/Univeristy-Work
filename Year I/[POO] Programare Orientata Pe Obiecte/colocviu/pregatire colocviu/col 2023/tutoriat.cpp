#include <iostream>
#include <vector>
#include<exception>
using namespace std;

class MyException: public exception{
public:
    virtual const char* what() const throw(){
        return "valoare invalida \n";
    }
}ex1;

class Drum{
protected:
    string nume;
    float lungime;
    int tronsoane;

public:
    Drum();
    Drum(string nume, float lungime, int tronsoane);
    Drum(const Drum &drum);
    ~Drum()=default;


};

Drum::Drum(){
    this->nume = "predefinit";
    this-> lungime = 0;
    this-> tronsoane = 0;
}

Drum::Drum(string nume, float lungime, int tronsoane){
    this->nume = nume;
    this-> lungime = lungime;
    this-> tronsoane = tronsoane;
}

Drum::Drum(const Drum &drum){
    this->nume = drum.nume;
    this-> lungime = drum.lungime;
    this-> tronsoane = drum.tronsoane;
}

class DrumNational : public Drum{
private:
    int nrJudete;

public:
    DrumNational(string nume, float lungime, int tronsoane, int nrJudete );


};

DrumNational::DrumNational(string nume, float lungime, int tronsoane, int nrJudete )
            :Drum(nume, lungime, tronsoane){
                this->nrJudete = nrJudete;
            }

            
class DrumEuropean : virtual public Drum{
private:
    int nrTari;

public:
    DrumEuropean(string nume, float lungime, int tronsoane, int nrTari );


};

DrumEuropean::DrumEuropean(string nume, float lungime, int tronsoane, int nrTari )
            :Drum(nume, lungime, tronsoane){
                this->nrTari = nrTari;
            }


class Autostrada : virtual public Drum{
private:
    int nrBenzi;

public:
    Autostrada(string nume, float lungime, int tronsoane, int nrBenzi );


};

Autostrada::Autostrada(string nume, float lungime, int tronsoane, int nrBenzi )
            :Drum(nume, lungime, tronsoane){
                this->nrBenzi = nrBenzi;
            }


class AutostradaEU : public DrumEuropean, public Autostrada{

public:
    AutostradaEU(string nume, float lungime, int tronsoane, int nrTari, int nrBenzi );


};

AutostradaEU::AutostradaEU(string nume, float lungime, int tronsoane, int nrTari, int nrBenzi )
            :DrumEuropean(nume, lungime, tronsoane, nrTari),
            Autostrada(nume, lungime, tronsoane, nrBenzi){}


class Contract{
private:
    const int id;
    static int idCnt;
    string nume;
    string cif;
    float cost;
    Drum *drum;
public:
    Contract(string nume, string cif, float cost, Drum *drum);
    ~Contract();
    


};

int Contract::idCnt = 0;
Contract::Contract(string nume, string cif, float cost, Drum *drum):id(++idCnt){
    this->nume = nume;
    this->cif = cif;
    this->cost = cost;
    this->drum = drum;
}
Contract::~Contract(){
    if(this->drum != nullptr){
        delete drum;
    }
    drum = nullptr;
}

class Meniu{
private:
    vector<Contract> contracte;
    vector<Drum*> drumuri;

public:
    Meniu() = default;
    void start();
    void afisareDrum(){}
    void lungimeTotala(){}
    void reziliere(){}
    void costTotal(){}

};

void Meniu::start(){
    int optiune;
    while(true){
        cout<<"1.Afisare Drum \n";
        cout<<"2.Lungime totala \n";
        cout<<"3.Reziliere \n";
        cout<<"4.Cost total \n";
        cout<<"0.Exit \n";

        cin>>optiune;
        try{
            switch(optiune){
                case 1:
                    afisareDrum();
                    break;
                
                case 2:
                    lungimeTotala();
                    break;
                case 3:
                    reziliere();
                    break;
                case 4:
                    costTotal();
                    break;
                case 0:
                    return;

                default:
                    throw ex1;

                

            }
        }
        catch(exception& ex){
            cout<<ex.what();
        }
    }
}

int main(){

    Meniu meniu;
    meniu.start();

    return 0;
}