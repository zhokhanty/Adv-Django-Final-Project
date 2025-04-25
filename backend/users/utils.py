import pyotp

def generate_otp_secret():
    return pyotp.random_base32()

def get_qr_code_uri(user):
    totp = pyotp.TOTP(user.otp_secret)
    return totp.provisioning_uri(name=user.email, issuer_name="backend")

def verify_otp(user, otp_code):
    totp = pyotp.TOTP(user.otp_secret)
    return totp.verify(otp_code)