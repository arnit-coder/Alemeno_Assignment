# backend/app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
import cv2
import numpy as np

class UploadImageView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        try:
            file = request.FILES['file']
            npimg = np.frombuffer(file.read(), np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            colors = self.extract_colors(img)
            return Response(colors, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def extract_colors(self, img):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        height, width, _ = img.shape
        section_width = width // 10

        colors = []

        for i in range(10):
            section = hsv_img[:, i * section_width:(i + 1) * section_width]

            section_rgb = cv2.cvtColor(section, cv2.COLOR_HSV2BGR)
            section_rgb = cv2.cvtColor(section_rgb, cv2.COLOR_BGR2RGB)
            avg_color_per_row = np.average(section_rgb, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            avg_color = avg_color.astype(int)  
            colors.append({"r": int(avg_color[0]), "g": int(avg_color[1]), "b": int(avg_color[2])})

        return colors
