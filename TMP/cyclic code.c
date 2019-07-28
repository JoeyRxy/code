/*(7,3)循环码的编译及纠检错实现*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
/*函数声明*/
void Begin();
void Code();
void Decoding();
/*主函数*/
main()
{
    printf("\n (7,3)cyclic code\n ");
    Begin();
}
/*进行编码*/
void Code()
{
    int Input[3];
    int Output[7];
    int reg[4] = {0, 0, 0, 0};
    int temp, i, j;
    printf("input info code,total 3\n");
    for (i = 0; i < 3; i++)
    {
        printf("%d of 3:\n", i + 1);
        scanf(" %d", &Input[i]); /*输入3位信息码*/
    }
    for (i = 0; i < 3; i++) /*进行除法操作*/
    {
        temp = reg[3] + Input[i]; /*生成多项式为g(x)=x^4+x^3+x^2+1*/
        if (temp == 2)
            temp = 0;
        reg[3] = reg[2] + temp;
        if (reg[3] == 2)
            reg[3] = 0;
        reg[2] = reg[1] + temp;
        if (reg[2] == 2)
            reg[2] = 0;
        reg[1] = reg[0];
        reg[0] = temp;
    }
    for (i = 0; i < 3; i++)
        Output[i] = Input[i]; /*进行编码操作*/
    for (i = 3; i < 7; i++)
    {
        temp = reg[3];
        for (j = 3; j > 0; j--)
            reg[j] = reg[j - 1];
        reg[0] = 0;
        Output[i] = temp;
    }
    printf("________________________________________");
    printf("\n");
    printf("coding result:\n");
    for (i = 0; i < 7; i++)
        printf("  %d  ", Output[i]); /*输出编码结果*/
    printf("\n");
    printf("________________________________________");
    printf("\n");
    Begin();
}
/*译码并进行纠检错*/
void Decoding()
{
    int Input[7], Output[7];
    int reg[4] = {
        0,
        0,
        0,
        0,
    };
    int temp, i, d, x, p;
    printf("\ninput receiving codes,total 7:\n");
    for (i = 0; i < 7; i++)
    {
        printf("%d of 7:\n", i + 1);
        scanf("  %d", &Input[i]); /*输入接受码组*/
    }
    for (i = 0; i < 7; i++) /*进入除法电路*/
    {
        temp = reg[3]; /*计算伴随式S(x)*/
        reg[3] = reg[2] + temp;
        if (reg[3] == 2)
            reg[3] = 0;
        reg[2] = reg[1] + temp;
        if (reg[2] == 2)
            reg[2] = 0;
        reg[1] = reg[0];
        reg[0] = temp + Input[i];
        if (reg[0] == 2)
            reg[0] = 0;
    }
    p = reg[3] + 2 * reg[2] + 4 * reg[1] + 8 * reg[0];
    if (p != 1 && p != 2 && p != 3 && p != 7 && p != 8 && p != 13 && p != 14 && p != 0 && p != 11)
    { /*输入错误位数大于2位*/
        printf("    \"The error >=2\"  \n");
        getchar();
    }
    printf("___________________________________________\n");
    printf("s(x)=");
    for (i = 3; i >= 0; i--)
        printf(" %d", reg[i]);
    printf("\n");
    for (i = 0; i < 7; i++) /*纠正一位错误*/
    {
        d = reg[3] * reg[2] * reg[1] * (!reg[0]);
        Output[i] = d + Input[i];
        if (Output[i] == 2)
            Output[i] = 0;
        temp = reg[3];
        x = 0; /*S(x)进行自发运算以求得错误位数*/
        reg[3] = temp + reg[2];
        if (reg[3] == 2)
            reg[3] = 0;
        reg[2] = reg[1] + temp;
        if (reg[2] == 2)
            reg[2] = 0;
        reg[1] = reg[0];
        reg[0] = temp + x;
    } /*输出3位信息源*/
    printf("The decoding bit3 is:");
    for (i = 0; i < 3; i++)
        printf(" %d ", Output[i]);
    printf("\n");
    printf("The Decoding bit7 is:"); /*输出7位译码结果*/
    for (i = 0; i < 7; i++)
        printf(" %d ", Output[i]);
    printf("\n");
    printf("___________________________________________\n");
    Begin();
}
/*选择操作*/
void Begin()
{
    fflush(stdin);
    char ch;
    printf("    -----------------------------------------------------------------");
    printf("\n");
    printf("    --     input c to code         --");
    printf("\n");
    printf("    --     input d to decode       --");
    printf("\n");
    printf("    --     input e to exit         --");
    printf("\n");
    printf("    -----------------------------------------------------------------");
    printf("\n");
    ch = getchar();
    if (ch == 'c')
        Code();
    else if (ch == 'd')
        Decoding();
    else if (ch == '\n')
        Begin();
    else if (ch == 'e')
        exit(0);
    else
    {
        printf("\"input error\"\n");
        fflush(stdin);
        Begin();
    } /*输入错误提示*/
}