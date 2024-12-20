import asyncio
from time import perf_counter

import grpc
from PIL import Image
from io import BytesIO
from inference import inference
import logging
from inference_pb2_grpc import InferenceServer, add_InferenceServerServicer_to_server
from inference_pb2 import InferenceRequest, InferenceResponse

logging.basicConfig(level=logging.INFO)


class InferenceService(InferenceServer):
    def open_image(self, image: bytes) -> Image.Image:
        image = Image.open(BytesIO(image))
        return image

    async def inference(self, request: InferenceRequest, context) -> InferenceResponse:
        logging.info(f"[X] Received request")
        start = perf_counter()
        images = list(map(self.open_image, request.image))
        preds = inference(images)
        logging.info(f"[V] Done in {(perf_counter() - start) * 1000:.2f}ms")
        return InferenceResponse(prediction=preds)


async def serve():
    server = grpc.aio.server()
    add_InferenceServerServicer_to_server(InferenceService(), server)
    address = "localhost:5001"
    server.add_insecure_port(address)
    logging.info(f"[*] Starting server on {address}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())