from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.execution_number = 1
    
    def open_app(self):
        # Implemente aqui o código para abrir o aplicativo
        pass

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

    def click_sign_email_button(self):
        sign_button = (By.ID, "com.chess:id/text")
        try:
            elemento_sign_email = self.wait.until(EC.element_to_be_clickable(sign_button))
            time.sleep(2)
            self.take_screenshot("1_given", "open_app", "verificar_texto")
            elemento_sign_email.click()
            time.sleep(2)
        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")
    
    def click_email_button(self):
        email_button = (By.ID, "com.chess:id/continueWithEmailBtn")
        try:
            self.take_screenshot("2.1_when", "click_email", "verificar_texto")
            elemento_email = self.wait.until(EC.element_to_be_clickable(email_button))
            elemento_email.click()
            self.take_screenshot("2.2_when", "click_email", "verificar_texto")
        except TimeoutException as te:
            print(f"TimeoutException ao clicar no botão de e-mail: {te}")
        except Exception as e:
            print(f"Erro ao clicar no botão de e-mail: {e}")
    
    def is_error_message_visible(self):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located((By.ID, "com.chess:id/textinput_error")))
            return True
        except TimeoutException:
            return False

    def verify_error_message(self, expected_text):
        error_message_visible = self.is_error_message_visible()
        if error_message_visible:
            error_message = self.get_error_message()
            if error_message == expected_text:
                self.take_screenshot("3_then", "click_email", "verificar_texto")
                return True
                
            else:
                print(f"O texto obtido '{error_message}' não é igual ao texto esperado '{expected_text}'")
                return False
        else:
            print("Mensagem de erro não está visível.")
            return False

    def get_error_message(self):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located((By.ID, "com.chess:id/textinput_error")))
            return elemento.text
        except TimeoutException as e:
            print(f"Erro ao validar a mensagem de erro: {e}")
            return None

    def click_play_as_guest_button(self):
        play_as_guest_button = (By.ID, "com.chess:id/playAsGuest")
        try:
            self.take_screenshot("2.1_when", "click_email", "verificar_texto")
            elemento_play_as_guest = self.wait.until(EC.element_to_be_clickable(play_as_guest_button))
            elemento_play_as_guest.click()
            self.take_screenshot("2.2_when", "click_email", "verificar_texto")
        except TimeoutException as te:
            print(f"TimeoutException ao clicar no botão de e-mail: {te}")
        except Exception as e:
            print(f"Erro ao clicar no botão de e-mail: {e}")
