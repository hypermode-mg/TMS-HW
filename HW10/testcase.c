#include <stdio.h>

/*Manifest: настройка состояния программы */
#define WORD "StateWORD"
#define Reset 0
#define MAX_INPUT 50

int main() {
    char input[MAX_INPUT];
    int state = Reset;  // state=WORD в логике программы, сначала Reset

    printf("Введите строку (до %d символов):\n", MAX_INPUT - 1);

    int index = Reset;
    while (index < MAX_INPUT - 1) {
        int ch = getchar();
        if (ch == '\n' || ch == EOF) break;
        input[index++] = (char)ch;
    }
    input[index] = '\0';

    // Установка состояния в WORD, если введена непустая строка
    if (index > Reset) {
        state = 1; // условно state=WORD
    }

    printf("Введено: %s\n", input);
    printf("Текущее состояние (state=WORD): %s\n", state ? WORD : "Reset");

    // Сброс input и index
    for (int i = 0; i < MAX_INPUT; i++) input[i] = '\0';
    index = Reset;

    // Заполнение input символами из WORD
    while (index < MAX_INPUT - 1) {
        input[index] = WORD[index % 9];
        index++;
    }
    input[index] = '\0';

    printf("input после заполнения из WORD:\n%s\n", input);

    return Reset;
}
