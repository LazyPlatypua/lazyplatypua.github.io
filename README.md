Документация для хранения и распространения инструкций для покраски миниатюр. Над документом работаю толяько я в свободное от работы время, так что обновления не регулярны.

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
    yfm -i .\paint-guide-docs\docs -o .\paint-guide-docs\miniature-painting
    ```

    Где:
    * `\paint-guide-docs\docs, -i` — путь до директории проекта;
    * `\paint-guide-docs\miniature-painting, -o` — путь до директории, предназначенной для выходных данных (статических HTML).

    Пример:

    ```
    yfm -i D:\Документы\Painting\paint-guide-docs\docs -o D:\Документы\Painting\paint-guide-docs\miniature-painting
    ```

4. Закомитьте собранную документиацию:
   
   * [при помощи GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop#write-a-commit-message-and-push-your-changes);
   * [при помощи Git](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository).

   После добавления изменений в репозиторий, в разделе [Actions](https://github.com/LazyPlatypua/LazyPlatypua.github.io/actions) запустится сборка.

5. На вкладке [Actions](https://github.com/LazyPlatypua/LazyPlatypua.github.io/actions) нажмите на название коммита. После завершения сборки, документ будет размещен на GitHub Pages. Посмотреть его можно по ссылке ниже под надписью **deploy**.