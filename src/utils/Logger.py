import logging
import os
import traceback

class Logger:
    _logger = None

    @classmethod
    def __set_logger(cls):
        if cls._logger is None:
            # Definir el directorio de logs en la raíz del proyecto
            log_directory = 'logs'
            log_filename = 'app.log'

            # Crear la carpeta de logs si no existe
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)

            log_path = os.path.join(log_directory, log_filename)

            # Crear y configurar el logger
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)

            # Crear el manejador de archivos
            file_handler = logging.FileHandler(log_path, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)

            # Configurar el formato de los logs
            formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
            file_handler.setFormatter(formatter)

            # Limpiar handlers previos si existen
            if logger.hasHandlers():
                logger.handlers.clear()

            # Añadir el manejador al logger
            logger.addHandler(file_handler)

            cls._logger = logger

        return cls._logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger()

            if level == "critical":
                logger.critical(message)
            elif level == "debug":
                logger.debug(message)
            elif level == "error":
                logger.error(message)
            elif level == "info":
                logger.info(message)
            elif level == "warn":
                logger.warning(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
