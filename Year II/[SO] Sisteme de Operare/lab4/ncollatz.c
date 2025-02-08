#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/errno.h>

void collatz(int x)
{
    while(x!=1)
    {
        if(x%2==0) x/=2;
        else x=3*x+1;
        printf("%d ", x);
    }
}

int main(int argc, char *argv[])
{
    int i;
    printf("Starting Parent %d\n", getpid());
    for(i=1; i<=argc; i++)
    {
        pid_t pid=fork();
        if(pid<0) {perror("Problema cu PID-ul.\n"); return errno;}
        else if(pid==0) 
        {
            int x=atoi(argv[i]);
            printf("%d: %d ", x, x);
            collatz(x);
            printf("\nDone Parent %d Me %d\n",  getppid(), getpid());
            return 1;
        }
    }
    for(i = 1; i <= argc; i++)
        wait(NULL);

    printf("Done Parent %d Me %d\n", getppid(), getpid());

    return 0;
}