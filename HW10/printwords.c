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
