# BoulderBrain

BoulderBrain is an algorithm for generating indoor bouldering routes by reusing existing holds in new combinations, multiplying the routes available to climbers on a given wall by several fold. Begun as a project for National Taiwan University's Advanced Human Computer Interaction course. [Demo video here.](https://www.youtube.com/watch?v=pPqtAb81Xyc)

## SAM Installation

The backend calls Segment Anything from **[Meta AI Research, FAIR](https://ai.facebook.com/research/)**; please install it first.

The code requires `python>=3.8`, as well as `pytorch>=1.7` and `torchvision>=0.8`. Please follow the instructions [here](https://pytorch.org/get-started/locally/) to install both PyTorch and TorchVision dependencies. Installing both PyTorch and TorchVision with CUDA support is strongly recommended.

Install Segment Anything:

```
pip install git+https://github.com/facebookresearch/segment-anything.git
```


Click the links below to download the checkpoint for the corresponding model type.

- **`default` or `vit_h`: [ViT-H SAM model.](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth)**

or
```
 !wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
```

## Execute the code


Please input the sample image path, wall information(e.g. id, height, width) in app.py file first.
```
cd backend
python3 app.py
```
