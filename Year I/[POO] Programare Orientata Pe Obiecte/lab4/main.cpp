#include <iostream>
#include <vector>
#include <list>
class Student{
private:
    int numarMatricol;
    std::string nume;
    int nota;

public:
    Student(int numarMatricol = -1, std::string nume = "", int nota = -1)
    {
        this->numarMatricol = numarMatricol;
        this->nume = nume;
        this->nota = nota;
    }

    int GetNota(void) const;
    Student(const Student& other){
        this->numarMatricol = other.numarMatricol;
        this->nume = other.nume;
        this->nota = other.nota;
    }

    Student& operator=(const Student& other){
        if(this == &other)
            return *this;

        this->numarMatricol = other.numarMatricol;
        this->nume = other.nume;
        this->nota = other.nota;
        return *this;
    }

    ~Student(){
        std::cout << "~Student()\n";
    }

    friend std::ostream& operator<<(std::ostream& os, const Student& student){
        //sprintf(str, "Student: nrMat = %d\tnume = %s\tnota = %d\n", student.numarMatricol, student.nume.c_str(), student.nota);
        os << "Student: " << "nrMat = " << student.numarMatricol << "\t" << "nume = " << student.nume
           << "\t" << "nota = " << student.nota << std::endl;
        return os;
    }

    friend std::istream& operator>>(std::istream& is, Student& s){
        is >> s.numarMatricol;
        is>>s.nume;
        is>>s.nota;
        return is;
        
    }
private:

};

//------------------------
class Curs{
private:

    std::list<Student> studenti;
    std::string numeCurs;

public:
    Curs(std::list<Student> studenti, std::string numeCurs){
        this->studenti = studenti;
        this->numeCurs = numeCurs;
    }

    Curs(const Curs& other){
        this->studenti = other.studenti;
        this->numeCurs = other.numeCurs;
    }
    Curs& operator=(const Curs& other){
        if(this == &other)
            return *this;
        this->studenti = other.studenti;
        this->numeCurs = other.numeCurs;
        return *this;
    }

    void InscrieStudent(const Student& student){
        studenti.push_back(student);
    }
    std::vector<Student> GetStudentiPromovati(void)
    {
        std::vector<Student> studentiPromovati;
        for(auto it = studenti.begin(); it != studenti.end(); it++){
            Student& crt = *it;
            if(crt.GetNota() >= 5)
            {
                studentiPromovati.push_back(crt);
            }
        }
        return studentiPromovati;
    }


    friend std::ostream& operator<<(std::ostream& os, const Curs& curs);
};

std::ostream& operator<<(std::ostream& os, const Curs& curs){
    int cnt = 0;
    os << "Afisam studentii la cursul "<<curs.numeCurs << ":" <<std::endl;
    for(auto it = curs.studenti.begin(); it != curs.studenti.end(); it++)
    {
        const Student& student = *it;
        os << student;
        os << "\n";
    }
    os << "-----\n";
    return os;
}



int Student::GetNota(void) const{
    return nota;
}


int main(){
    
    
    std::list<Curs> cursuri;
    std::list<Student> studentiPOO;
    int nrStudentiPOO;
    std::cin >> nrStudentiPOO;
    for(int i=0; i<nrStudentiPOO; i++){
        Student student;
        std::cin >> student;
        studentiPOO.push_back(student);
    }
    Curs poo = Curs(studentiPOO, "Programare Orientata pe Obiecte");
    cursuri.push_back(poo);

    for(auto it = cursuri.begin(); it != cursuri.end(); it++){
        const Curs& curs = *it;
        std::cout<< curs;
    }

    return 0;
}