#include <iostream>
#include <vector>
#include <map>

class Stream{
public:
    Stream()=default;
    virtual ~Stream()=default;

    friend std::istream &operator>>(std::istream&in,Stream* ob){
        ob->read(in);
        return in;
    }
    friend std::ostream &operator<<(std::ostream&out,Stream* ob){
        ob->write(out);
        return out;
    }

    virtual void read(std::istream &in)=0;
    virtual void write(std::ostream &out) const=0;
};

class Vaccin:public Stream{
protected:
    float pret;
    float temperatura;
    std::vector<std::string> ingrediente;
    std::string numeProducator;
public:
    Vaccin()=default;

    Vaccin(std::string&,float&,float&,std::vector<std::string>&);

    void read(std::istream &in) override;
    void write(std::ostream &out)const override;

    float getPret(){return pret;}

    virtual void afisareSchemaVaccinare(){}

    std::string getNumeProducator(){return numeProducator;}
};

Vaccin::Vaccin(std::string&np,float&p,float&t,std::vector<std::string>&i):
        numeProducator(np),pret(p),temperatura(t),ingrediente(i){}

void Vaccin::read(std::istream &in) {
    std::cout<<"\nNume producator:";
    in>>numeProducator;
    std::cout<<"\nPret vaccin:";
    in>>pret;
    std::cout<<"\nTemperatura vaccin:";
    in>>temperatura;
    std::cout<<"\nNumar ingrediente vaccin:";
    int n;
    in>>n;
    std::string ingredient;
    for (int i = 0; i < n; ++i) {
        std::cout<<"\nIngredient "<<i+1;
        in>>ingredient;
        ingrediente.push_back(ingredient);
    }
}

void Vaccin::write(std::ostream &out) const {
    out<<"\nNume producator:"<<numeProducator
        <<"\nPret vaccin:"<<pret
        <<"\nTemperatura vaccin:"<<temperatura
        <<"\nLista ingrediente:";
    for(auto i:ingrediente)
        out<<i<<" ";
}

class AntiGripal:public Vaccin{
private:
    std::string tulpina, recomandari;
public:
    AntiGripal()=default;

    AntiGripal(std::string&,float&,float&,std::vector<std::string>&,std::string&,std::string&);

    void read(std::istream &in) override;
    void write(std::ostream &out)const override;

    void afisareSchemaVaccinare() override;
};

AntiGripal::AntiGripal(std::string&np,float&p,float&t,std::vector<std::string>&i,std::string&tu,std::string&r):
        Vaccin(np,p,t,i),tulpina(tu),recomandari(r){}

void AntiGripal::read(std::istream &in) {
    Vaccin::read(in);
    std::cout<<"\nTulpina virus:";
    in>>tulpina;
    std::cout<<"\nRespecta recomandarile OMS? ";
    in>>recomandari;
}

void AntiGripal::write(std::ostream &out) const {
    Vaccin::write(out);
    out<<"\nTulpina virus:"<<tulpina;
    if(recomandari=="da")
        out<<"\nVaccinul respecta recomandarile OMS.";
    else
        out<<"\nVaccinul nu respecta recomandarile OMS.";
}

void AntiGripal::afisareSchemaVaccinare() {
    std::cout<<"\nSe adimintreaza la adulti o doza de 0.5ml, iar la copii si adolescenti"
               "o doza de 0.3ml,repetandu-se din 2 in 2 ani.";
}

class AntiCovid:public Vaccin{
private:
    std::vector<std::string> reactiiAdverse;
    float eficienta;
    std::vector<std::string> medicamenteContraindicate;
public:
    AntiCovid()=default;

    AntiCovid(std::string&,float&,float&,std::vector<std::string>&,std::vector<std::string>&,float&,std::vector<std::string>&);

    void read(std::istream &in) override;
    void write(std::ostream &out)const override;

    void afisareSchemaVaccinare() override;
};

AntiCovid::AntiCovid(std::string&np,float&p,float&t,std::vector<std::string>&i,std::vector<std::string>&ra,float&e,std::vector<std::string>&mc):
        Vaccin(np,p,t,i),reactiiAdverse(ra),eficienta(e),medicamenteContraindicate(mc) {}

