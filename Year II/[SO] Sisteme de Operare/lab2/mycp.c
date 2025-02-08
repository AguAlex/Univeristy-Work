#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <errno.h>

int main(int argc, char* argv[])
{
    if (argc != 3) {
        printf("Numar gresit de argumente\n");
        return 0;
    }

    int src_fd, dest_fd;

    src_fd = open(argv[1], O_RDONLY);

    if(src_fd < 0)
    {
        perror("Eroare fisier de intrare.\n");
        return errno;
    }

    dest_fd = open(argv[2], O_WRONLY | O_CREAT , 200);

    if(dest_fd < 0)
    {
        perror("Eroare deschidere fisier copie\n");
        return errno;
    }
    else
    {
        struct stat sb;
        stat(argv[1], &sb);

        int size = sb.st_size;
        char buffer[size];

        read(src_fd, buffer, size);
        write(dest_fd, buffer, size);
    }
    

    close(src_fd);
    close(dest_fd);

    return 0;
}
