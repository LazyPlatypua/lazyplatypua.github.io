Документация для хранения и распространения инструкций для покраски миниатюр. Над документом работаю толяько я в свободное от работы время, так что обновления не регулярны.

Документация создана на основе [Diplodoc](https://diplodoc.com/ru) и [GitHub Pages](https://pages.github.com/).

## Собрать документ

Для сборки документа:

1. Установите [Node.js](https://nodejs.org/en/download/prebuilt-installer).
2. Установите [Builder](https://diplodoc.com/docs/ru/tools/docs/) при помощи команды:

    ```
    npm i @diplodoc/cli -g
    ```

3. Соберите документ при помощи команды:
    ```
    yfm -i .\paint-guide-docs\docs -o .\paint-guide-docs\docs-gen
    ```

    Где:
    * `\paint-guide-docs\docs, -i` — путь до директории проекта;
    * `\paint-guide-docs\docs-gen, -o` — путь до директории, предназначенной для выходных данных (статических HTML).

    Пример:

    ```
    yfm -i D:\Документы\Painting\paint-guide-docs\docs -o D:\Документы\Painting\paint-guide-docs\docs-gen
    ```

4. 