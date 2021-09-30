# Поиск аномалий на временном ряду по количеству логов

1. На входе: размеченный датасет c полями:
   - 5ти минутный таймстемп
   - количество логов за промежуток
   - аномалия (0/1)
2. Требуется: на основе визульного анализа данных сформулировать гипотезу "что является аномалией" и построить модель машинного обучения
3. Решение задачи:
  - Определение сезонности данных на основе визуального анализа
  - "Локальный" визуальный анализ аномалий при помощи кастомной функции `plot_logs` (файл `utils.py)
  - Формулировка гипотезы
  - Генерация фич
  - Настройка модели
  - Анализ интегральных метрик качества предсказаний по:
    - `roc_auc`
    - `precision`
    - `recall`
  - Анализ ошибок модели ("что модель не смогла предсказать")
  - Анализ feature importances (Shap values, теория игр)
4. Предложения по улучшению модели
