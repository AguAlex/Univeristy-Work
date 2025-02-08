#include "Header.h"
#include <cstdlib>

//Setters for Card
void Card::setName(std::string x){
        name = x;
    }
void Card::setLife(int x){
        life = x;
    }
void Card::setAttack(int x){
        attack = x;
    }

//Getters for Card
int Card::getLife(){
        return life;
    }
int Card::getAttack(){
    return attack;
}
std::string Card::getName(){
    return name;
}



//Supraincararea operatorilor pentru Card
Card::Card(std::string name, int life, int attack){
        this->life = life;
        this->name = name;
        this->attack = attack;
    }

std::ostream& operator<<(std::ostream& os, Card& card){
        //os<<"--------Stats---------"<<std::endl;
        os<<"Name: "<<card.name<<std::endl;
        os<<"Life: "<<card.life<<std::endl;
        os<<"Attack: "<<card.attack<<std::endl;
        return os;
    }

Card Card::operator+(Card& c){
        return Card(c.name, life + c.life, attack + c.attack);
    }

Card& Card::operator+=(Card& c) 
{ 
life += c.life; 
attack += c.attack; 
return *this; 
} 


//Metode Card
void Card::attackAction(Card& oponent){
    oponent.setLife(oponent.getLife() - this->attack);
    this->setLife(this->getLife() - oponent.attack);
}



//Implementari clase derivate

Goblin::Goblin(){
    this->setLife(10);
    this->setAttack(4);
    this->setName("Goblin");

}
Orc::Orc(){
    this->setLife(10);
    this->setAttack(8);
    this->setName("Orc");

}
Knight::Knight(){
    this->setLife(15);
    this->setAttack(8);
    this->setName("Knight");

}
Witch::Witch(){
    this->setLife(8);
    this->setAttack(10);
    this->setName("Witch");
}

//Implementari pentru clasa PLAYER
Player::Player(std::string name, std::vector<Card> c, int cards){
        this->name = name;
        this->cards_number = cards;
        this->cards = c;
    }

std::vector<Card> Player::getCards(){
        return cards;
    }

void Player::setCards(std::vector<Card> v){
        cards.clear();
        for(auto it : v){
            cards.push_back(it);
        }
    }

std::ostream& operator<<(std::ostream& os, Player& p){
    if(p.name == "Computer"){
        os << "Computer Cards: " << std::endl << std::endl;
    }
    else {
        os << "Your Cards: " << std::endl << std::endl;
    }
    int i = 1;
    for(auto it : p.cards){
        if(it.getLife() > 0){
            std::cout << "Card " << i << ":" <<std::endl;
            std::cout << it <<std::endl;
            i ++;
        }
    }
    std::cout<<"------------------------"<<std::endl;
    return os;
}

