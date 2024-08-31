from django.http import StreamingHttpResponse
from django.views import View
import time

class HelloClaude_V1(View):

    def stream_response(self):
        text = "HELLO CLAUDE"
        for t in text:
            yield f"{t}. "
            time.sleep(1)
            

    def get(self, request, *args, **kwargs):
        response = StreamingHttpResponse(streaming_content=self.stream_response())
        response['Content-Type'] = 'text/event-stream'
        return response
