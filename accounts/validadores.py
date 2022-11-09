from django.core.exceptions import ValidationError
from validate_docbr import CPF

def valida_cpf(cpf_str:str):

    cpf_valid = CPF()

    if len(cpf_str) < 11 or len(cpf_str) > 16:
        raise ValidationError('CPF com tamanho inválido, tal dado deve conter 11 dígitos.')     
    else:
        try:
            cpf = int(cpf_str)
        except ValueError:
            raise ValidationError('O CPF não pode conter letras, apenas números inteiros.')     

    if cpf_valid.validate(str(cpf)):
        pass
    else:
        raise ValidationError('CPF inválido!')
