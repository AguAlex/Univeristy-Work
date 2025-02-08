#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <errno.h>
#include <sys/mman.h>

int main(int argc, char *argv[]){

    int i;
    printf("Starting Parent: %d\n", getpid());

    char shm_name[] = "myshm";
    int shm_fd;

    shm_fd = shm_open(shm_name, O_CREAT|O_RDWR, S_IRUSR | S_IWUSR);
    if (shm_fd < 0) {
        perror(NULL);
        return errno ;
    }

    size_t page_size=getpagesize();
    size_t shm_size = argc * page_size;

    if (ftruncate(shm_fd, shm_size) == -1) {
        perror(NULL);
        shm_unlink(shm_name);
        return errno ;
    }

    char *shm_ptr;
    for(int i = 0; i < argc; i++){
        
        shm_ptr = mmap(0, page_size, PROT_WRITE, MAP_SHARED, shm_fd, page_size*i);
        if (shm_ptr == MAP_FAILED){
            perror(NULL);
            shm_unlink(shm_name);
            return errno;
        }

        pid_t pid=fork();
        if(pid < 0){
            perror(NULL);
            return errno;
        }
        else if(pid == 0){
            int nr = atoi(argv[i+1]);
            shm_ptr += sprintf(shm_ptr, "%d: %d ", nr, nr);
            while(nr > 1){
                if(nr % 2 == 0)
                    nr /= 2;
                else
                    nr = 3*nr + 1;
                shm_ptr += sprintf(shm_ptr, "%d ", nr);
            }
            printf("Done Parent %d Me %d\n", getppid(), getpid());
            return 1;
        }
        munmap(shm_ptr, page_size);
    }
        for(i=1; i<argc; i++)
            wait(NULL);

        for(int i=1; i<argc; i++){
            shm_ptr=mmap(0, page_size, PROT_READ, MAP_SHARED, shm_fd, (i-1)*page_size);
            printf("%s\n", shm_ptr);
            munmap(shm_ptr, page_size);
        }
    shm_unlink(shm_name);
    printf("Done Parent %d Me %d\n", getppid(), getpid());
    

    return 0;
}