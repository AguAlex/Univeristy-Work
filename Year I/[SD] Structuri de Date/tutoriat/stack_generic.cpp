#include <iostream>
#include <vector>
#include <exception>

template <typename T>
class Stack {
private:
    T *stk;
    int top;
    int capacity;
public:
    Stack()
    {
        stk = nullptr;
        top = -1;
        capacity = 1000;
    }
    Stack(const std::vector<T>& stk_)
    {
        if(stk_.size() >= capacity)
        {
            throw std::logic_error("Stack overflow in constructor with array");
        }
        capacity = 1000;
        this->stk = new T[capacity];
        top = stk_.size();
        for(int i = 0; i < top; i++)
            this->stk[i] = stk_[i];
    }
    void Push(T val)
    {
        if(stk == nullptr)
            stk = new T[capacity];
        if(IsFull() == false)
            stk[top++] = val;
        else
            throw std::logic_error("Stack Overflow!");
    }
    T Pop(void)
    {
        if(IsEmpty() == true)
             throw std::logic_error("Stack Underflow!");
        else
            return stk[--top];
        return -1;
    }
    T Peek(void)
    {
        if(top == 0)
            throw std::logic_error("Stack Underflow!");
        else
            return stk[top-1];
        return -1;
    }
    bool IsEmpty(void)
    {
        return top == -1;
    }
    bool IsFull(void)
    {
        return top == capacity-1;
    }
    ~Stack()
    {
        delete[] stk;
    }
};

template <typename T>
void Afisare(T *v, int n)
{
    for(int i = 0; i < n; i++)
        std::cout << v[i] << " ";
    std::cout << std::endl;
}


int main()
{
    Stack<int> stk;
    stk.Push(10);
    stk.Push(20);
    stk.Push(30);
    std::cout << "Peek(): " << stk.Peek() << std::endl;
    std::cout << "Pop(): " << stk.Pop() << std::endl;
    std::cout << "Pop(): " << stk.Pop() << std::endl;
    stk.Push(40);
    std::cout << "Pop(): " << stk.Pop() << std::endl;
    std::cout << "Pop(): " << stk.Pop() << std::endl;
    std::cout << "Pop(): " << stk.Pop() << std::endl;

    return 0;
}