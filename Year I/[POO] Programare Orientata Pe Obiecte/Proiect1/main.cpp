#include "Header.h"
#include <iostream>
#include <cstdlib>
#include <vector>
#include <time.h>

//Functie de generare a cartilor
std::vector<Card> generatePlayerCards(){

    std::vector<Card> v;
    for(int i=1; i<=3; i++){
        int randomNumber = std::rand() % 4 + 1;
        Card card;
    switch(randomNumber) {
        case 1:
            card = Goblin();
            break;
        case 2:
            card = Orc();
            break;
        case 3:
            card = Knight();
            break;
        case 4:
            card = Witch();
            break;
        default:
            break;
    }
    v.push_back(card);
    }
    return v;
}



//Functie de verificare in cazul unui castigator si oprire a jocului
bool verificareCastigator(bool p1, bool p2){
    if(p1 == true and p2 == false){
        std::cout<<"!!!!!!!!!!!!"<<std::endl<<"Computer Win !";
        return true;
    }else if(p1 == false and p2 == true){
        std::cout<<"!!!!!!!!!!!!"<<std::endl<<"You win !";
        return true;
    } else if(p1 == true and p2 == true){
        std::cout<<"!!!!!!!!!!!!"<<std::endl<<"Draw !";
        return true;
    }
    return false;
}

//Functia principala cu logica si parcursul jocului
void startGame(Player& p1, Player& p2){
    int playerAttackCard;
    int computerAttackCard;
    static int attackCounter = 1;
    while(true){

        //Cererea input-ului pentru atacurile playerului
        std::cout<<"Choose your card: ";
        std::cin>>playerAttackCard;

        //Verificare input corect
        while(playerAttackCard > p1.getCards().size()){
            std::cout<<"This is not a valid card number. Try Again !"<<std::endl;
            std::cout<<"Choose your card: ";
            std::cin>>playerAttackCard;
        }
        std::cout<<"Choose oponent card: ";
        std::cin>>computerAttackCard;
        while(computerAttackCard > p2.getCards().size()){
            std::cout<<"This is not a valid card number. Try Again !"<<std::endl;
            std::cout<<"Choose oponent card: ";
            std::cin>>computerAttackCard;
        }

        //Actualizarea si verificarea cartilor jucatorilor dupa fiecare atac (folosind vectori auxiliari)
        int playerAttackValue = p1.getCards()[playerAttackCard-1].getAttack();
        int computerAttackValue = p2.getCards()[computerAttackCard-1].getAttack();
        int playerLifeValue = p1.getCards()[playerAttackCard-1].getLife();
        int computerLifeValue = p2.getCards()[computerAttackCard-1].getLife();

        std::vector<Card> auxPlayer = p1.getCards();
        std::vector<Card> auxComputer = p2.getCards();
        auxPlayer[playerAttackCard-1].setLife(playerLifeValue - computerAttackValue);
        auxComputer[computerAttackCard-1].setLife(computerLifeValue - playerAttackValue);

        if(auxPlayer[playerAttackCard-1].getLife() <= 0)
            auxPlayer.erase(auxPlayer.begin()+playerAttackCard-1);
        if(auxComputer[computerAttackCard-1].getLife() <= 0)
            auxComputer.erase(auxComputer.begin()+computerAttackCard-1);

        p1.setCards(auxPlayer);
        p2.setCards(auxComputer);


        std::cout<<"Stats after attack "<<attackCounter<<":"<<std::endl;
            attackCounter++;
        std::cout<<std::endl<<p1<<p2<<std::endl;


        //Verificare castigator
        bool validareP1 = p1.getCards().empty();
        bool validareP2 = p2.getCards().empty();

        bool check = verificareCastigator(validareP1, validareP2);
        if(check == true)
            break;
    }
    
}

int main(){

    //Initializarea jocului prin crearea playerilor si citirea numelui

    srand(time(NULL));
    std::string name;

    std::cout<<"Enter Your Name: ";
    std::cin>>name;

    //Generare carti pentru playeri
    std::vector<Card> cards1 = generatePlayerCards();
    std::vector<Card> cards2 = generatePlayerCards();

    Player p1 = Player(name, cards1);
    std::cout<< "Hello, " << name << "!" << std::endl;
    std::cout<<p1;

    name = "Computer";
    
    Player p2 = Player(name, cards2);

    std::cout<<p2;

    //Functia care porneste jocul
    startGame(p1, p2);

    return 0;
}