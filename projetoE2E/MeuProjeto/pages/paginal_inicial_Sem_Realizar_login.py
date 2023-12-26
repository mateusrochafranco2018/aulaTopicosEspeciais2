from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time

class PaginaInicialSemRealizarLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.execution_number = self.load_execution_number()

    def load_execution_number(self):
        execution_file = "execution_number.txt"
        if os.path.exists(execution_file):
            with open(execution_file, "r") as file:
                return int(file.read().strip())
        return 1  # Valor padrão para a primeira execução
    
    def update_execution_number(self):
        execution_file = "execution_number.txt"
        with open(execution_file, "w") as file:
            file.write(str(self.execution_number + 1))
            self.execution_number += 1

    def take_screenshot(self, step_type, step_name, feature_name):
        feature_folder = f"{feature_name}_{self.execution_number}"
        directory = f"evidencia/{feature_folder}"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        step_folder = f"{directory}/{step_type}_{step_name}"
        if not os.path.exists(step_folder):
            os.makedirs(step_folder)
        
        screenshot_path = f"{step_folder}/{feature_folder}.png"
        self.driver.save_screenshot(screenshot_path)
        self.update_execution_number()

    def botao_sing_in_visible(self):
        try:
            time.sleep(5)
            self.wait.until(EC.visibility_of_element_located((By.ID, "com.chess:id/sign_up")))
            return True
        except TimeoutException:
            return False