void AntiCovid::read(std::istream &in) {
    Vaccin::read(in);
    std::cout<<"\nNumar reactii adverse:";
    int n;
    in>>n;
    std::string aux;
    for (int i = 0; i < n; ++i) {
        in>>aux;
        std::cout<<" ";
        reactiiAdverse.push_back(aux);
    }
    std::cout<<"\nEficienta vaccin:";
    in>>eficienta;
    std::cout<<"\nNumar medicamente contraindicate:";
    in>>n;
    for (int i = 0; i < n; ++i) {
        in>>aux;
        std::cout<<" ";
        medicamenteContraindicate.push_back(aux);
    }
}

void AntiCovid::write(std::ostream &out) const {
    Vaccin::write(out);
    out<<std::endl;
    for(auto a:reactiiAdverse)
        out<<a<<" ";
    out<<"\nEficienta vaccin:"<<eficienta;
    out<<std::endl;
    for(auto a:medicamenteContraindicate)
        out<<a<<" ";
}

void AntiCovid::afisareSchemaVaccinare() {
    std::cout<<"\nSe administreaza persoanelor cu varsta mai mare de 16 ani, 2 doze la o perioada de 21 de zile.";
}

class AntiHeptatita:public Vaccin{
private:
    std::string tipHeptatita, modVaccinare;
public:
    AntiHeptatita()=default;

    AntiHeptatita(std::string&,float&,float&,std::vector<std::string>&,std::string&,std::string&);

    void read(std::istream &in) override;
    void write(std::ostream &out)const override;

    void afisareSchemaVaccinare() override;

};

AntiHeptatita::AntiHeptatita(std::string&np,float&p,float&t,std::vector<std::string>&i,std::string&th,std::string&mv):
        Vaccin(np,p,t,i),tipHeptatita(th),modVaccinare(mv) {}

void AntiHeptatita::read(std::istream &in) {
    Vaccin::read(in);
    std::cout<<"\nTip hepatita:";
    in>>tipHeptatita;
    std::cout<<"\nMod vaccinare:";
    in>>modVaccinare;
}

void AntiHeptatita::write(std::ostream &out) const {
    Vaccin::write(out);
    out<<"\nTip hepatita:"<<tipHeptatita
        <<"\nMod vaccinare:"<<modVaccinare;
}

void AntiHeptatita::afisareSchemaVaccinare() {
    std::string aux;
    std::cout<<"\nAlegeti tipul de hepatita (A,B,C):";
    std::cin>>aux;
    if(aux=="A"||aux=="B")
        std::cout<<"\n La copii cu vârstă mai mică de 1 an se adminstrează 2 \n"
                   "injectări la un interval de o lună, a treia injectare după 6 luni de la prima administrare, la adulți \n"
                   "conform schemei de imunizare recomandată de medic.";
    else
        std::cout<<"\nDoar la recomandarea medicului.";
}

class VaccinFactory{
    VaccinFactory()=default;
public:
    static std::string getTip(std::istream &in){
        std::cout<<"\nAlege tipul de vaccin (1.antigripal,2.anti hepatita,3.anti sars-cov2)";
        std::string tip;
        in>>tip;
        return tip;
    }
    static Vaccin* newInstance(std::basic_string<char> tip){
        if(tip=="1")
            return new AntiGripal();
        else if(tip=="2")
            return new AntiHeptatita();
        else if(tip=="3")
            return new AntiCovid();
        throw std::runtime_error("Tip invalid");
    }
};

class Comanda:public Stream{
    static int cnt;
    int id;
    std::string data;
    std::string numeClient;
    std::map<Vaccin*,int> vaccinuri;
public:
    Comanda()=default;
    Comanda(std::string&,std::string&,std::map<Vaccin*,int>&);

    void read(std::istream &in) override;
    void write(std::ostream &out) const override;

    std::map<Vaccin*,int> getVaccinuri() const {return vaccinuri;}
    std::string getData() const {return data;}

    ~Comanda(){
        for(auto p:vaccinuri)
            delete p.first;
    }
};

int Comanda::cnt=1;

Comanda::Comanda(std::string&d,std::string&n,std::map<Vaccin*,int>&v):
        id(Comanda::cnt++),data(d),numeClient(n),vaccinuri(v) {}

void Comanda::read(std::istream &in) {
    std::cout<<"\nData plasare comanda:";
    in>>data;
    std::cout<<"\nNume client:";
    in>>numeClient;
    std::cout<<"\nCate tipuri de vaccinuri doriti(1-3):";
    int n;
    in>>n;
    int aux;
    for (int i = 0; i < n; ++i) {
        Vaccin *v=VaccinFactory::newInstance(VaccinFactory::getTip(std::cin));
        in>>v;
        std::cout<<"\nCata cantitate doriti:";
        in>>aux;
        vaccinuri.insert({v,aux});
    }
}

