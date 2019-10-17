from itsdangerous import TimestampSigner


class Signer:

    def __init__(self, alive_seconds=12 * 60 * 60, secret_key=b'SECRET_KEY'):
        self._alive_seconds = alive_seconds
        self._signer = TimestampSigner(secret_key)

    def sign(self, value):
        return self._signer.sign(value)

    def unsign(self, sign):
        return self._signer.unsign(sign, max_age=self._alive_seconds)
