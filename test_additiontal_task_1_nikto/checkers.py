import subprocess
import logging


def checkout(cmd, text):
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

        # Логируем результат выполнения
        logging.info(f"Executed command: {cmd}")
        logging.debug(f"STDOUT: {result.stdout.strip()}")
        logging.debug(f"STDERR: {result.stderr.strip()}")

        if text in result.stdout and result.returncode == 0:
            return True

        if result.returncode != 0:
            logging.warning(f"Command failed with code {result.returncode}: {cmd}")
            logging.warning(f"STDERR: {result.stderr.strip()}")

        return False

    except Exception as e:
        logging.error(f"Unexpected error executing '{cmd}': {e}")
        return False