void Comanda::write(std::ostream &out) const {
    out<<"\nId comanda:"<<id
        <<"\nData plasare comanda:"<<data
        <<"\nNume client:"<<numeClient;
    for(auto pair:vaccinuri)
        out<<"\nCantitate vaccin:"<<pair.second<<" doze\n"<<pair.first;
}

class Menu{
    Menu()=default;
    std::vector<Vaccin*> vaccinuri;
    std::vector<Comanda*> comenzi;
public:
    Menu &operator=(const Menu&)=delete;

    Menu(const Menu&)= delete;

    static Menu& getmenu(){
        static Menu menu;
        return menu;
    }

    ~Menu(){
        for(auto *v:vaccinuri)
            delete v;
        for(auto *c:comenzi)
            delete c;
    }

    void adaugareNVaccinuri();

    void adaugareNComenzi();

    void afisareVaccinuri();

    void afisareComenzi();

    void afisareProducatori();

    void valoareComenzi();

    void SVVaccin();

    void startMenu();

};

void Menu::adaugareNVaccinuri() {
    std::cout<<"\nAlege numarul de vaccinuri:";
    int n;
    std::cin>>n;
    for (int i = 0; i < n; ++i) {
        Vaccin *v=VaccinFactory::newInstance(VaccinFactory::getTip(std::cin));
        std::cin>>v;
        vaccinuri.push_back(v);
    }
}


void Menu::adaugareNComenzi() {
    std::cout<<"\nAlege numarul de comenzi:";
    int n;
    std::cin>>n;
    for (int i = 0; i < n; ++i) {
        auto *c=new Comanda();
        std::cin>>c;
        comenzi.push_back(c);
    }
}


void Menu::afisareComenzi() {
    for(auto *c:comenzi)
        std::cout<<c;
}

void Menu::afisareVaccinuri() {
    for(auto *c:vaccinuri)
        std::cout<<c;
}

void Menu::afisareProducatori() {
    for(auto *v:vaccinuri)
        std::cout<<v->getNumeProducator()<<" ";
}

void Menu::valoareComenzi() {
    std::cout<<"\nData de verificare a costului unei comenzi:";
    std::string d;
    std::cin>>d;
    int sumaTotala=0;
    for(auto *c:comenzi)
        if(d==c->getData())
            for(auto v:c->getVaccinuri())
                sumaTotala+=(float) v.second*v.first->getPret();
    std::cout<<"\nSuma totala castigata in ziua "<<d<<" este de "<<sumaTotala<<" lei.";
}

void Menu::SVVaccin() {
    Vaccin *v=VaccinFactory::newInstance(VaccinFactory::getTip(std::cin));
    v->afisareSchemaVaccinare();
}

void PrintMenu(){
    std::cout<<"\n1.Adaugare a n vaccinuri noi"
            <<"\n2.Adaugare a n comenzi noi"
            <<"\n3.Afisare vaccinuri"
            <<"\n4.Afisare comenzi"
            <<"\n5.Afisare numele producatorilor pentru toate vaccinurile"
            <<"\n6.Valoarea comenzilor dintr-o anumita zi"
            <<"\n7.Afisarea schemei de vaccinare pentru un anumit tip de vaccin"
            <<"\n8.Exit";
}

void Menu::startMenu() {
    bool ok=true;
    while(ok){
        int opt;
        PrintMenu();
        std::cin>>opt;
        switch(opt){
            case 1:{
                try{
                    Menu::adaugareNVaccinuri();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
              break;
            }
            case 2:{
                try{
                    Menu::adaugareNComenzi();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
                break;
            }
            case 3:{
                try{
                    Menu::afisareVaccinuri();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
                break;
            }
            case 4:{
                try{
                    Menu::afisareComenzi();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
                break;
            }
            case 5:{
                try{
                    Menu::afisareProducatori();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
                break;
            }
            case 6:{
                try{
                    Menu::valoareComenzi();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
                break;
            }
            case 7:{
                try{
                    Menu::SVVaccin();
                } catch(std::exception &e){
                    std::cout<<e.what()<<std::endl;
                }
                break;
            }
            case 8:{
                ok=false;
                break;
            }
        }
    }
}

int main(){
    Menu::getmenu().startMenu();
    return 0;
}