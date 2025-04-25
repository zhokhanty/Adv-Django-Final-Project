from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import verify_otp, generate_otp_secret, get_qr_code_uri

@api_view(['POST'])
def verify_2fa(request):
    otp = request.data.get('otp')
    user = request.user

    if not user.otp_secret:
        return Response({'error': '2FA is not setup yet'}, status=400)

    if verify_otp(user, otp):
        return Response({'status': 'OTP Verified'})
    
    return Response({'error': 'Invalid OTP'}, status=400)

@api_view(['GET'])
def setup_2fa(request):
    user = request.user

    # Generate and save OTP secret if not exists
    if not user.otp_secret:
        user.otp_secret = generate_otp_secret()
        user.save()

    # Generate QR code URI (to be used with Google Authenticator)
    qr_code_uri = get_qr_code_uri(user)
    return Response({'otp_secret': user.otp_secret, 'qr_code_uri': qr_code_uri})