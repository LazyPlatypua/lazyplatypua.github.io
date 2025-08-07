Документация для хранения и распространения инструкций для покраски миниатюр. Над документом работает один человек в свободное от работы время, поэтому обновления не регулярны.

Документация создана на основе [Diplodoc](https://diplodoc.com/ru) и [GitHub Pages](https://pages.github.com/).

[Актуальная версия документации](https://lazyplatypua.github.io/miniature-painting/index.html)

## Собрать документ

Для сборки документа:

1. Установите [Node.js](https://nodejs.org/en/download/prebuilt-installer).
2. Установите [Builder](https://diplodoc.com/docs/ru/tools/docs/) при помощи команды:

    ```
    npm i @diplodoc/cli -g
    ```

3. Соберите документ при помощи команды:
    ```
    yfm -i .\paint-guide-docs\source -o .\paint-guide-docs\miniature-painting
    ```

    Где:
    * `\paint-guide-docs\source, -i` — путь до директории проекта;
    * `\paint-guide-docs\miniature-painting, -o` — путь до директории, предназначенной для выходных данных (статических HTML).

    Пример:

    ```
    yfm -i D:\Документы\Painting\paint-guide-docs\source -o D:\Документы\Painting\paint-guide-docs\miniature-painting
    ```

4. Сделайте коммит документа:
   
   * [при помощи GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop#write-a-commit-message-and-push-your-changes);
   * [при помощи Git](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository).

   После добавления изменений в репозиторий, в разделе [Actions](https://github.com/LazyPlatypua/LazyPlatypua.github.io/actions) запустится сборка.

5. На вкладке [Actions](https://github.com/LazyPlatypua/LazyPlatypua.github.io/actions) нажмите на название коммита. После завершения сборки, документ будет размещен на GitHub Pages. Посмотреть его можно по ссылке под надписью **deploy**.
