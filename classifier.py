import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load pretrained CNN models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load ImageNet class labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    """
    Classifies an image using a specified pretrained CNN model.
    Args:
        img_path (str): Path to the image file to be classified.
        model_name (str): Name of the CNN model ('resnet', 'alexnet', 'vgg').

    Returns:
        str: Predicted label for the image.
    """
    # Open the image file
    img = Image.open(img_path)

    # Define preprocessing steps for the image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Apply preprocessing and add a batch dimension
    img_tensor = preprocess(img).unsqueeze(0)
    
    # Determine PyTorch version
    pytorch_version = list(map(int, __version__.split('.')[:2]))
    
    # Ensure tensor doesn't require gradient (for PyTorch >= 0.4)
    if pytorch_version >= [0, 4]:
        img_tensor.requires_grad_(False)
    else:
        # For PyTorch < 0.4, use Variable with volatile=True for inference
        img_tensor = Variable(img_tensor, volatile=True)

    # Select the model and switch to evaluation mode
    model = models[model_name].eval()
    
    # Perform inference
    if pytorch_version >= [0, 4]:
        output = model(img_tensor)
    else:
        output = model(img_tensor)

    # Extract predicted class index
    pred_idx = output.detach().numpy().argmax()
    
    # Return the corresponding label
    return imagenet_classes_dict[pred_idx]
