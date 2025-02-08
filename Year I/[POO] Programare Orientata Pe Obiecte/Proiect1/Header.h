#ifndef Header
#define Header

#include <iostream>
#include <vector>

class Card{
private:
    std::string name;
    int life;
    int attack;
    
public:
    
    //Constructor de initializare
    Card(std::string name="", int life= -1, int attack= -1);

    //Getteri si setteri
    int getLife();
    int getAttack();
    std::string getName();
    
    void setName(std::string x);
    void setLife(int x);
    void setAttack(int x);

    //Supraincarcare operator << pentru carti
    friend std::ostream& operator<<(std::ostream& os, Card& card);

    //Functia de atac
    void attackAction(Card& oponent);
        
    //Supraincarcarea operatorilor + si +=
    Card operator+(Card& c);
    Card& operator+=(Card& c); 

};

//Tipurile de carti ale jocului
class Goblin : public Card{
public:
    Goblin();
};
class Orc : public Card{
public:
    Orc();
};
class Knight : public Card{
public:
    Knight();
};
class Witch : public Card{
public:
    Witch();
};



class Player{
private:
    int cards_number;
    std::string name;
    std::vector<Card> cards;

public:
    //Constructor de initializare
    Player(std::string name, std::vector<Card> c, int cards=5);

    //Getter si setter pentru vectorul cartilor
    std::vector<Card> getCards();
    void setCards(std::vector<Card> v);
    
    //Supraincarcarea operatorului << pentru afisarea statisticilor playerilor
    friend std::ostream& operator<<(std::ostream& os, Player& p);
};


#endif