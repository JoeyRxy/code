/*************************************************************************
  > File Name: main.c
  > Author: KrisChou
  > Mail:zhoujx0219@163.com 
  > Created Time: Wed 10 Sep 2014 07:44:10 PM CST
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct tag_stack1
{
    int dig_arr[1024];
    int dig_top;
} DIG, *pDIG;

typedef struct tag_stack2
{
    char op_arr[1024];
    int op_top;
} OP, *pOP;

static int is_ok[8][8] =
    {
        //      + - * / % ( # @ )
        /* + */ 0, 0, 0, 0, 0, 1, 1, 0,
        /* - */ 0, 0, 0, 0, 0, 1, 1, 0,
        /* * */ 1, 1, 0, 0, 0, 1, 1, 0,
        /* / */ 1, 1, 0, 0, 0, 1, 1, 0,
        /* % */ 1, 1, 0, 0, 0, 1, 1, 0,
        /* ( */ 1, 1, 1, 1, 1, 1, 1, 1,
        /* # */ 0, 0, 0, 0, 0, 0, 0, 0,
        /* @ */ 1, 1, 1, 1, 1, 1, 1, 0};

static char op_arr[9] = {'+', '-', '*', '/', '%', '(', '#', '@', ')'};

static int find_index(char op)
{
    int index;
    for (index = 0; index < 9; index++)
    {
        if (op == op_arr[index])
        {
            return index;
        }
    }
    return -1;
}

static int is_myspace(char c)
{
    if (c == ' ' || c == '\n' || c == '\t' || c == '\v')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

static void trim_space(char *str)
{
    int slow = -1;
    int fast = 0;
    while (str[fast] != '\0')
    {
        if (!is_myspace(str[fast]))
        {
            str[++slow] = str[fast];
        }
        fast++;
    }
    str[++slow] = '\0';
}

static int calculate(char op, int left, int right)
{
    switch (op)
    {
    case ('+'):
        return left + right;
        break;
    case ('-'):
        return left - right;
        break;
    case ('*'):
        return left * right;
        break;
    case ('/'):
        return left / right;
        break;
    case ('%'):
        return left % right;
        break;
    }
}

int handler(char *str)
{
    OP my_op;
    DIG my_dig;
    memset(&my_op, 0, sizeof(OP));
    memset(&my_dig, 0, sizeof(DIG)); //两个栈，栈顶元素均指向下一个要入栈的位置
    my_op.op_arr[my_op.op_top++] = '#';
    int result = 0;
    int index = 0;
    for (index = 0; str[index] != '\0'; index++)
    {
        int numb;
        if (find_index(str[index]) >= 0 && find_index(str[index] <= 8)) /* 操作符 */
        {
            int left, right;
            char stk_op;
            int tmp_result;
            if (str[index] == ')')
            {
                while (my_op.op_arr[my_op.op_top - 1] != '(') //一直计算直到遇到左括号
                {
                    stk_op = my_op.op_arr[--my_op.op_top];
                    right = my_dig.dig_arr[--my_dig.dig_top];
                    if (stk_op == '@')
                    {
                        tmp_result = -right;
                    }
                    else
                    {
                        left = my_dig.dig_arr[--my_dig.dig_top];
                        tmp_result = calculate(stk_op, left, right);
                    }
                    my_dig.dig_arr[my_dig.dig_top++] = tmp_result; //新操作数入栈
                }
                my_op.op_top--; //'('也出栈
            }
            else
            {

                if ( //操作符为负号
                    str[index] == '-' &&
                    ((index > 0 && find_index(str[index - 1]) >= 0 && find_index(str[index - 1]) <= 4) ||
                     (index > 0 && str[index - 1] == '(') ||
                     (index > 0 && str[index - 1] == '@') ||
                     (index == 0)))
                {
                    str[index] = '@';
                }

                while (1)
                {
                    stk_op = my_op.op_arr[my_op.op_top - 1];
                    if (is_ok[find_index(str[index])][find_index(stk_op)]) //运算符可以进栈
                    {
                        my_op.op_arr[my_op.op_top++] = str[index];
                        break;
                    }
                    else
                    {
                        my_op.op_top--;
                        right = my_dig.dig_arr[--my_dig.dig_top];
                        if (stk_op == '@')
                        {
                            tmp_result = -right;
                        }
                        else
                        {
                            left = my_dig.dig_arr[--my_dig.dig_top];
                            tmp_result = calculate(stk_op, left, right);
                        }
                        my_dig.dig_arr[my_dig.dig_top++] = tmp_result; //新操作数入栈
                    }
                }
            }
        }
        else /* 操作数 */
        {
            numb = 0;
            while (str[index] >= '0' && str[index] <= '9')
            {
                numb = numb * 10 + str[index] - '0';
                index++;
            }
            my_dig.dig_arr[my_dig.dig_top++] = numb;
            index--;
        }
    }

    while (my_op.op_arr[my_op.op_top - 1] != '#')
    {
        int stk_op = my_op.op_arr[--my_op.op_top];
        int right = my_dig.dig_arr[--my_dig.dig_top];
        int tmp_result;
        int left;
        if (stk_op == '@')
        {
            tmp_result = -right;
        }
        else
        {
            left = my_dig.dig_arr[--my_dig.dig_top];
            tmp_result = calculate(stk_op, left, right);
        }
        my_dig.dig_arr[my_dig.dig_top++] = tmp_result; //新操作数入栈
    }
    result = my_dig.dig_arr[--my_dig.dig_top];
    return result;
}

int main(int argc, char *argv[])
{
    int ret;
    char str[1024];
    while (fflush(stdin), memset(str, 0, 1024), fgets(str, 1024, stdin))
    {
        trim_space(str);
        ret = handler(str);
        printf("the result is %d\n", ret);
    }
    return 0;
}