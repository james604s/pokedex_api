import logging
import traceback

from rest_framework import status
from rest_framework.response import Response

class ResponseWithCallback(Response):
    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        callback=None,
        **kwargs,
    ):
        super().__init__(
            data=data,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
            **kwargs,
        )

        self.callback = callback

    def close(self):
        super().close()
        if self.callback is not None:
            callbacks = self.callback if isinstance(self.callback, list) else [self.callback]
            for callback in callbacks:
                fn, *args = callback
                try:
                    fn(*args)
                except Exception:
                    logging.error(traceback.format_exc())

class ErrorResponse(ResponseWithCallback):
    def __init__(
        self, data="Unknown Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR, callback=None
    ):
        super().__init__({"detail": data}, status=status, callback=callback)
        logging.error(data)