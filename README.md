
# gRPC server with classfication Deep Learning model

Project for demonstrate the application of gRPC to deploy deep learning model using python




## Installation

Install torch and torchvision

```bash
  pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
```
Install gRPC Python SDK
```bash
  pip install -r requirements.txt
```
## Run Locally

Clone the project
In first terminal

```bash
  python src/server.py
```

In second terminal

```bash
  python src/client.py
```


## Authors

- [@Đỗ Ngọc Tuyền](https://www.github.com/stephen-do)


## Tech Stack

**Client:** python

**Server:** python, grpcio, grpcio-tools

