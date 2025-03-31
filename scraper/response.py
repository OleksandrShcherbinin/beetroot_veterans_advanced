from base import HttpResponse


class JsonResponse(HttpResponse):
    def get(self):
        response = super().get()
        if response:
            return response.json()


class TextResponse(HttpResponse):
    def get(self):
        response = super().get()
        if response:
            return response.text


class BytesResponse(HttpResponse):
    def get(self):
        response = super().get()
        if response:
            return response.content
