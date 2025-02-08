#include <iostream>
#include <ctime>
#include <vector>
#include <memory>
#include <string>
#include <algorithm>

using namespace std::string_literals;

class Malware {
    float impact;
    std::tm data;  // .tm_year, .tm_month, .tm_day
    std::string nume;
    std::string infect;
    std::vector<std::string> registri;
protected:
    virtual float rating_impl() const { return 0; }
public:
    virtual ~Malware() = default;
    Malware(float imp, std::tm dat, std::string num, std::string inf, std::vector<std::string> regs) :
        impact(imp), data(dat), nume(num), infect(inf), registri(regs) {}
    float rating() const {
        float rating_total = rating_impl();
        bool adaugat = false;
        for(const auto& reg : registri)
            if(!adaugat && (reg == "HKLM-run"s || reg == "HKCU-run"s)) {
                rating_total += 20;
                adaugat = true;
            }
        return rating_total;
    }
    friend std::ostream& operator<<(std::ostream& os, const Malware& m) {
        os << "nume: " << m.nume
           << "rating: " << m.rating();
        return os;
    }
};

class Rootkit : public virtual Malware {
    std::vector<std::string> imports;
    std::vector<std::string> ss; // significant strings
protected:
    float rating_impl() const override {
        float rating_total = 0;
        for(const auto& st : ss)
            if(st == "Sys whatever"s || st == "SSDT"s || st == "NT..."s)
                rating_total += 100;
        for(const auto& imp : imports)
            if(imp == "ntoskrnl.exe"s)
                rating_total *= 2;
        return rating_total;
    }
public:
    Rootkit(float imp,
            std::tm dat,
            std::string num,
            std::string inf,
            std::vector<std::string> regs,
            std::vector<std::string> imps,
            std::vector<std::string> sigstrs) :
        Malware(imp, dat, num, inf, regs), imports(imps), ss(sigstrs) {}

};
class Keylogger : public virtual Malware {
    std::vector<std::string> funcs;
    std::vector<std::string> keys;
protected:
    float rating_impl() const override {
        float rating_total = 0;
        for(const auto& key : keys)
            if(key == "[Up]"s || key == "[Num Lock]"s || key == "[Down]"s)
                rating_total += 10;
        for(const auto& func : funcs)
            if(func == "CreateFileW"s || func == "OpenProcess"s)
                rating_total += 30;
        return rating_total;
    }
};
class KKeylogger : public Keylogger, public Rootkit {
    bool ascundeF;
    bool ascundeR;
protected:
    float rating_impl() const override {
        float rating_total = Keylogger::rating_impl() + Rootkit::rating_impl();
        if(ascundeF)
            rating_total += 20;
        if(ascundeR)
            rating_total += 30;
        return rating_total;
    }
};
class Ransom : public Malware {
    int rating;
    float obf;
protected:
    float rating_impl() const override {
        return static_cast<float>(rating) + obf;
    }
};

class Computer {
    const int id;
    static int id_max;
    std::vector<std::shared_ptr<Malware>> virusi;
public:
    explicit Computer(const std::vector<std::shared_ptr<Malware>>& virs) : id(id_max), virusi(virs) {
        id_max++;
    }
    Computer(const Computer& other) : id(id_max), virusi(other.virusi) {
        // ar trebui cu clone
        id_max++;
    }
    Computer& operator=(const Computer& other) {
        // ar trebui cu copy&swap
        virusi = other.virusi;
        return *this;
    }
    float rating_total() const {
        float total = 0;
        for(const auto& virus : virusi)
            total += virus->rating();
        return total;
    }
    friend std::ostream& operator<<(std::ostream& os, const Computer& c) {
        for(const auto& v : c.virusi)
            os << v << "\n";
        return os;
    }
};

int Computer::id_max = 1;

class Firma {
    std::string nume;
    std::vector<Computer> comps;
public:
    explicit Firma(std::string nume_) : nume(nume_) {}
    void adauga(const Computer& comp) {
        comps.push_back(comp);
    }
    friend std::ostream& operator<<(std::ostream& os, const Firma& f) {
        os << "nume: " << f.nume << "\n";
        for(const auto& comp : f.comps)
            os << comp << "\n";
        return os;
    }
    void sort1() {
        std::sort(comps.begin(), comps.end(), [](const auto& c1, const auto& c2) {
            return c1.rating_total() < c2.rating_total();
        });
    }
};

int main() {
    int optiune;
    Firma fir{"SmallCompany"};
    Rootkit r1(1, std::tm{}, "test1"s, "ceva"s, {}, {}, {});
    Computer comp1{{std::make_shared<Rootkit>(r1)}
        //{std::make_shared<Rootkit>(1, std::tm{}, "test1"s, "ceva"s, {}, {}, {})}
    };
    fir.adauga(comp1);
    do {
        std::cin >> optiune;
        if(optiune == 1) {
            // afis info
            std::cout << fir;
        }
        else if(optiune == 2) {
            fir.sort1();
            std::cout << fir;
        }
    } while(true);
}


















