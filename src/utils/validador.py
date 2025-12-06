import re

class Validador:

    @staticmethod
    def validarCpf(cpf: str) -> bool:
        cpf = cpf.replace('.', '').replace('-', '')

        if not cpf.isdigit() or len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        return True

    @staticmethod
    def validarEmail(email: str) -> bool:
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if re.match(padrao, email):
            return True
        else:
            return False

    @staticmethod
    def validarTel(telefone: str) -> bool:
        tel = telefone.replace('(', '').replace(')', '').replace('-', '')

        if tel.isdigit() and len(tel) != 10 or len(tel) != 11:
            return True
        else:
            return False

    @staticmethod
    def isEmpty(texto: str) -> bool:
        return bool(texto and texto.strip())
