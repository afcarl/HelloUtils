#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

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

        // get first string
        char* ptr2 = strchr(ptr1, ':');
        if (ptr2 == NULL) {
            break;
        }

        int len1 = ptr2 - ptr1;
        char char_array1[20] = {0};
        memcpy(char_array1, ptr1, sizeof(char) * len1);
        printf("  parse first str: %s\n", char_array1);
        string str1(char_array1);
        printf("  parse first string: %s\n\n", str1.c_str());

        ptr2++;
        printf("  ptr2:\n%s\n", ptr2);

        // get second string
        char* ptr3 = strchr(ptr2, ':');
        if (ptr3 == NULL) {
            break;
        }

        int len2 = ptr3 - ptr2;
        char char_array2[20] = {0};
        memcpy(char_array2, ptr2, sizeof(char) * len2);
        printf("  parse second str: %s\n", char_array2);
        string str2(char_array2);
        printf("  parse second string: %s\n\n", str2.c_str());

        // get final float number
        ptr3++;
        printf("  ptr3:\n%s\n", ptr3);

        printf("  parse float: %f\n\n", (float)atof(ptr3));

        //ptr1 = ptr3;
        char* ptr4 = strchr(ptr3, '\n');
        ptr4++;
        printf("  ptr4:\n%s\n", ptr4);
        ptr1 = ptr4;
    }

    return 0;
}
