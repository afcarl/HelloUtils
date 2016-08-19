#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

/*******************************************************\
text file like:

AAAAA:aaaaa:0.333
BBBBB:bbbbb:0.555
DDDDD:ddddd:0.777
\*******************************************************/

int main()
{
    char* str = "AAAAA:aaaaa:0.333\nBBBBB:bbbbb:0.555\nDDDDD:ddddd:0.777\n";
    char *ptr1 = str;

    int count = 0;
    while (ptr1 != NULL) {
        printf("Loop %d\n", ++count);
        printf("  ptr1:\n%s\n", ptr1);

        char* ptr2 = strchr(ptr1, ':');
        if (ptr2 == NULL) {
            break;
        }
        printf("  ptr2:\n%s\n", ++ptr2);

        char* ptr3 = strchr(ptr2, ':');
        if (ptr3 == NULL) {
            break;
        }
        printf("  ptr3:\n%s\n", ++ptr3);

        printf("  parse float: %f\n\n", (float)atof(ptr3));

        ptr1 = ptr3;
    }

    return 0;
}
