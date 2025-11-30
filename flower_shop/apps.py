from django.apps import AppConfig
from django.conf import settings
import threading
import logging
import os
import sys

logger = logging.getLogger(__name__)

class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "flower_shop"

    def ready(self):
        import flower_shop.signals  # Импорт сигналов

        # Проверяем, что это не тестовый процесс и не reloader процесс Django
        # RUN_MAIN устанавливается в 'True' только в основном рабочем процессе runserver
        is_test = 'test' in sys.argv or 'pytest' in sys.argv[0]
        is_runserver = 'runserver' in sys.argv
        is_main_process = os.environ.get("RUN_MAIN") == "True"
        
        if not is_test and (not is_runserver or is_main_process):
            logger.info("Запуск Telegram бота...")
            from .telegram_bot import start_bot
            threading.Thread(target=start_bot, daemon=True).start()
        else:
            logger.debug("Пропуск запуска бота: тестовый процесс или reloader.")
