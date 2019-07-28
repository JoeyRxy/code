#include <iostream>
// Alphabet length:256
const int len_alphabet = 256;

void radixSort(char *str, int mod, int length, int depth)
{ //str : the str
    //length : str's length
    //mod of {0,1,2}
    //depth of {0,1,2}
    int count[len_alphabet] = {0};
    char c;
    for (int i = 0; i < length; i++)
    {
        c = str[i * 3 + mod];
        count[c]++;
    }
    for (int i = 0; i < len_alphabet; i++)
    {
        count[i] = 0;
    }
}

int *suffixArray(char *str, int length)
{

    int *ans;
    int *R12 = new int[length];
}

int main(int argc, char const *argv[])
{
    char str[] = "";
    int length = 0;
    int *ans = suffixArray(str, length);
    return 0;
}
