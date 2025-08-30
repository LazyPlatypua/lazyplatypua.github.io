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

3. Соберите документ при помощи приложения или команды:

   - При помощи приложения
  
     Запустите приложение `build.exe`. Результат выполнения сохранится в файл `build_log.txt`.

   - При помощи команды
  
     Выполните команду:
  
     ```
     yfm -i .\paint-guide-docs\source -o .\paint-guide-docs\miniature-painting
     ```

     Где:
     - `\paint-guide-docs\source, -i` — путь до директории проекта;
     - `\paint-guide-docs\miniature-painting, -o` — путь до директории, предназначенной для выходных данных (статических HTML).

     Пример:

     ```
     yfm -i D:\Документы\Painting\paint-guide-docs\source -o D:\Документы\Painting\paint-guide-docs\miniature-painting
     ```

Документация автоматически соберется в GitHub на основе изменений в папке `source`. Изменения в папке `miniature-painting` не будут добавлены в коммит.

## Добавить серую рамку изображениям

Программа `add-border.py` добавляет серую рамку шириной 1 пиксель всем файлам PNG, JPG, JPEG, BMP и GIF в указанной папке и подпапках. Не используйте для добавления рамки на уже обработанных картинках — ее ширина увеличится на 1 пиксель, а не будет нарисована поверх существующей.
