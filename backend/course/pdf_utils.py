from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from django.conf import settings
import os
from datetime import datetime

def generate_certificate_pdf(user, course):
    cert_dir = os.path.join(settings.MEDIA_ROOT, 'certificates')
    os.makedirs(cert_dir, exist_ok=True)

    filename = f"{user.username}_course_{course.id}.pdf"
    file_path = os.path.join(cert_dir, filename)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Заголовок
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, height - 2 * inch, "Certificate of Completion")

    # Подзаголовок
    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2, height - 3 * inch, f"This certifies that")

    # Имя пользователя
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(width / 2, height - 4 * inch, f"{user.get_full_name()}")

    # Текст курса
    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2, height - 5 * inch, f"has successfully completed the course:")

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 5.7 * inch, f"{course.title}")

    # Дата
    c.setFont("Helvetica", 14)
    date_str = datetime.now().strftime('%d %B %Y')
    c.drawCentredString(width / 2, height - 7 * inch, f"Issued on: {date_str}")

    # Подпись (можно потом картинку вставить)
    c.line(width / 2 - 1.5 * inch, height - 8 * inch, width / 2 + 1.5 * inch, height - 8 * inch)
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 8.3 * inch, "Authorized Signature")

    c.save()

    return f"certificates/{filename}"
