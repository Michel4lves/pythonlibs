class send_email:

    def send(self, remetente, destinatario, assunto, corpo):
        if '@' not in destinatario:
            raise InvalidEmail(f'Email inválido: {destinatario}')
        return destinatario


class InvalidEmail(Exception):
    pass
